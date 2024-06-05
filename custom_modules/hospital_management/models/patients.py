from odoo import api, models, fields, _

class HospitalPatient(models.Model):
    _name ='hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    is_child = fields.Boolean(string="Is Child ?")
    notes = fields.Text(string='Notes')
    gender = fields.Selection([('male', 'Male'),('female', 'Female'), ('others', 'Others')], string='Gender')






