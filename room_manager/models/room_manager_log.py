from odoo import models, fields, api

class RoomManagerLog(models.Model):
    _name = 'room.manager.log'
    _description = 'Room Manager Log'
    _order = 'create_date desc'

    direction = fields.Selection(
        [
            ('incoming', 'Incoming'),
            ('outgoing', 'Outgoing'),
        ],
        string="Direction",
        required=True
    )
    resource_type_id = fields.Many2one(related="resource_id.type_id", string="Resource Type")
    resource_id = fields.Many2one(
        'room.manager.resource',
        string="Resource Name"
    )
    parameter_id = fields.Many2one(
        'room.manager.parameter',
        string="Parameter"
    )
    message = fields.Char(string="Message")
    parameter_value = fields.Char("Parameter Value")
    parameter_value_numeric = fields.Float(compute="_compute_parameter_value_numeric", store=True)
    timestamp = fields.Datetime()


    @api.depends('parameter_value')
    def _compute_parameter_value_numeric(self):
        for record in self:
            record.parameter_value_numeric = float(record.parameter_value) if record.parameter_value.isnumeric() else 0.0
