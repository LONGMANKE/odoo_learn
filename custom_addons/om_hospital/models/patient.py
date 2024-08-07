from odoo import api, fields, models

class hospitalPatient(models.Model):
      _name = "hospital.patient"
      _inherit = ['mail.thread']
      _description= 'Patient Master'


      name = fields.Char(string="Name", required=True)
      date_of_birth = fields.Date(string="DOB")
      gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")