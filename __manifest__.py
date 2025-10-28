{
<<<<<<< HEAD
    'name': 'CRM Lead Extension',
    'version': '1.0',
    'summary': 'Add CRM Lead User field to crm.lead',
    'description': 'Adds a field crm_lead_user_id to track the user on leads.',
    'category': 'CRM',
    'author': 'Mahmoud',
    'depends': ['crm'],
    'data': [
        'views/crm_lead_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
=======
    'name': "Odoo CRM Customizations",
    'summary': "Customizations for the CRM module in Odoo 17",
    'description': "CRM customizations with new menus, security groups, and reports",
    'author': "Mahmoud",
    'website': "https://www.example.com",
    'category': 'Sales/CRM',
    'version': '17.0.1.0.3',
    'depends': ['crm', 'base'],
    'external_dependencies': {
        'python': ['xlsxwriter'],
    },
    'data': [
        'security/crm_lead_security.xml',
        'views/crm_lead_views.xml',
        'data/user_ids.xml',
        'wizards/crm_lead_report_wizard_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
>>>>>>> c44e047 (task report and wizard)
