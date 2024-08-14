from odoo import api, fields, models


class hospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread']
    _description = 'Hospital Appointment'
    _rec_name = "patient_id"

    reference = fields.Char(string="Reference", default='Appointment Code')
    patient_id = fields.Many2one('hospital.patient', string="Patient")
    date_appointment = fields.Date(string="Date", tracking=True)
    note = fields.Text(string="Note")
    state =  fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'),('ongoing', 'Ongoing'),
                               ('done', 'Done'),('cancelled', 'Cancelled')
                               ], string="Gender")


    @api.model_create_multi
    def create(self, vals_list):
      for vals in vals_list:
         if not vals.get('reference') or vals['references'] == 'New':
                  vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
      return super().create(vals_list)
