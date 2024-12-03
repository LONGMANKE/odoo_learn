# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json
from datetime import datetime


class OdooController(http.Controller):
    @http.route('/api/sales_orders', auth='public', methods=['GET'], type='http', csrf=False)
    def get_sales_orders(self, **kwargs):
        try:
            sales_orders = request.env['sale.order'].sudo().search([])
            sales_orders_list = []
            for order in sales_orders:
                sales_orders_list.append({
                    'id': order.id,
                    'name': order.name,
                    'date_order': order.date_order.strftime('%Y-%m-%d %H:%M:%S') if order.date_order else None,
                    'amount_total': order.amount_total,
                    'state': order.state,
                    'customer': order.partner_id.name if order.partner_id else None,
                })
            # Serialize response as JSON
            return request.make_response(json.dumps({
                'status': 'success',
                'data': sales_orders_list
            }), headers=[('Content-Type', 'application/json')])
        except Exception as e:
            return request.make_response(json.dumps({
                'status': 'error',
                'message': str(e)
            }), headers=[('Content-Type', 'application/json')])


class SalesOrderController(http.Controller):
    @http.route('/api/sales_orders1', auth='none', methods=['GET'], type='http', csrf=False)
    def get_sales_orders(self, **kwargs):
        # Step 1: Extract API key from headers
        api_key = request.httprequest.headers.get('Authorization')
        if not api_key or not api_key.startswith('Bearer '):
            return request.make_response(json.dumps({
                'status': 'error',
                'message': 'Unauthorized: API key missing or invalid'
            }), headers=[('Content-Type', 'application/json')], status=401)

        # Step 2: Validate API key
        token = api_key.split("Bearer ")[1]
        user = request.env['res.users'].sudo().search([('api_key', '=', token)], limit=1)
        if not user:
            return request.make_response(json.dumps({
                'status': 'error',
                'message': 'Unauthorized: Invalid API key'
            }), headers=[('Content-Type', 'application/json')], status=401)

        # Step 3: Fetch and return sales orders if authenticated
        try:
            sales_orders = request.env['sale.order'].sudo().search([])
            sales_orders_list = []
            for order in sales_orders:
                sales_orders_list.append({
                    'id': order.id,
                    'name': order.name,
                    'date_order': order.date_order.strftime('%Y-%m-%d %H:%M:%S') if order.date_order else None,
                    'amount_total': order.amount_total,
                    'state': order.state,
                    'customer': order.partner_id.name if order.partner_id else None,
                })
            return request.make_response(json.dumps({
                'status': 'success',
                'data': sales_orders_list
            }), headers=[('Content-Type', 'application/json')])
        except Exception as e:
            return request.make_response(json.dumps({
                'status': 'error',
                'message': str(e)
            }), headers=[('Content-Type', 'application/json')], status=500)


#     @http.route('/odoo_controller/odoo_controller/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_controller.listing', {
#             'root': '/odoo_controller/odoo_controller',
#             'objects': http.request.env['odoo_controller.odoo_controller'].search([]),
#         })

#     @http.route('/odoo_controller/odoo_controller/objects/<model("odoo_controller.odoo_controller"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_controller.object', {
#             'object': obj
#         })
# -*- coding: utf-8 -*-

class SalesOrderAPI(http.Controller):
    @http.route('/api/all/sales_orders', auth='none', type='json', methods=['GET'], csrf=False)
    def get_sales_orders(self):
        """
        Expose sales orders via REST API with API key authentication.
        """
        # Extract the API key from headers
        api_key = request.httprequest.headers.get('Authorization')
        if not api_key or not api_key.startswith("Bearer "):
            return {'status': 'error', 'message': 'Unauthorized: Missing or invalid API key'}

        # Remove "Bearer " from the API key
        api_key = api_key.split(" ")[1]

        # Authenticate the API key
        user = request.env['res.users'].sudo().search([('api_key', '=', api_key)], limit=1)
        if not user:
            return {'status': 'error', 'message': 'Unauthorized: Invalid API key'}

        try:
            # Fetch sales orders (with sudo for elevated privileges)
            sales_orders = request.env['sale.order'].sudo().search([])

            # Build the response data
            response_data = []
            for order in sales_orders:
                response_data.append({
                    'id': order.id,
                    'name': order.name,
                    'date_order': order.date_order.strftime('%Y-%m-%d %H:%M:%S') if order.date_order else None,
                    'amount_total': order.amount_total,
                    'partner': {
                        'id': order.partner_id.id,
                        'name': order.partner_id.name
                    },
                    'state': order.state,
                })

            # Return response
            return {'status': 'success', 'data': response_data}

        except Exception as e:
            return {'status': 'error', 'message': str(e)}
