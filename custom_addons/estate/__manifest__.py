# -*- coding: utf-8 -*-
{
    'name': "Real Estate",

    'summary': "Test Module",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '17.0.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ["crm"],

    # always loaded
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/estate_menus.xml',
        'views/estate_property.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
