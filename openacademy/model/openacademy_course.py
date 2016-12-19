from openerp import fields, models

'''
This module is to create model of Course
'''

class Course(models.Model):
    '''
    This class create model of course
    '''

    _name = "openacademy.course" # Model odoo name

    name = fields.Char(string='Title', required=True)# Field reserved to identified the rec name
    decsription = fields.Text(string='Description') 
    user_id = fields.Many2one('res.users', ondelete='cascade', string='User Responsible')
    session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions G")
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    _sql_constraints = [
        ('name_decsription_check',
         'CHECK(name != decsription)',
         "The title of the course should not be the description"),

        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]
