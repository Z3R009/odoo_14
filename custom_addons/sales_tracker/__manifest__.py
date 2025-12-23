# -*- coding: utf-8 -*-
{
    'name': 'Sales Tracker',
    'version': '1.0',
    'summary': 'Sales Tracker Module',
    'description': '',
    'category': 'Sales',
    'author': 'Your Name',
    'website': 'https://example.com',
    'depends': ['base', 'contacts'],  
    'data': [
        'security/ir.model.access.csv',
        'views/customer_view.xml',
        'views/product_view.xml',
        'views/sale_view.xml',
    ],
    'installable': True,
    'application': True,
}


