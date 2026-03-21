from odoo import models, fields

class RobertTest(models.Model):
    _name = 'robert.test'
    _description = 'Robert Test Model'

    name = fields.Char(string="Title", required=True)
    notes = fields.Text(string="Notes")
    number = fields.Integer(string="Number")