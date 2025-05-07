# -*- coding: utf-8 -*-

from odoo.exceptions import UserError

from odoo import api, fields, models


class School(models.Model):
    _name = "wb.school"
    _description = "This is school profile"

    image = fields.Image("School Image", max_width=128, max_height=128)
    name = fields.Char("School Name")
    invoice_id = fields.Many2one("account.move")
    # this will be a virtual field
    invoice_user_id = fields.Many2one("res.users", related="invoice_id.invoice_user_id")
    # This will be stored in the table //brings also like the search by sales person in  the group by
    # invoice_user_id= fields.Many2one("res.users",  related="invoice_id.invoice_user_id", storable=True)
    invoice_date = fields.Date(related="invoice_id.invoice_date")
    student_list = fields.One2many("wb.student", "school_id", string="Students", readonly=True,
                                   help="This field is used to display related students list for this current school.")

    ref_field_id = fields.Reference(selection=[('wb.school', 'School'),
                                               ('wb.student', 'Student'),
                                               ('wb.hobby', 'Hobby'),
                                               ('sales.order', 'Sale'),
                                               ('account.move', 'Invoice'),
                                               ('purchase.order', 'Purchase'),
                                               ], string="reference",required=True,
                                    help="Please select records accordingly")  # we can use default
    binary_field = fields.Binary(string="Upload file", copy=False)
    binary_file_name = fields.Char("Binary Field Name")
    binary_fields = fields.Many2many("ir.attachment", string="Multi Files Upload")
    # this currency_id is known by default
    # currency_id = fields.Many2one("res.currency", "Currency")
    # amount = fields.Monetary("Amount")

    # use this if like you name the field anything else rather than currency_id
    my_currency_id = fields.Many2one("res.currency", string="(My Currency)")
    amount = fields.Monetary("Amount", currency_field="my_currency_id", default=0)

    def unlink(self):
        print("Unlink Method Call")
        print(self)
        rtn = super(School, self).unlink()
        print(rtn)
        print("Unlink Method finished")
        return rtn

    # def create(self, vals):
    #     print(self)
    #     print(vals)
    #     rtn = super(School, self).create(vals)
    #     print(rtn)
    #     return rtn

    # With decorators
    # @api.model
    # Creates like multiple records in one create.
    @api.model_create_multi
    # Creates like one record in one create.
    # @api.model_create_single
    def create(self, vals):
        print(self)
        print(vals)
        rtn = super(School, self).create(vals)
        # Alternative
        rtn = super().create(vals)
        print(rtn)
        return rtn

    def custom_method(self):
        print("Custom method clicked")
        print(self)
        # search(domain, limit, offset, order)
        # [condition, more condition]

        # this is a blank domain like to get all
        # print(self.search([]))
        print(self.search([], order="id desc"))

        # print(self.search([], order="name"))
        # print(self.search([], limit=5, offset=0))
        # print(self.search([], limit=5, offset=1))
        # print(self.env["wb.student"].search([]))
        # print(self.search([("name", "ilike", "web")]))

        # [('1', '2', '3')]
        # [
        # ('field name', 'condition', 'field value'),
        # ('field name', 'condition', 'field value'),
        # ('field name', 'condition', 'field value')
        # ]
        # select * from school where amount > 1000;

        # select * from school where amount =1000;
        #
        # records =self.search([("amount","=",2000)])
        # self.print_table(records)
        # records =self.search([("name","=","Web")])
        # self.print_table(records)
        # records =self.search([("name","=","web")])
        # self.print_table(records)

        # null is 0 so to avoid conflict we use this false
        # records =self.search([("amount","=", False )])
        # self.print_table(records)

        # False/None mark as true :- 100 Specific value =100
        # records = self.search([("amount", "=?", False)])
        # self.print_table(records)
        # >
        # records = self.search([("amount", ">", 0)])
        # self.print_table(records)

        # >=
        # records = self.search([("amount", ">=", -1)])
        # self.print_table(records)

        # <
        # records = self.search([("amount", "<", 100)])
        # self.print_table(records)

        # <=
        # records = self.search([("amount", "<=", 100)])
        # self.print_table(records)

        # # !=
        # records = self.search([("amount", "!=", 100)])
        # records = self.search([("name", "!=", "Web")])
        # self.print_table(records)

        # in
        records = self.search([("name", "in", ("Web", "web", "Weblearns-3-Record"))])
        self.print_table(records)

        # Method 1
        # self.name = "Single update"
        # self.amount = 5000

        # Method 2 this runs like individually
        # self.update({"name": "Write update", "amount": 50})
        # Method 3 make them run at once // single write ,method
        # self.write({"name": "Write update", "amount": 50})

        # Mass editing
        # records = self.search([], limit=5)
        # print(records)

        # records.write({"name": "Mass Editing", "amount": 1000})

        # Alternative for above
        # for rec in records:
        #     rec.write({"name": f"{rec.id}", "amount":2000})
        pass

    def print_table(self, records):
        print(f"Total Record Found:- {len(records)}")
        print("ID       Name         Amount")
        for rec in records:
            print(f"{rec.id}         {rec.name}            {rec.amount}")
            # print("")
            # print("")

    def write(self, vals):
        print("Write method called")
        print(self)
        print(vals)
        rtn = super(School, self).write(vals)
        print(rtn)
        return rtn


class Student(models.Model):
    _name = 'wb.student'
    _description = 'This is a student profile'

    def delete_records(self):
        print(self)
        school_id = self.env["wb.school"].browse([17, 18, 19, 20, 21])
        for school in school_id:
            if not school.exists():
                raise UserError(f"Recordset is not available! {school}")
                print("Instance or Recordset is not available", school)
            else:
                print("Instance or Recordset is available", school)
        print(school_id)
        print(school_id.unlink())

    # The fields that do not copy are set to copy false individually
    def duplicate_records(self):
        # print(self)
        duplicate_record = self.copy({"joining_date": fields.Datetime.now()})
        # print(duplicate_record)

    @api.returns("self", lambda value: value.id)
    def copy(self, default=None):
        print(self)
        print(default)
        rtn = super(Student, self).copy(default=default)
        print(rtn)
        return rtn

    hobby_list = fields.Many2many("wb.hobby", "student_hobby_list_relation", "student_id", "hobby_id")
    hobby_list_ids = fields.Many2many("wb.hobby", help="Select hobby list for this student")

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
        [('male', 'Male'), ('female', 'Female')], required=True
    )
    advanced_gender = fields.Selection("_get_advanced_gender_list")
    vip_gender = fields.Selection(_get_vip_list, "VIP Gen")

    combobox = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')],
                                string="Combo Box")

    is_default_demo = fields.Boolean(default=True)
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

    @api.onchange("student_fees", "discount_fees")
    # @api.depends("student_fees","discount_fees")
    def _compute_final_fees_cal(self):
        for record in self:
            record.final_fees = record.student_fees - record.discount_fees

    def _get_advanced_gender_list(self):
        return [('male', 'Male'), ('female', 'Female')]

    def json_data_store(self):
        self.school_data = {"name": self.name, "id": self.id, "fees": self.student_fees, "g": self.gender}

    def custom_method(self):
        print("Clicked")

        data = [{"name": "Weblearns-1-Record"},
                {"name": "Weblearns-2-Record"},
                {"name": "Weblearns-3-Record"},
                {"name": "Weblearns-4-Record"},
                {"name": "Weblearns-5-Record"}]

        self.env["wb.school"].create(data)


class Hobby(models.Model):
    _name = "wb.hobby"
    _description = "This is students hobbies"

    name = fields.Char("Hobby Name")
