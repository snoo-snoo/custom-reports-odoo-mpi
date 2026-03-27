# -*- coding: utf-8 -*-
{
    'name': 'Company Report Branding',
    'version': '19.0.1.0.0',
    'category': 'Reporting',
    'summary': 'Per-company letterhead, fonts, and footer/logo modes for PDF reports',
    'description': """
Company-centric report branding (CI)
====================================

Configure letterhead PDF, heading/body fonts, custom footer HTML, and whether
the standard Odoo report logo/footer are shown—per company (multicompany).

Parts of this module were developed with assistance from AI tools; MPI GmbH
remains responsible for review, testing, and compliance.
    """,
    'author': 'MPI GmbH, Michael Plöckinger',
    'website': 'https://www.mpi-erp.at',
    'license': 'LGPL-3',
    'depends': ['web'],
    'data': [
        'report/report_layout_branding.xml',
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
