# -*- coding: utf-8 -*-
############################################################################
#    Module Writen For Odoo, Open Source Management Solution
#
#    coded by: Gabriela Quilarque <gabrielaquilarque97@gmail.com>
############################################################################

from openerp import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    instructor_id = fields.Boolean("Instructor", default=False,
        help="Instructor related to this partner")
    session_ids = fields.Many2many("openacademy.session",
        string="Attended Sessions", readonly=True,
        help="Session Asigned to this partner")
