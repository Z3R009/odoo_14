{
    # name of module (appears in Odoo apps)
    'name': 'Student Enrollment', 
    'version': '1.0',
    'summary': 'Simple student enrollment form',
    'depends': ['base', 'website'],
    'data': [
        
        'views/student_enrollment_report.xml',
        'views/student_enrollment_menu.xml',
        'views/student_enrollment_view.xml',
    ],
    'qweb': [
        'views/website_enrollment_templates.xml',
    ],
    'installable': True,
    'application': True,
}
