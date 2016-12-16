# -*- coding: utf-8 -*-
from openerp import api, fields, models

class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    user_id = fields.Many2one('res.partner', string='Instructor',
                                             domain=['|',('instructor_id', '=', True),
                                                         ('category_id.name', 'ilike', "Teacher")])
    course_id = fields.Many2one('openacademy.course', string='Course', required=True) 
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')
    active = fields.Boolean(default=True)

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats
