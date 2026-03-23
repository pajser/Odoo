from odoo import models, fields


class RoomManagerResource(models.Model):
    _name = 'room.manager.resource'
    _description = 'Room Manager Resource'

    name = fields.Char("Name", required=True)
    type_id = fields.Many2one(comodel_name='room.manager.resource.type', string="Resource Type", required=True,
                              ondelete='restrict')
    allowed_parameter_ids = fields.Many2many(related="type_id.allowed_parameter_ids")
    contains_resource_ids = fields.Many2many(comodel_name='room.manager.resource',
                                              relation="room_manager_resource_resource_rel",
                                              column1="resource_1_id",
                                              column2="resource_2_id",
                                              string="Contains Resources")

    contained_by_resource_ids = fields.Many2many(comodel_name='room.manager.resource',
                                              relation="room_manager_resource_resource_rel",
                                              column1="resource_2_id",
                                              column2="resource_1_id",
                                              string="Contained by Resources")

