# -*- coding: utf-8 -*-
{
    'name': "student",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,
    'license': 'LGPL-3',
    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],
    'auto_install': False,
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/student_view.xml',
        'views/school_view.xml',
        'views/hobby_view.xml',
    ],
}

