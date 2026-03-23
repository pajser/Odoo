from odoo import models, fields


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
    parameter_value = fields.Char("Parameter Value")
    message = fields.Char(string="Message")
    # is_critical = fields.Boolean(
    #     "Is Critical",
    #     compute='_compute_is_critical',
    #     store=True
    # )
    #
    # @api.depends('parameter_id', 'parameter_value')
    # def _compute_is_critical(self):
    #     for rec in self:
    #         if rec.parameter_id:
    #             rec.is_critical = rec.parameter_id.is_critical(rec.parameter_value)
    #         else:
    #             rec.is_critical = False