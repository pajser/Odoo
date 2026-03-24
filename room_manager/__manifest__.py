# __manifest__.py
{
    'name': 'Temperature API',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/room_manager_resource_type_views.xml',
        'views/room_manager_resource_views.xml',
        'views/room_manager_parameter_views.xml',
        'views/room_manager_log_views.xml',
        'views/room_manager_menus.xml',
        'views/temperature_views.xml',

        'data/test_data.xml',
        'data/test_logs.xml',
    ],
    'installable': True,
}