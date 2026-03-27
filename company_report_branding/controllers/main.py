# -*- coding: utf-8 -*-

import base64

from werkzeug.exceptions import NotFound

from odoo import http
from odoo.http import request


class CompanyReportBrandingController(http.Controller):
    @http.route(
        '/company_report_branding/letterhead/<int:company_id>/<string:token>.png',
        type='http',
        auth='public',
    )
    def letterhead_png(self, company_id, token, **kwargs):
        company = request.env['res.company'].sudo().browse(company_id)
        if not company.exists() or company.crb_asset_token != token:
            raise NotFound()
        if not company.crb_letterhead_png:
            raise NotFound()
        data = base64.b64decode(company.crb_letterhead_png)
        return request.make_response(
            data,
            headers=[('Content-Type', 'image/png'), ('Cache-Control', 'private, max-age=3600')],
        )

    @http.route(
        '/company_report_branding/font/<int:company_id>/<string:token>/<string:role>',
        type='http',
        auth='public',
    )
    def font_file(self, company_id, token, role, **kwargs):
        company = request.env['res.company'].sudo().browse(company_id)
        if not company.exists() or company.crb_asset_token != token:
            raise NotFound()
        if role == 'heading':
            raw_b64 = company.crb_font_heading_file
            name = (company.crb_font_heading_filename or '').lower()
        elif role == 'body':
            raw_b64 = company.crb_font_body_file
            name = (company.crb_font_body_filename or '').lower()
        else:
            raise NotFound()
        if not raw_b64:
            raise NotFound()
        data = base64.b64decode(raw_b64)
        if name.endswith('.woff2'):
            ctype = 'font/woff2'
        elif name.endswith('.woff'):
            ctype = 'font/woff'
        elif name.endswith('.ttf'):
            ctype = 'font/ttf'
        elif name.endswith('.otf'):
            ctype = 'font/otf'
        else:
            ctype = 'application/octet-stream'
        return request.make_response(
            data,
            headers=[('Content-Type', ctype), ('Cache-Control', 'private, max-age=86400')],
        )
