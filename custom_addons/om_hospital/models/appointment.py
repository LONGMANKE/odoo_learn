from odoo import api, fields, models

class hospitalAppointment(models.Model):
      _name = "hospital.appointment"
      _inherit = ['mail.thread']
      _description= 'Hospital Appointment'


      patient_id = fields.Many2one('hospital.patient', string="Patient")
      date_appointment = fields.Date(string="Date", tracking= True)
      note = fields.Text(string="Note")
