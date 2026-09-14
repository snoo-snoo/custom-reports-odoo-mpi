# -*- coding: utf-8 -*-
{
    'name': 'Company Report Branding',
    'version': '19.0.1.3.0',
    'category': 'Reporting',
    'summary': 'Per-company PDF letterhead, fonts, logo/footer modes, and HTML notes on quotations, deliveries, POs and invoices',
    'description': """
Company-centric report branding (CI)
====================================

Configure letterhead PDF, heading/body fonts, custom footer HTML, and whether
the standard Odoo report logo/footer are shown—per company (multicompany).
Optional HTML blocks can be printed above and below line tables on sales,
stock, purchase and accounting PDFs.

Parts of this module were developed with assistance from AI tools; MPI GmbH
remains responsible for review, testing, and compliance.
    """,
    'author': 'MPI GmbH, Michael Plöckinger',
    'website': 'https://www.mpi-erp.at',
    'license': 'LGPL-3',
    'images': [
        'static/description/banner.png',
        'static/description/cover.png',
        'static/description/screenshot_settings.png',
        'static/description/screenshot_fonts.png',
        'static/description/screenshot_line_notes.png',
        'static/description/invoice_screenshot.png',
    ],
    'depends': ['web', 'sale', 'stock', 'purchase', 'account'],
    'data': [
        'report/report_layout_branding.xml',
        'report/report_line_notes.xml',
        'views/res_company_views.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            'company_report_branding/static/src/scss/report_branding.scss',
        ],
    },
    'installable': True,
    'application': False,
    'post_init_hook': 'post_init_hook',
}
