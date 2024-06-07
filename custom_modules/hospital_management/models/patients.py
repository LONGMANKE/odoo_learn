from odoo import api, models, fields, _


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = 'mail.thread'
    _description = 'Hospital Patient'

    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    is_child = fields.Boolean(string="Is Child ?", tracking=True)
    notes = fields.Text(string='Notes', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender',
                              tracking=True)
    #  want to store to database it  store=true if we want to edit readonly= False
    capitalized_name = fields.Char(string='Capitalized Name', compute='_compute_capitalized_name', store=True)

    @api.depends('name')
    def _compute_capitalized_name(self):
        for rec in self:
            if rec.name:
                rec.capitalized_name = rec.name.upper()
            else:
                rec.capitalized_name = ''

    @api.onchange('age')
    def _onchange_age(self):
        if self.age <= 10:
            self.is_child = True
        else:
            self.is_child = False
