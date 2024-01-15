# -*- coding: utf-8 -*-
{
    'name': 'Sale Purchase Invoice Serial No in Order lines ',
    'version': '17.0.0.0',
    'author': 'PK Meta Code',
    'summary': 'Serial number in Sale,Purchase and Invoice Order Lines',
    'description': """This module helps to show serial number in sale,purchase, and invoice order lines.""",
    'category': 'Sales,Purchase,Invoice',
    'website': 'tech4sab@gmail.com/',
    'license': 'AGPL-3',
    'depends': ['sale_management','purchase','account'],
    'data': [
        'views/sale_order_views.xml',
        'views/purchase_order_line.xml',
        'views/invoice_order_line.xml',

    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
