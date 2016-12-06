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
