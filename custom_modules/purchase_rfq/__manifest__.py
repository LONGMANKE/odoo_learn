{
    'name': 'Purchase RFQ',
    'Version': '1.0.0',
    'sequence': -100,
    'author': 'Simon Mburu',
    'website': 'https://mburunjoroge.netlify.app/',
    'category': 'Purchase RFQ',
    'summary': 'RFQ',
    'description': 'RFQ different from PO',
    'depends': ['purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_custom_views.xml',
    ],
    'installable': True,
    'auto-install': False,
    'application': False,
    'license': 'LGPL-3',
}
