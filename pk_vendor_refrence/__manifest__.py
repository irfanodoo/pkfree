# -*- coding: utf-8 -*-
{
    'name': "Vendor Reference",
    'summary': """Vendor reference auto by enter the Vendor name""",
    "description": """Vendor reference auto get by entering the vendor name.""",
    'author': 'Irfan Ullah',
    'website': 'https://www.youtube.com/@irfanullah',
    'category': 'product',
    'version': '16.0.0.0',
    'license': 'LGPL-3',
    'depends': ['base', 'product'],
    'data': [
        'views/partner_vendor.xml',

    ],
    'images': ['static/description/banner.png'],

    'installable': True,
    'application': True,
    'auto_install': False,

}
