# controllers/main.py
from odoo import http
from odoo.http import request

class TemperatureController(http.Controller):

    @http.route('/api/room-manager', type='json', auth='public', methods=['POST'], csrf=False)
    def receive_temperature(self, **kwargs):

        resource_id = kwargs.get('resource_id')
        parameter_id = kwargs.get('parameter_id')
        parameter_value = kwargs.get('parameter_value')
        message = kwargs.get('message', '')

        if not isinstance(resource_id, int):
            return {"status": "error", "message": "Resource id must be an integer"}
        if not isinstance(parameter_id, int):
            return {"status": "error", "message": "Parameter id must be an integer"}

        resource = request.env['room.manager.resource'].browse(resource_id)
        if not resource:
            return {"status": "error", "message": f"Resource with id {resource_id} does not exist"}

        parameter = request.env['room.manager.parameter'].browse(parameter_id)
        if not parameter:
            return {"status": "error", "message": f"Parameter with id {parameter_id} does not exist"}

        request.env['room.manager.log'].sudo().create({
            'direction': 'incoming',
            'resource_id': resource.id,
            'parameter_id': parameter.id,
            'parameter_value': str(parameter_value),
            'message': str(message),
        })

        return {"status": "success"}