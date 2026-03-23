from odoo import models, fields


class RoomManagerResourceType(models.Model):
    _name = 'room.manager.resource.type'
    _description = 'Room Manager Resource Type'

    name = fields.Char("Name", required=True)
    allowed_parameter_ids = fields.Many2many(comodel_name="room.manager.parameter", string="Allowed Parameters")