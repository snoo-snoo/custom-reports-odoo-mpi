# -*- coding: utf-8 -*-

import base64
import logging
import secrets
import urllib.parse

from markupsafe import Markup

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None


def _slugify_google_family(name):
    if not name:
        return ''
    return urllib.parse.quote_plus(name.strip().replace(' ', '+'))


class ResCompany(models.Model):
    _inherit = 'res.company'

    crb_asset_token = fields.Char(
        string='Report asset token',
        copy=False,
        groups='base.group_system',
        help='Secret used in URLs for letterhead and font assets in PDF rendering.',
    )
    crb_letterhead_pdf = fields.Binary(
        string='Letterhead PDF',
        attachment=True,
        groups='base.group_system',
    )
    crb_letterhead_pdf_filename = fields.Char(groups='base.group_system')
    crb_letterhead_png = fields.Binary(
        string='Letterhead preview (PNG)',
        attachment=True,
        readonly=True,
        groups='base.group_system',
        help='First page of the letterhead PDF, rasterized for use as report background.',
    )
    crb_use_letterhead = fields.Boolean(
        string='Use letterhead on reports',
        default=False,
        groups='base.group_system',
    )
    crb_margin_top_mm = fields.Float(string='Content margin top (mm)', default=35.0, groups='base.group_system')
    crb_margin_bottom_mm = fields.Float(string='Content margin bottom (mm)', default=25.0, groups='base.group_system')
    crb_margin_left_mm = fields.Float(string='Content margin left (mm)', default=20.0, groups='base.group_system')
    crb_margin_right_mm = fields.Float(string='Content margin right (mm)', default=20.0, groups='base.group_system')

    crb_font_heading_source = fields.Selection(
        selection=[
            ('theme', 'Odoo layout / theme'),
            ('google', 'Google Font'),
            ('upload', 'Uploaded font file'),
        ],
        string='Heading font',
        default='theme',
        required=True,
        groups='base.group_system',
    )
    crb_font_heading_google_family = fields.Char(
        string='Heading Google Font family',
        groups='base.group_system',
        help='E.g. Roboto — used with Google Fonts CSS.',
    )
    crb_font_heading_file = fields.Binary(string='Heading font file', attachment=True, groups='base.group_system')
    crb_font_heading_filename = fields.Char(groups='base.group_system')

    crb_font_body_source = fields.Selection(
        selection=[
            ('theme', 'Odoo layout / theme'),
            ('google', 'Google Font'),
            ('upload', 'Uploaded font file'),
        ],
        string='Body font',
        default='theme',
        required=True,
        groups='base.group_system',
    )
    crb_font_body_google_family = fields.Char(
        string='Body Google Font family',
        groups='base.group_system',
    )
    crb_font_body_file = fields.Binary(string='Body font file', attachment=True, groups='base.group_system')
    crb_font_body_filename = fields.Char(groups='base.group_system')

    crb_footer_mode = fields.Selection(
        selection=[
            ('standard', 'Standard Odoo footer'),
            ('custom', 'Custom HTML footer'),
            ('none', 'No footer text (letterhead / minimal)'),
        ],
        string='Report footer',
        default='standard',
        required=True,
        groups='base.group_system',
    )
    crb_footer_html = fields.Html(
        string='Custom footer HTML',
        translate=True,
        sanitize_attributes=True,
        sanitize_form=True,
        groups='base.group_system',
    )

    crb_logo_mode = fields.Selection(
        selection=[
            ('standard', 'Company logo (standard)'),
            ('none', 'Hide logo'),
            ('custom', 'Custom report logo'),
        ],
        string='Report logo',
        default='standard',
        required=True,
        groups='base.group_system',
    )
    crb_logo_custom = fields.Binary(string='Custom report logo', attachment=True, groups='base.group_system')
    crb_logo_custom_filename = fields.Char(groups='base.group_system')

    crb_rpt_sale_order = fields.Boolean(
        string='Sales quotations & orders',
        default=True,
        groups='base.group_system',
        help='Apply letterhead, fonts, logo/footer modes on sale.order PDF reports (requires Sale app).',
    )
    crb_rpt_stock_picking = fields.Boolean(
        string='Deliveries / pickings',
        default=True,
        groups='base.group_system',
        help='Apply on stock.picking / delivery slip PDF reports (requires Inventory).',
    )
    crb_rpt_purchase_order = fields.Boolean(
        string='Purchase orders',
        default=True,
        groups='base.group_system',
        help='Apply on purchase.order PDF reports (requires Purchase).',
    )
    crb_rpt_customer_invoice = fields.Boolean(
        string='Customer invoices',
        default=True,
        groups='base.group_system',
        help='Apply on customer invoices (account.move, type out_invoice).',
    )
    crb_rpt_credit_note = fields.Boolean(
        string='Customer credit notes',
        default=True,
        groups='base.group_system',
        help='Apply on customer credit notes (account.move, type out_refund).',
    )
    crb_rpt_vendor = fields.Boolean(
        string='Vendor bills & refunds',
        default=True,
        groups='base.group_system',
        help='Apply on vendor bills and refunds (account.move, in_invoice / in_refund).',
    )
    crb_rpt_other = fields.Boolean(
        string='All other PDF reports',
        default=True,
        groups='base.group_system',
        help='Apply on any other model using the external report layout (incl. layout preview).',
    )

    crb_line_note_sale_above = fields.Html(
        string='Sale order — above lines',
        translate=True,
        sanitize_attributes=True,
        sanitize_form=True,
        groups='base.group_system',
    )
    crb_line_note_sale_below = fields.Html(
        string='Sale order — below lines',
        translate=True,
        sanitize_attributes=True,
        sanitize_form=True,
        groups='base.group_system',
    )
    crb_line_note_delivery_above = fields.Html(
        string='Delivery slip — above lines',
        translate=True,
        sanitize_attributes=True,
        sanitize_form=True,
        groups='base.group_system',
    )
    crb_line_note_delivery_below = fields.Html(
        string='Delivery slip — below lines',
        translate=True,
        sanitize_attributes=True,
        sanitize_form=True,
        groups='base.group_system',
    )
    crb_line_note_purchase_above = fields.Html(
        string='Purchase order — above lines',
        translate=True,
        sanitize_attributes=True,
        sanitize_form=True,
        groups='base.group_system',
    )
    crb_line_note_purchase_below = fields.Html(
        string='Purchase order — below lines',
        translate=True,
        sanitize_attributes=True,
        sanitize_form=True,
        groups='base.group_system',
    )
    crb_line_note_out_invoice_above = fields.Html(
        string='Customer invoice — above lines',
        translate=True,
        sanitize_attributes=True,
        sanitize_form=True,
        groups='base.group_system',
    )
    crb_line_note_out_invoice_below = fields.Html(
        string='Customer invoice — below lines',
        translate=True,
        sanitize_attributes=True,
        sanitize_form=True,
        groups='base.group_system',
    )
    crb_line_note_out_refund_above = fields.Html(
        string='Customer credit note — above lines',
        translate=True,
        sanitize_attributes=True,
        sanitize_form=True,
        groups='base.group_system',
    )
    crb_line_note_out_refund_below = fields.Html(
        string='Customer credit note — below lines',
        translate=True,
        sanitize_attributes=True,
        sanitize_form=True,
        groups='base.group_system',
    )
    crb_line_note_vendor_above = fields.Html(
        string='Vendor bill / refund — above lines',
        translate=True,
        sanitize_attributes=True,
        sanitize_form=True,
        groups='base.group_system',
        help='Shown on vendor bills and vendor credit notes (account.move in_invoice / in_refund).',
    )
    crb_line_note_vendor_below = fields.Html(
        string='Vendor bill / refund — below lines',
        translate=True,
        sanitize_attributes=True,
        sanitize_form=True,
        groups='base.group_system',
    )

    @api.constrains('crb_footer_mode', 'crb_footer_html')
    def _check_crb_footer_custom(self):
        for company in self:
            if company.crb_footer_mode == 'custom':
                body = company.crb_footer_html or ''
                if not str(body).strip():
                    raise ValidationError(
                        _('Custom footer HTML is required when footer mode is “Custom HTML footer”.')
                    )

    @api.constrains('crb_logo_mode', 'crb_logo_custom')
    def _check_crb_logo_custom(self):
        for company in self:
            if company.crb_logo_mode == 'custom' and not company.crb_logo_custom:
                raise ValidationError(
                    _('A custom logo file is required when report logo mode is “Custom report logo”.')
                )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('crb_asset_token'):
                vals['crb_asset_token'] = secrets.token_urlsafe(24)
        companies = super().create(vals_list)
        companies._crb_sync_letterhead_png()
        return companies

    def write(self, vals):
        res = super().write(vals)
        if self.env.context.get('crb_skip_letterhead_sync'):
            return res
        if any(
            k in vals
            for k in (
                'crb_letterhead_pdf',
                'crb_font_heading_file',
                'crb_font_body_file',
                'crb_asset_token',
            )
        ):
            self._crb_sync_letterhead_png()
        return res

    def _crb_sync_letterhead_png(self):
        """Rasterize first page of letterhead PDF to PNG when PyMuPDF is available."""
        for company in self:
            if not company.crb_letterhead_pdf:
                if company.crb_letterhead_png:
                    super(ResCompany, company).write({'crb_letterhead_png': False})
                continue
            if not fitz:
                _logger.warning('PyMuPDF (fitz) not installed; letterhead PNG not generated for company %s', company.id)
                continue
            try:
                raw = base64.b64decode(company.crb_letterhead_pdf)
                doc = fitz.open(stream=raw, filetype='pdf')
                try:
                    page = doc.load_page(0)
                    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
                    png_bytes = pix.tobytes('png')
                    super(ResCompany, company.with_context(crb_skip_letterhead_sync=True)).write(
                        {'crb_letterhead_png': base64.b64encode(png_bytes)}
                    )
                finally:
                    doc.close()
            except Exception as e:
                _logger.exception('Could not rasterize letterhead for company %s: %s', company.id, e)

    def _crb_base_url(self):
        return self.env['ir.config_parameter'].sudo().get_param('web.base.url', '').rstrip('/')

    def _crb_letterhead_url(self):
        self.ensure_one()
        if not self.crb_use_letterhead or not self.crb_letterhead_png or not self.crb_asset_token:
            return ''
        return '%s/company_report_branding/letterhead/%s/%s.png' % (
            self._crb_base_url(),
            self.id,
            self.crb_asset_token,
        )

    def _crb_font_url(self, role):
        """role: 'heading' or 'body'."""
        self.ensure_one()
        if not self.crb_asset_token:
            return ''
        return '%s/company_report_branding/font/%s/%s/%s' % (
            self._crb_base_url(),
            self.id,
            self.crb_asset_token,
            role,
        )

    def crb_get_article_wrapper_style(self):
        """CSS for the inner article wrapper (margins + optional letterhead background)."""
        self.ensure_one()
        parts = [
            'box-sizing: border-box',
            'position: relative',
            'min-height: 100%',
        ]
        parts.append('padding-top: %smm' % (self.crb_margin_top_mm or 0.0))
        parts.append('padding-bottom: %smm' % (self.crb_margin_bottom_mm or 0.0))
        parts.append('padding-left: %smm' % (self.crb_margin_left_mm or 0.0))
        parts.append('padding-right: %smm' % (self.crb_margin_right_mm or 0.0))
        url = self._crb_letterhead_url()
        if url:
            parts.append("background-image: url('%s')" % url.replace("'", "%27"))
            parts.append('background-size: cover')
            parts.append('background-repeat: no-repeat')
            parts.append('background-position: top center')
        return '; '.join(parts) + ';'

    def crb_get_typography_css(self):
        """Inline CSS for heading/body font-family (upload + google name)."""
        self.ensure_one()
        rules = []
        if self.crb_font_heading_source == 'google' and self.crb_font_heading_google_family:
            fam = self.crb_font_heading_google_family.strip()
            rules.append(".crb-report-root h1, .crb-report-root h2, .crb-report-root h3, .crb-report-root h4 { font-family: '%s', sans-serif !important; }" % fam.replace("'", ""))
        elif self.crb_font_heading_source == 'upload' and self.crb_font_heading_file:
            rules.append(
                "@font-face { font-family: 'CRBHeading'; src: url('%s'); font-weight: normal; font-style: normal; }"
                % self._crb_font_url('heading').replace("'", "%27")
            )
            rules.append(
                ".crb-report-root h1, .crb-report-root h2, .crb-report-root h3, .crb-report-root h4 { font-family: 'CRBHeading', sans-serif !important; }"
            )
        if self.crb_font_body_source == 'google' and self.crb_font_body_google_family:
            fam = self.crb_font_body_google_family.strip()
            rules.append(".crb-report-root, .crb-report-root body, .crb-report-root .page { font-family: '%s', sans-serif !important; }" % fam.replace("'", ""))
        elif self.crb_font_body_source == 'upload' and self.crb_font_body_file:
            rules.append(
                "@font-face { font-family: 'CRBBody'; src: url('%s'); font-weight: normal; font-style: normal; }"
                % self._crb_font_url('body').replace("'", "%27")
            )
            rules.append(".crb-report-root, .crb-report-root .page { font-family: 'CRBBody', sans-serif !important; }")
        return '\n'.join(rules)

    def crb_build_google_font_link_tags(self):
        """Markup for <head>: Google Fonts stylesheet links for this company."""
        self.ensure_one()
        links = []
        families = set()
        if self.crb_font_heading_source == 'google' and self.crb_font_heading_google_family:
            families.add(self.crb_font_heading_google_family.strip())
        if self.crb_font_body_source == 'google' and self.crb_font_body_google_family:
            fam = self.crb_font_body_google_family.strip()
            if fam not in families:
                families.add(fam)
        for fam in families:
            q = _slugify_google_family(fam)
            if not q:
                continue
            href = 'https://fonts.googleapis.com/css2?family=%s:wght@400;700&display=swap' % q
            links.append('<link rel="stylesheet" href="%s"/>' % href)
        return Markup(''.join(links))

    def _crb_build_extra_head_markup(self):
        """Markup injected into report <head> (Google Fonts + typography CSS)."""
        self.ensure_one()
        parts = [self.crb_build_google_font_link_tags()]
        css = self.crb_get_typography_css()
        if css:
            parts.append(Markup('<style>%s</style>' % css))
        return Markup('').join(parts)

    @api.model
    def _get_report_branding_company(self, docs):
        """Pick company from document records for shared report <head> context."""
        if docs is not None and len(docs):
            rec = docs[:1]
            if rec._name == 'res.company':
                return rec.sudo()
            if 'company_id' in rec._fields and rec.company_id:
                return rec.company_id.sudo()
        return self.env.company.sudo()

    def _crb_normalize_doc_ids(self, doc_ids):
        """Normalize doc ids from ir.actions.report to a list of ints."""
        if doc_ids is None or doc_ids is False:
            return []
        if isinstance(doc_ids, int):
            return [doc_ids]
        try:
            return [int(x) for x in doc_ids if x is not False and x is not None]
        except (TypeError, ValueError):
            return []

    def _crb_should_apply_branding_for_report(self, report, doc_ids):
        """Whether this company’s CI should apply to the given report action."""
        self.ensure_one()
        if not report or not report.model:
            return self.crb_rpt_other
        model_name = report.model
        if model_name not in self.env:
            return self.crb_rpt_other
        if model_name == 'sale.order':
            return self.crb_rpt_sale_order
        if model_name == 'stock.picking':
            return self.crb_rpt_stock_picking
        if model_name == 'purchase.order':
            return self.crb_rpt_purchase_order
        if model_name == 'account.move':
            ids = self._crb_normalize_doc_ids(doc_ids)
            if not ids:
                return (
                    self.crb_rpt_customer_invoice
                    or self.crb_rpt_credit_note
                    or self.crb_rpt_vendor
                    or self.crb_rpt_other
                )
            move = self.env['account.move'].browse(ids[0])
            if not move.exists():
                return self.crb_rpt_other
            mt = move.move_type
            if mt == 'out_invoice':
                return self.crb_rpt_customer_invoice
            if mt == 'out_refund':
                return self.crb_rpt_credit_note
            if mt in ('in_invoice', 'in_refund'):
                return self.crb_rpt_vendor
            return self.crb_rpt_other
        return self.crb_rpt_other
