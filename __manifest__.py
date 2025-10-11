{
<<<<<<< HEAD
    'name': 'Custom CRM',
    'version': '1.0',
    'summary': 'Custom CRM module with Next Call Date field',
    'description': 'Extends CRM Lead with a new field: Next Call Date',
    'author': 'Mahmoud',
    'depends': ['crm'],
    'data': [],
    'installable': True,
    'application': False,
}

=======
    'name': 'Project Custom',
    'version': '1.0',
    'category': 'Project',
    'summary': 'Custom fields and wizard for Project',
    'depends': ['project', 'crm'],
    'data': [
        'views/project_task_views.xml',
        'wizards/project_lead_wizard_views.xml',
        'views/project_security.xml',  # السطر الجديد
    ],
    'installable': True,
    'application': False,
}
>>>>>>> 8a4ef33 (Initial commit: add project_custom module with all tasks)
