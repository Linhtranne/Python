# -*- coding: utf-8 -*-
{
    'name': "TechZone Management - Device Repair",
    
    'summary': "Hệ thống quản lý sửa chữa thiết bị điện tử",
    
    'description': """
        Hệ thống quản lý sửa chữa thiết bị điện tử (điện thoại, laptop, tablet...)
        - Quản lý thiết bị và khách hàng
        - Quản lý phiếu sửa chữa và linh kiện
        - Lịch sử sửa chữa và báo cáo
    """,
    
    'author': "TechZone",
    'website': "https://www.techzone.com",
    
    'category': 'Services/Repair',
    'version': '17.0.1.0.0',
    
    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'mail'],
    
    # always loaded
    'data': [
        'security/repair_security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/repair_line_form.xml',
        'views/repair_order_form.xml',
        'views/repair_order_views.xml',
        'views/device_views.xml',
        'views/repair_appointment_views.xml',
        'views/repair_history_views.xml',
        'views/res_partner_views.xml',
        'views/product_views.xml',
        'views/repair_diagnosis_views.xml',
        'views/repair_order_calendar_views.xml',
        'views/menus.xml',
    ],
    
    # only loaded in demonstration mode
    'demo': [
        'data/demo_data.xml',
    ],
    
    'installable': True,
    'application': True,
    'auto_install': False,

    'assets': {
        'web.assets_backend': [
            'techzone_management/static/src/scss/techzone_backend.scss',
        ],
    },
}

