# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta

class Travel(models.Model):
    
    _name = 'space_mission_odoo.travel'
    _description = 'UNSC Travels across the universe'
    
    spaceship_id = fields.Many2one(comodel_name='space_mission_odoo.spaceship', string='Spaceship', ondelete='cascade', required=True)
    
    name = fields.Char(string='Title', related='spaceship_id.name')
    
    commander_id = fields.Many2one(comodel_name='res.partner', string='Commander')
    
    attendee_ids = fields.Many2many(comodel_name='res.partner', string='Attendees')
    
    start_date = fields.Date(string='Start Date', default=fields.Date.today)
    
    duration = fields.Integer(string='Travel Days', default=7)
    
    end_date = fields.Date(string='End Date', compute='_compute_end_date', inverse='_inverse_end_date', stored=True)
    
    @api.depends('start_date', 'duration')
    def _compute_end_date(self):
        for record in self:
            if not (record.start_date and record.duration):
                record.end_date = record.start_date
            else:
                duration = timedelta(days=record.duration)
                record.end_date = record.start_date + duration
                
    def _inverse_end_date(self):
        for record in self:
            if record.start_date and record.end_date:
                record.duration = (record.end_date - record.start_date).days + 1
            else:
                continue