# -*- coding: utf-8 -*-
{
    'name': 'Water Billing',
    'version': '1.0',
    'summary': 'Water Billing Module',
    'description': '',
    'category': 'Accounting',
    'author': 'Your Name',
    'website': 'https://example.com',
    'depends': ['base', 'account'],  
    'data': [
        'data/sequence_data.xml',
        'data/transaction_sequence.xml',
        'views/member_views.xml',
        # 'views/billing_views.xml',
        'views/read_meter.xml',
        # 'views/history_views.xml',
        'views/usage_graph.xml',
        'report/water_billing_report.xml',
    ],
    'installable': True,
    'application': True,
}