# -*- coding: utf-8 -*-

from odoo.exceptions import ValidationError
from odoo.tests import tagged
from odoo.tests.common import TransactionCase


@tagged('post_install', '-at_install')
class TestCompanyReportBranding(TransactionCase):

    def test_asset_token_on_create(self):
        company = self.env['res.company'].create({'name': 'CRB TestCo'})
        self.assertTrue(company.crb_asset_token)

    def test_footer_custom_requires_html(self):
        company = self.env['res.company'].create({'name': 'CRB FooterCo'})
        with self.assertRaises(ValidationError):
            company.write({'crb_footer_mode': 'custom', 'crb_footer_html': False})

    def test_logo_custom_requires_binary(self):
        company = self.env['res.company'].create({'name': 'CRB LogoCo'})
        with self.assertRaises(ValidationError):
            company.write({'crb_logo_mode': 'custom'})

    def test_get_report_branding_company_res_company_doc(self):
        company = self.env['res.company'].create({'name': 'CRB PreviewCo'})
        picked = self.env['res.company']._get_report_branding_company(company)
        self.assertEqual(picked, company)

    def test_get_report_branding_company_from_company_id_field(self):
        company = self.env.company
        user = self.env.user
        picked = self.env['res.company']._get_report_branding_company(user)
        self.assertEqual(picked, user.company_id)

    def test_article_wrapper_style_padding(self):
        company = self.env.company
        company.crb_margin_top_mm = 11.5
        style = company.crb_get_article_wrapper_style()
        self.assertIn('padding-top: 11.5mm', style)

    def test_rendering_context_includes_head_extra(self):
        report = self.env.ref('web.action_report_externalpreview', raise_if_not_found=False)
        if not report:
            self.skipTest('External preview report (web) not available.')
        data = self.env['ir.actions.report']._get_rendering_context(
            report,
            [self.env.company.id],
            {},
        )
        self.assertIn('crb_report_extra_head', data)
        self.assertIn('crb_apply_branding', data)
        self.assertTrue(data['crb_apply_branding'])

    def test_should_apply_branding_sale_order_flag(self):
        company = self.env.company
        company.crb_rpt_sale_order = False
        if 'sale.order' not in self.env:
            self.skipTest('sale app not installed')
        report = self.env['ir.actions.report'].sudo().search(
            [('model', '=', 'sale.order')],
            limit=1,
        )
        if not report:
            self.skipTest('No ir.actions.report on sale.order')
        self.assertFalse(company._crb_should_apply_branding_for_report(report, []))

    def test_should_apply_branding_other_when_model_unknown(self):
        company = self.env.company
        company.crb_rpt_other = False
        report = self.env['ir.actions.report'].sudo().search(
            [('model', '=', 'res.users')],
            limit=1,
        )
        if not report:
            self.skipTest('No report on res.users')
        self.assertFalse(company._crb_should_apply_branding_for_report(report, []))
