from odoo import api, fields, models, _


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = 'mail.thread'
    _description = "Doctor Records"

    name = fields.Char(string='Name', required=True, tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')],
                              string="Gender", tracking=True)
    ref = fields.Char(string="Reference", required=True)

    # New computed field to store the combination of ref and name
    ref_name = fields.Char(string='Ref Name', compute='_compute_ref_name', store=True)

    _rec_name = 'ref_name'  # Set _rec_name to the new field 'ref_name'

    @api.depends('ref', 'name')
    def _compute_ref_name(self):
        for record in self:
            record.ref_name = f'{record.ref} - {record.name}'
