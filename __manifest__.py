{
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
