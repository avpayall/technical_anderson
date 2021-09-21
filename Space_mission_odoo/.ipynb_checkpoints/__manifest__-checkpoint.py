# -*- coding: utf-8 -*-

{
    'name': 'Space Mission Odoo',
    
    'summary': """This is a Space Mission module for odoo""",
    
    'description': """
        This is a Space Mission module to Mars in Odoo 14
    """,
    
    'author': 'Erwe',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    
    'version': '0.01',
    
    'depends': ['sale'],
    
    'data': [
        'security/space_mission_security.xml',
        'security/ir.model.access.csv',
        'views/space_mission_menuitems.xml',
        'views/spaceship_views.xml',
        'views/travel_views.xml',
        'views/sale_views_inherit.xml',
        'views/resource_views_inherit.xml',
        'wizard/sale_wizard_view.xml',
    ],
    
    'demo': [
        'demo/space_mission_demo.xml',
    ],
}