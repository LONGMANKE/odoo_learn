from odoo import api, fields, models,_
from odoo.exceptions import ValidationError, UserError


class hospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread']
    _description = 'Patient Master'

    name = fields.Char(string="Name", required=True, tracking=True)
    date_of_birth = fields.Date(string="DOB", tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    tag_ids = fields.Many2many('patient.tag', 'patient_tag_rel', 'tag_id', string="Tags")

    def unlink(self):
        for rec in self:
            domain = [('patient_id', '=', rec.id)]
            appointments = self.env['hospital.appointment'].search(domain)
            if appointments:
                raise UserError(_("You cannot delete the patient now.\nAppointments existing for this patient: %s" % rec.name))
                # raise ValidationError(_("You cannot delete the patient now.\nAppointments existing for this patient: %s" % rec.name))
        return super().unlink()
