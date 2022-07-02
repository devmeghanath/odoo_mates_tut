
{
    'name' : 'om_hospital_management',
    'version' : '1.0.0',
    'summary': 'hospital management fesilites ',
    'sequence': -100,
    'description': """
    this is an ozm app
""",
    'category': 'hospital',


    'depends' :['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_views.xml',
        'views/patient_female_view.xml',
        'views/patient_male_view.xml',
        'views/appoinment_views.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,

    'license': 'LGPL-3',
}