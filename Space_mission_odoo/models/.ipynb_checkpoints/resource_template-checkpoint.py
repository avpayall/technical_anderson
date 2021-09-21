# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResourceTemplate(models.Model):
    _inherit = 'product.template'
    
    is_travel_resource = fields.Boolean(string='Use as Travel Resource', help='Check this box to use this as a resource for a Travel', default=False)