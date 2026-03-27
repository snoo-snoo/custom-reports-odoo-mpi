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
        data['crb_report_extra_head'] = company._crb_build_extra_head_markup() if company else Markup('')
        return data
