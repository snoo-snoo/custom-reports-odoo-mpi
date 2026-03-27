# -*- coding: utf-8 -*-

from markupsafe import Markup

from odoo import api, models


class IrActionsReport(models.Model):
    _inherit = 'ir.actions.report'

    @api.model
    def _get_rendering_context(self, report, docids, data):
        data = super()._get_rendering_context(report, docids, data) or {}
        docs = data.get('docs')
        if docs is None and docids is not None and report.model:
            docs = self.env[report.model].browse(docids)
        company = self.env['res.company']._get_report_branding_company(docs)
        apply_branding = True
        if company:
            apply_branding = company._crb_should_apply_branding_for_report(report, docids)
        data['crb_apply_branding'] = apply_branding
        if company and apply_branding:
            data['crb_report_extra_head'] = company._crb_build_extra_head_markup()
        else:
            data['crb_report_extra_head'] = Markup('')
        return data
