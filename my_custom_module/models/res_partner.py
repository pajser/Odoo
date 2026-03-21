from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'  # extend existing partner model

    x_notes = fields.Text(string="Extra Notes")  # new custom field
