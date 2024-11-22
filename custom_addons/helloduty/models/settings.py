# models/settings.py

from odoo import fields, models

class HellodutyModuleSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    helloduty_api_token = fields.Char(
        "Helloduty API Public Token", help="Enter the API public token from Helloduty.")
    auto_create_customers = fields.Boolean("Automatically Create Customers")
    auto_create_agents = fields.Boolean("Automatically Create Agents")
    auto_create_tickets = fields.Boolean("Automatically Create Tickets")
    auto_create_notes = fields.Boolean("Automatically Create Notes")

    # Override get_values to fetch stored values
    def get_values(self):
        res = super(HellodutyModuleSettings, self).get_values()
        # Load each setting from the database using the ir.config_parameter model
        params = self.env['ir.config_parameter'].sudo()
        res.update(
            helloduty_api_token=params.get_param('my_module.helloduty_api_token', default=''),
            auto_create_customers=bool(params.get_param('my_module.auto_create_customers', default=False)),
            auto_create_agents=bool(params.get_param('my_module.auto_create_agents', default=False)),
            auto_create_tickets=bool(params.get_param('my_module.auto_create_tickets', default=False)),
            auto_create_notes=bool(params.get_param('my_module.auto_create_notes', default=False)),
        )
        return res

    # Override set_values to save the new settings values
    def set_values(self):
        super(HellodutyModuleSettings, self).set_values()
        params = self.env['ir.config_parameter'].sudo()
        params.set_param('my_module.helloduty_api_token', self.helloduty_api_token or '')
        params.set_param('my_module.auto_create_customers', self.auto_create_customers)
        params.set_param('my_module.auto_create_agents', self.auto_create_agents)
        params.set_param('my_module.auto_create_tickets', self.auto_create_tickets)
        params.set_param('my_module.auto_create_notes', self.auto_create_notes)
