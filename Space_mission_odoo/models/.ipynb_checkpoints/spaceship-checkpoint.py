# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Spaceship(models.Model):
    
    _name = 'space_mission_odoo.spaceship'
    _description = 'UNSC'
    
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    
    level = fields.Selection(string='Level',
                             selection=[('planetary', 'Planetary'),
                                       ('interstellar', 'Interstellar'),
                                       ('intergalactic', 'Intergalactic')],
                             copy=False)
    
    active = fields.Boolean(string='Commissioned', default=True)
    
    base_cost = fields.Float(string='Base Cost', default=0.00)
    
    fuel_cost = fields.Float(string='Fuel Cost', default=10.00)
    
    total_cost = fields.Float(string='Total Cost', readonly=True)
    
    travel_ids = fields.One2many(comodel_name='space_mission_odoo.travel', inverse_name='spaceship_id', string='Travels')
    
    @api.onchange('base_cost', 'fuel_cost')
    def _onchange_total_cost(self):
        
        if self.base_cost < 0.00:
            raise UserError('Base Cost can not be set as a negative number')
        
        self.total_cost = self.base_cost + self.fuel_cost
        
    @api.constrains('fuel_cost')
    def _check_fuel_cost(self):
        for record in self:
            if record.fuel_cost < 10.00:
                raise ValidationError('The Anti-matter fuel must be at least 10 shmuckles')
        