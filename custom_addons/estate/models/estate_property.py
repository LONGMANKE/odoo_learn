# -*- coding: utf-8 -*-
from odoo import models, fields


class RealEstate(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate Property'

    name = fields.Char(default="House", required=True)
    description = fields.Text()
    postcode = fields.Char()

    def _default_date(self):
        return fields.Date.today()

    date_availability = fields.Date(string="Date Availability", default=_default_date)
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    facades = fields.Integer()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ])
    living_area = fields.Integer()
    garage = fields.Boolean()
    total_area = fields.Integer()
    best_offer = fields.Float()
    active = fields.Boolean(default=True)
    state = fields.Selection([
        ('new', 'New'),
        ('received', 'Offer Received'),
        ('accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('cancelled', 'Cancelled')
    ], required=True, copy=False, default='new')

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
