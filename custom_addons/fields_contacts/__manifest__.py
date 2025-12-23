# -*- coding: utf-8 -*-
{
    'name': 'Custom Contacts Fields',
    'version': '14.0.1.0.0',
    'summary': 'Add first, middle, and last name to Contacts',
    'description': 'Adds first_name, middle_name, last_name fields to res.partner and updates views.',
    'category': 'Contacts',
    'author': 'Your Name',
    'website': 'https://example.com',
    'depends': ['base', 'contacts'],  
    'data': [
        'views/res_partner_view.xml',
    ],
    'installable': True,
    'application': True,
}


