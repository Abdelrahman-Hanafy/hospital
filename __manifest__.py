# -*- coding: utf-8 -*-
{
    'name': "hospital",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr','account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/group.xml',

        'data/seq.xml',

        'views/hospital_doctor_view.xml',
        'views/hospital_patient_view.xml',
        'views/hospital_request_view.xml',
        'views/hospital_patient_visit_view.xml',
        'views/hospital_doctor_availablility_view.xml',

        'views/hospital_menu.xml',
    ],

    'application': True

}

