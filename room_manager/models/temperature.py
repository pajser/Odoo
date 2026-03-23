# models/temperature.py
from odoo import models, fields

class Temperature(models.Model):
    _name = 'temperature'
    _description = 'Temperature Record'

    value = fields.Integer("Temperature")