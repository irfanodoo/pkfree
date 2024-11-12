# -*- coding: utf-8 -*-
{
    'name': "Invoice Report",

    'summary': "add start date and end date to invoice",


    'author': "Irfan Ullah",
    'website': "https://www.lahoreanalytica.com",

    'category': 'Account',
    'version': '17.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base','account_accountant', 'account'],
    'data': [
        # 'security/ir.model.access.csv',
        'report/inherit_invoice_report.xml',
    ],
}

