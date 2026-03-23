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

    def is_critical(self, value):
        """Evaluate whether the given value is critical based on the expression."""
        self.ensure_one()
        try:
            func = eval(self.critical_value_expression)
            return func(value)
        except Exception:
            return False