# -*- coding: utf-8 -*-
{
    'name': "Far",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],


    'data': [
    'views/financing_assessment_business_line_views.xml',
    'views/financing_assessment_form.xml',
    'views/financing_assessment_notebook.xml',
    'views/pages/page_farming.xml',
    'views/pages/page_business.xml',
    'views/pages/page_employment.xml',
    'views/pages/page_others.xml',
    'views/action.xml',
    'views/menu.xml',
],


    
    'installable': True,
    'application': True, 
}
