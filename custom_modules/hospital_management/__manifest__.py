{
    'name': 'Hospital Management',
    'Version': '1.0.0',
    'sequence': -100,
    'author': 'Simon Mburu',
    'website': 'https://mburunjoroge.netlify.app/',
    'category': 'Health',
    'summary': 'Hospital management system',
    'description': 'Hospital management system',
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menu.xml',
        'views/patient.xml',
        'views/doctor.xml',
    ],
    'installable': True,
    'auto-install': False,
    'application': True,
    'license': 'LGPL-3',
}
