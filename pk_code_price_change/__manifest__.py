# -*- coding: utf-8 -*-
{
    'name': "All Products price's change",
    'summary': "All Products prices change of same code when we change the price of one product",
    'author': "Irfan Ullah",
    'website': "https://lahoreanalytica.com",
    'category': 'Uncategorized',
    'version': '17.0.0.0',
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/product_varient.xml',
    ],
}

