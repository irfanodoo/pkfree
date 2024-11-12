# -*- coding: utf-8 -*-
{
    'name': "Employee Portal",

    'summary': "Employee Portal",

    'author': "Irfan Ullah",
    'website': "https://www.lahoreanalytica.com",
    'category': 'Portal',
    'version': '17.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'portal', 'hr_holidays', 'planning'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'security/portal_user_group.xml',
        'views/active_warning_view.xml',
        'views/sop_violation_view.xml',
        'views/portal_announcement_view.xml',
        'views/new_menus_in_portal.xml',
        'views/employee_leave_template.xml',
        'views/sop_violation_template.xml',
        'views/active_warning_template.xml',
        'views/weekly_schedule_template.xml',
        'views/portal_announcement_template.xml',
    ],
}

