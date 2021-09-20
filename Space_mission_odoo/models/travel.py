# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Travel(models.Model):
    
    _name = 'space_mission_odoo.travel'
    _description = 'UNSC Travels across the universe'
    
    spaceship_id = fields.Many2one(comodel_name='space_mission_odoo.spaceship', string='Spaceship', ondelete='cascade', required=True)
    
    name = fields.Char(string='Title', related='spaceship_id.name')
    
    commander_id = fields.Many2one(comodel_name='res.partner', string='Commander')
    
    attendee_ids = fields.Many2many(comodel_name='res.partner', string='Attendees')