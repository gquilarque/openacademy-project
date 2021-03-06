# -*- coding: utf-8 -*-
############################################################################
#    Module Writen For Odoo, Open Source Management Solution
#
#    coded by: Gabriela Quilarque <gabrielaquilarque97@gmail.com>
############################################################################

from openerp import api, fields, models


class Course(models.Model):
    '''
    This class create model of course
    '''
    # Model odoo name
    _name = "openacademy.course"
    # Field reserved to identified the rec name
    name = fields.Char(string='Title', required=True)
    description = fields.Text()
    user_id = fields.Many2one(
        'res.users', ondelete='cascade', string='User Responsible')
    session_ids = fields.One2many(
        'openacademy.session', 'course_id', string="Sessions G")
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', u"Copy of {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(Course, self).copy(default)

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),
        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]
