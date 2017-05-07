# -*- coding: utf-8 -*-
############################################################################
#    Module Writen For Odoo, Open Source Management Solution
#
#    coded by: Gabriela Quilarque <gabrielaquilarque97@gmail.com>
############################################################################
{
    'name': "Open Academy",
    "license": "LGPL-3",
    'summary': """Manage trainings""",
    'author': "Gabriela Quilarque",
    'website': "",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp
    # /addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '8.0.3.3.0',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    'data': [
        'security/security.xml',
        'view/openacademy_course_view.xml',
        'view/openacademy_session_view.xml',
        'view/partner_view.xml',
        'workflow/openacademy_session_workflow.xml',
        'security/ir.model.access.csv',
        'view/openacademy_wizard_view.xml',
        # 'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/openacademy_course_demo.xml',
    ],
    'installable': True,
}
