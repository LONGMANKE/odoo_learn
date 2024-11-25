# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Student(models.Model):
    _name = 'wb.student'
    _description = 'This is a student profile'

    is_paid = fields.Boolean(string="Paid?", default=True, help="This is the field for paid")
    name = fields.Char("Name")
    name1 = fields.Char("Name1")
    name2 = fields.Char("Name2", copy=False)
    name3 = fields.Char("Name3", default="learn")
    name4 = fields.Char("Name4", readonly=True)

    student_name= fields.Char(string="Student", required=True, index=True, size=10)
    address = fields.Text("Student Address", required=True, help="Enter here student address", default="Student address")

    address_html= fields.Html("Address Html", help="This field is use for the dynamic html code to render into the student profile.", copy=False)
