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
