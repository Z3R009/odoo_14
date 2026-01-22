# -*- coding: utf-8 -*-
{
    'name': "Notebook",

    'summary': """
        Notebook""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",


    'category': 'Uncategorized',
    'version': '0.1',


    'depends': ['base'],

    # always loaded
    'data': [
        'views/main_form.xml',
        'views/pages/farming_page.xml',
        'views/pages/business_page.xml',
        'views/pages/employment_page.xml',
        'views/pages/self_employed_page.xml',
        'views/pages/others_page.xml',
        'views/action.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
}
