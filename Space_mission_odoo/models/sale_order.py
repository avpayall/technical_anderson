# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    travel_id = fields.Many2one(comodel_name='space_mission_odoo.travel', string='Related Travel', ondelete='set null')
    
    commander_id = fields.Many2one(string='Travel Commander', related='travel_id.commander_id')
    
    attendee_ids = fields.Many2many(string='Attendees', related='travel_id.attendee_ids')