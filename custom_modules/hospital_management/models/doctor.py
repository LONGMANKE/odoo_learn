from odoo import api, models, fields, _

class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = 'mail.thread'
    _description = 'Doctors Record'

    name = fields.Char(string='Name', required=True, tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender', tracking=True)
    ref = fields.Char(string='Reference', required=True)
