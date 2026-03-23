# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _
from odoo.exceptions import AccessError, MissingError, ValidationError
from odoo.fields import Command
from odoo.http import request, route

from odoo.addons.payment import utils as payment_utils
from odoo.addons.payment.controllers import portal as payment_portal


# The three auth options:
#
# auth='public' — no authentication required
# auth='user' — requires an active Odoo user session
# auth='none' — Odoo does zero auth handling, you manage it yourself (raw access, use with caution)

class NRmNodeRedController(http.Controller):

    @http.route(
        '/room-manager/readings',
        type='json',
        auth='public',
        methods=['GET'],
        csrf=False,
    )
    def receive_readings(self, **kwargs):
        """
        Endpoint to receive room sensor readings.
        Expects a JSON body, e.g.:
        {
            "room_id": 1,
            "temperature": 22.5,
            "humidity": 45.0,
            "timestamp": "2026-03-23T10:00:00"
        }
        """
        data = request.jsonrequest  # parsed JSON body

        room_id = data.get('room_id')
        temperature = data.get('temperature')
        humidity = data.get('humidity')

        if not room_id:
            return {'success': False, 'error': 'room_id is required'}

        # Example: write to a model
        # request.env['room.manager.reading'].sudo().create({
        #     'room_id': room_id,
        #     'temperature': temperature,
        #     'humidity': humidity,
        # })

        return {
            'success': True,
            'message': 'Reading received',
            'data': data,
        }
