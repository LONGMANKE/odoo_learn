from odoo import http
from odoo.http import request
from datetime import datetime


class HellodutyController(http.Controller):
    # POST /helloduty/api/user
    @http.route("/helloduty/api/user", auth="user", type="json")
    def getuser(self):
        user = request.env.user
        return {
            "user_id": user.id,
            "user_name": user.name,
        }
    
    # POST /helloduty/token
    @http.route('/helloduty/settings', type='json', auth='user')
    def get_settings(self):
        # Fetch the settings via ir.config_parameter
        params = request.env['ir.config_parameter'].sudo()
        settings = {
            'token': params.get_param('my_module.helloduty_api_token', default=''),
            'auto_create_customers': bool(params.get_param('my_module.auto_create_customers', default=False)),
            'auto_create_agents': bool(params.get_param('my_module.auto_create_agents', default=False)),
            'auto_create_tickets': bool(params.get_param('my_module.auto_create_tickets', default=False)),
            'auto_create_notes': bool(params.get_param('my_module.auto_create_notes', default=False)),
        }
        return settings

    # POST /helloduty/api/auth { "db": "test_db", "": "", "password": "" }
    @http.route("/helloduty/api/auth", auth="public", type="json")
    def authenticate(self):
        params = request.get_json_data()
        db, username, password = params.get("db"), params.get("username"), params.get("password")

        request.session.authenticate(db, username, password)

        user = request.env.user.read(['id', 'name', 'email'])[0]

        return { 'user': user }

    @http.route("/helloduty/api/whoami", auth="user", type="json")
    def whoami(self):
        return request.env.user.read(['id', 'name','email'])[0]

    @http.route("/helloduty/api/contact", auth="public", type="json")
    def get_contact(self, **kwargs):
        # Access URL parameter
        phone = request.params.get("phone")
        phone = "+" + phone

        # contacts = request.env['res.partner'].search([('phone_sanitized', '=', phone)],limit=1).read([])
        contacts = (
            request.env["res.partner"]
            .search([("phone_sanitized", "=", phone)], limit=1)
            .read(["name", "phone", "phone_sanitized"])
        )
        contact = contacts[0] if len(contacts) > 0 else None

        # Get users
        # request.env['res.users'].search([])

        # Get all contacts ids
        # a = request.env['res.partner'].search([])

        # All contacts
        # a = request.env['res.partner'].search([]).read([])

        # Get all contacts's info
        # a = request.env['res.partner'].search([]).read(['name','phone', 'phone_sanitized'])

        # Get a specific contact's info
        # a = request.env['res.partner'].browse([1]).read(['name','phone'])

        return {"phone": phone, "contact": contact}

    # POST /helloduty/api/contact/create { "name": "Contact name", "phone": "+254..." }
    @http.route("/helloduty/api/contact/create", auth="public", type="json")
    def create_contact(self, **kwargs):

        contacts = (
            request.env["res.partner"]
            .create({"name": kwargs.get("name"), "phone": kwargs.get("phone")})
            .read(["name", "phone", "phone_sanitized"])
        )
        contact = contacts[0] if len(contacts) > 0 else None
        return {"contact": contact}

    @http.route("/helloduty/api/call_ring", auth="public", type="json")
    def call_ring(self):
        params = request.get_json_data()
        id = str(params["id"])
        return {"url": "/web#id=" + id + "&cids=1&model=res.partner&view_type=form"}

    @http.route("/helloduty/api/call_activity/create", auth="public", type="json")
    def create_activity(self, **kwargs):
        # Extract parameters from the request
        contact_id = kwargs.get("contactid")
        activity_message = kwargs.get("notes")

        # Search for the contact
        contact = request.env["res.partner"].browse(int(contact_id))

        if contact:
            # Create closed activity
            activity = (
                request.env["mail.activity"]
                .create(
                    {
                        "activity_type_id": request.env.ref(
                            "mail.mail_activity_data_call"
                        ).id,  # Reference to 'Call' activity type
                        "res_id": contact.id,
                        "res_model_id": request.env.ref(
                            "base.model_res_partner"
                        ).id,  # Reference to 'res.partner' model
                        "note": activity_message,
                    }
                )
                .read([])
            )

            return {"activity": activity[0] if len(activity) > 0 else None}
        else:
            return {}

    @http.route("/helloduty/api/call_activity/finish", auth="public", type="json")
    def finish_activity(self, **kwargs):
        activity_id = kwargs.get("id")
        activity_message = kwargs.get("notes")

        activity = request.env["mail.activity"].browse(int(activity_id))

        if activity:
            activity.action_feedback(feedback=activity_message)

        return None
