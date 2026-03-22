from odoo import models, fields

class CaffeBar(models.Model):
    _name = 'n.caffe.bar'
    _description = 'Caffe Bar'
    name = fields.Char(string="Title", required=True)
    country_id = fields.Many2one(comodel_name = "res.country", string="Country")
    rating = fields.Selection(selection=[('bad', 'Bad'), ('ok', 'OK'), ('good', 'Good')])