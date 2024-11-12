# -*- coding: utf-8 -*-
{
    'name': "Outstanding Payment Report",

    'summary': "customer/vendor outstanding payment report along with ageing",

    'author': "Irfan Ullah",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '17.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'report/invoice_report.xml',
    ],
}

