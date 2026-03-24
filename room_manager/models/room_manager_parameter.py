from odoo import models, fields, api
from odoo.exceptions import ValidationError


class RoomManagerParameter(models.Model):
    _name = 'room.manager.parameter'
    _description = 'Room Manager Parameter'

    name = fields.Char("Name", required=True)
    code = fields.Char("Code", required=True)
    value_type = fields.Selection(
        [('numeric', 'Numeric'), ('boolean', 'Boolean'),],
        string="Value Type",
        default='numeric',
        required=True
    )
    critical_value_expression = fields.Char(
        "Critical Value Expression",
        default="lambda v: v > 28 or v < 12",
        help="Python lambda expression to evaluate if a value is critical. "
             "Example: lambda v: v > 28 or v < 12"
    )



    def action_graph(self):
        self.ensure_one()
        context = self.env.context
        resource_id = context.get('params', {}).get('resId', False)

        if not resource_id:
            return

        return {
            'type': 'ir.actions.act_window',
            'name': 'Log Entries Graph',
            'res_model': 'room.manager.log',
            'view_mode': 'graph',
            'views': [(False, 'graph')],
            'target': 'new',
            'domain': [('resource_id', '=', resource_id), ('parameter_id', '=', self.id)],
            'context': {
                'group_by': ['create_date'],
            },
        }
