# -*- coding: utf-8 -*-
{
    'name': 'Company Report Branding eLearning',
    'version': '19.0.1.0.0',
    'category': 'Website/eLearning',
    'summary': 'Anwenderkurs: PDF-Berichte im Corporate Design gestalten',
    'description': """
E-Learning-Kurs für das Modul Company Report Branding.

Installiert einen veröffentlichten Trainingskurs in der App eLearning
(website_slides) mit Artikeln, PDF-Handbuch, Quiz und Download-Videos.

Zielgruppe: Administration / Büroleitung, keine Programmierkenntnisse.
    """,
    'author': 'MPI GmbH, Michael Plöckinger',
    'website': 'https://www.mpi-erp.at',
    'license': 'LGPL-3',
    'depends': ['website_slides'],
    'data': [
        'data/slide_channel_data.xml',
    ],
    'installable': True,
    'application': False,
}
