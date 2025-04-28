# -*- coding: utf-8 -*-

from odoo import api, fields, models
import time


class School(models.Model):
    _name = "wb.school"
    _description = "This is school profile"

    name = fields.Char("School Name")
    invoice_id = fields.Many2one("account.move")
    #this will be a virtual field
    invoice_user_id= fields.Many2one("res.users",  related="invoice_id.invoice_user_id")
    #This will be stored in the table //brings also like the search by sales person in  the group by
    # invoice_user_id= fields.Many2one("res.users",  related="invoice_id.invoice_user_id", storable=True)
    invoice_date= fields.Date(related="invoice_id.invoice_date")
    student_list = fields.One2many("wb.student", "school_id", string="Students", readonly=1,
                                   help="This field is used to display related students list for this current school.")

    ref_field_id = fields.Reference(selection=[('wb.school','School'),
                                     ('wb.student','Student'),
                                     ('wb.hobby','Hobby'),
                                     ('sales.order','Sale'),
                                     ('account.move','Invoice'),
                                     ('purchase.order','Purchase'),
                                     ], string="reference", required=1, help="Please select records accordingly") #we can use default
    binary_field = fields.Binary(string="Upload file", copy=False)
    binary_file_name = fields.Char("Binary Field Name")
    binary_fields = fields.Many2many("ir.attachment", string="Multi Files Upload")
    #this currency_id is known by default
    # currency_id = fields.Many2one("res.currency", "Currency")
    # amount = fields.Monetary("Amount")

    #use this if like you name the field anything else rather than currency_id
    my_currency_id = fields.Many2one("res.currency", string="(My Currency)", )
    amount = fields.Monetary("Amount", currency_field="my_currency_id")

class Student(models.Model):
    _name = 'wb.student'
    _description = 'This is a student profile'

    hobby_list = fields.Many2many("wb.hobby", "student_hobby_list_relation","student_id","hobby_id")
    hobby_list_ids = fields.Many2many("wb.hobby"
                                      )
    # school_id = fields.Many2one("wb.school")
    # school_id = fields.Many2one("wb.school", "School Name")
    school_id = fields.Many2one(comodel_name="wb.school")

    # date and time field
    # joining_date = fields.Datetime(copy=False, default="2024-12-01 00:00:00")
    joining_date = fields.Datetime(copy=False, default=fields.Datetime.now)
    # joining_date = fields.Datetime(copy=False, default=fields.Datetime.now())

    # date fields
    # joining_date = fields.Date(string="Joining DT", default='2024-12-01')
    # joining_date = fields.Date(string="Joining DT", default=fields.Date.today())
    # joining_date = fields.Date(string="Joining DT", default=fields.Date.today)
    # joining_date = fields.Date(string="Joining DT", default=fields.Date.context_today)
    #
    # start_date = fields.Date(default= time.strftime("%Y-01-01"))
    # end_date = fields.Date(default= time.strftime("%Y-12-31"))

    school_data = fields.Json()

    @api.model
    def _get_vip_list(self):
        return [('a', '1'), ('b', '2'), ('c', '3')]

    student_fees = fields.Float(digits="Student Fees", help="Please Enter Student fees")
    discount_fees = fields.Float("Discount")
    roll_number = fields.Integer("Enrollment NO", index=True)
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')], required=1
    )
    advanced_gender = fields.Selection("_get_advanced_gender_list")
    vip_gender = fields.Selection(_get_vip_list, "VIP Gen")

    combobox = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')],
                                string="Combo Box")

    is_default_demo = fields.Boolean(default=True, required=1)
    is_paid = fields.Boolean(string="Paid?", default=True, help="This is the field for paid")

    name = fields.Char("Name")
    name1 = fields.Char("Name1")
    name2 = fields.Char("Name2", copy=False)
    name3 = fields.Char("Name3", default="learn")
    name4 = fields.Char("Name4", readonly=True)

    student_name = fields.Char(string="Student", required=True, index=True, size=10)
    address = fields.Text("Student Address", required=True, help="Enter here student address",
                          default="Student address")

    address_html = fields.Html("Address Html",
                               help="This field is use for the dynamic html code to render into the student profile.",
                               copy=False)
    # autoupdate when i type the address above
    compute_address_html = fields.Html(string="Compute Address Field")
    final_fees = fields.Float("Final Fees", compute="_compute_final_fees_cal", store=True)

    @api.onchange("address_html")
    def onchange_address_html_field(self):
        for record in self:
            record.compute_address_html = record.address_html

    @api.onchange("student_fees","discount_fees")
    # @api.depends("student_fees","discount_fees")
    def _compute_final_fees_cal(self):
        for record in self:
            record.final_fees = record.student_fees - record.discount_fees
    def _get_advanced_gender_list(self):
        return [('male', 'Male'), ('female', 'Female')]

    def json_data_store(self):
        self.school_data = {"name": self.name, "id": self.id, "fees": self.student_fees, "g": self.gender}


class Hobby(models.Model):
    _name = "wb.hobby"
    _description = "This is students hobbies"

    name = fields.Char("Hobby Name")
