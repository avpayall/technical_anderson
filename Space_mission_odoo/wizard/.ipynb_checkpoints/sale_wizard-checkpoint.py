# -*- coding: utf-8 -*-

from odoo import models, fields, api

class  SaleWizard(models.TransientModel):
    _name = 'space_mission_odoo.sale.wizard'
    _description = 'Wizard: Quick sale orders for travel attendees'
    
    def _default_travel(self):
        return self.env['space_mission_odoo.travel'].browse(self._context.get('active_id'))
    
    travel_id = fields.Many2one(comodel_name='space_mission_odoo.travel', string='Travel', required=True, default=_default_travel)
    
    travel_attendee_ids = fields.Many2many(comodel_name='res.partner',
                                           string='Attendees in current Travel', 
                                           related='travel_id.attendee_ids', 
                                           help='These are the attendees in the current travel')
    
    attendee_ids = fields.Many2many(comodel_name='res.partner',
                                    string='Attendees for sale order')
    
    def create_sale_orders(self):
        
        travel_resource_id = self.env['product.product'].search([('is_travel_resource', '=', True)], limit=1)
        if travel_resource_id:
            for attendee in self.attendee_ids:
                order_id = self.env['sale.order'].create({
                    'partner_id': attendee.id,
                    'travel_id': self.travel.id,
                    'order_line':[(0,0, {'product_id': travel_resource_id.id, 'price_unit': self.travel_id.total_cost})]
                })