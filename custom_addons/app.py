
# After Swagger impelementation

from flask import Flask, jsonify, request
import xmlrpc.client
from dotenv import load_dotenv
import os
from flasgger import Swagger, swag_from

# Load environment variables from .env file
load_dotenv()

# Fetch values from environment variables
url = os.getenv('ODOO_URL')  # Odoo URL
db = os.getenv('ODOO_DB')  # Database name
username = os.getenv('ODOO_USERNAME')  # Odoo login
api_key = os.getenv('ODOO_API_KEY')  # API key

# Flask app initialization
app = Flask(__name__)

# Initialize Swagger
swagger = Swagger(app)


def fetch_sales_orders():
    """
    Fetch sales orders from Odoo using XML-RPC.
    """
    try:
        # Authenticate
        common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
        uid = common.authenticate(db, username, api_key, {})
        if not uid:
            return {"status": "error", "message": "Authentication failed"}

        # Access model methods
        models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")

        # Fetch sales orders
        domain = []  # Add filters if needed, e.g., [['state', '=', 'sale']]
        fields = ['name', 'date_order', 'amount_total', 'partner_id', 'state']

        sales_orders = models.execute_kw(
            db, uid, api_key,  # Use API Key in place of password
            'sale.order',  # Model
            'search_read',  # Method
            [domain],  # Domain (filter conditions)
            {'fields': fields, 'limit': 10}  # Additional options
        )
        return {"status": "success", "data": sales_orders}

    except Exception as e:
        return {"status": "error", "message": str(e)}


def fetch_chart_of_accounts():
    """
    Fetch chart of accounts from Odoo using XML-RPC, and process the JSONB 'name' field.
    """
    try:
        # Authenticate
        common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
        uid = common.authenticate(db, username, api_key, {})
        if not uid:
            return {"status": "error", "message": "Authentication failed"}

        # Access model methods
        models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")

        # Fetch chart of accounts
        domain = []  # Add filters if needed
        fields = ['id', 'code', 'account_type', 'internal_group', 'name']

        accounts = models.execute_kw(
            db, uid, api_key,  # Use API Key in place of password
            'account.account',  # Model
            'search_read',  # Method
            [domain],  # Domain (filter conditions)
            {'fields': fields, 'limit': 20}  # Additional options
        )

        # Process accounts to format the response
        formatted_accounts = []
        for account in accounts:
            # Extract 'name' from JSONB-like structure (e.g., {"en_US": "Account Receivable"})
            account_name = account['name'].get('en_US', "N/A") if isinstance(account['name'], dict) else account['name']

            # Add the required fields to the formatted response
            formatted_accounts.append({
                'id': account['id'],
                'code': account['code'],
                'account_type': account['account_type'],
                'internal_group': account.get('internal_group', "N/A"),
                'name': account_name
            })

        return {"status": "success", "data": formatted_accounts}

    except Exception as e:
        return {"status": "error", "message": str(e)}


# API route for Sales Orders
@app.route('/api/sales_orders', methods=['GET'])
@swag_from({
    'tags': ['Sales Orders'],
    'summary': 'Fetch Sales Orders',
    'description': 'Fetch sales orders from Odoo via XML-RPC.',
    'responses': {
        200: {
            'description': 'List of sales orders',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {'type': 'string'},
                    'data': {'type': 'array', 'items': {'type': 'object'}}
                }
            }
        }
    }
})
def get_sales_orders():
    """
    Public API to fetch sales orders.
    """
    result = fetch_sales_orders()
    return jsonify(result)


# API route for Chart of Accounts
@app.route('/api/chart_of_accounts', methods=['GET'])
@swag_from({
    'tags': ['Chart of Accounts'],
    'summary': 'Fetch Chart of Accounts',
    'description': 'Fetch chart of accounts from Odoo via XML-RPC.',
    'responses': {
        200: {
            'description': 'List of chart of accounts',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {'type': 'string'},
                    'data': {'type': 'array', 'items': {'type': 'object'}}
                }
            }
        }
    }
})
def get_chart_of_accounts():
    """
    Public API to fetch the chart of accounts.
    """
    result = fetch_chart_of_accounts()
    return jsonify(result)


# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


# before swagger
# from flask import Flask, jsonify, request
# import xmlrpc.client
# from dotenv import load_dotenv
# import os
#
# # Load environment variables from .env file
# load_dotenv()
# # ODOO_URL=url
# # ODOO_DB=dbname
# # ODOO_USERNAME=email
# # ODOO_API_KEY=apikey
#
# # Fetch values from environment variables
# url = os.getenv('ODOO_URL')  # Odoo URL
# db = os.getenv('ODOO_DB')  # Database name
# username = os.getenv('ODOO_USERNAME')  # Odoo login
# api_key = os.getenv('ODOO_API_KEY')  # API key
#
# # Flask app initialization
# app = Flask(__name__)
#
#
# def fetch_sales_orders():
#     """
#     Fetch sales orders from Odoo using XML-RPC.
#     """
#     try:
#         # Authenticate
#         common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
#         uid = common.authenticate(db, username, api_key, {})
#         if not uid:
#             return {"status": "error", "message": "Authentication failed"}
#
#         # Access model methods
#         models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
#
#         # Fetch sales orders
#         domain = []  # Add filters if needed, e.g., [['state', '=', 'sale']]
#         fields = ['name', 'date_order', 'amount_total', 'partner_id', 'state']
#
#         sales_orders = models.execute_kw(
#             db, uid, api_key,  # Use API Key in place of password
#             'sale.order',  # Model
#             'search_read',  # Method
#             [domain],  # Domain (filter conditions)
#             {'fields': fields, 'limit': 10}  # Additional options
#         )
#         return {"status": "success", "data": sales_orders}
#
#     except Exception as e:
#         return {"status": "error", "message": str(e)}
#
#
# def fetch_chart_of_accounts():
#     """
#     Fetch chart of accounts from Odoo using XML-RPC, and process the JSONB 'name' field.
#     """
#     try:
#         # Authenticate
#         common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
#         uid = common.authenticate(db, username, api_key, {})
#         if not uid:
#             return {"status": "error", "message": "Authentication failed"}
#
#         # Access model methods
#         models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
#
#         # Fetch chart of accounts
#         domain = []  # Add filters if needed
#         fields = ['id', 'code', 'account_type', 'internal_group', 'name']
#
#         accounts = models.execute_kw(
#             db, uid, api_key,  # Use API Key in place of password
#             'account.account',  # Model
#             'search_read',  # Method
#             [domain],  # Domain (filter conditions)
#             {'fields': fields, 'limit': 20}  # Additional options
#         )
#
#         # Process accounts to format the response
#         formatted_accounts = []
#         for account in accounts:
#             # Extract 'name' from JSONB-like structure (e.g., {"en_US": "Account Receivable"})
#             account_name = account['name'].get('en_US', "N/A") if isinstance(account['name'], dict) else account['name']
#
#             # Add the required fields to the formatted response
#             formatted_accounts.append({
#                 'id': account['id'],
#                 'code': account['code'],
#                 'account_type': account['account_type'],
#                 'internal_group': account.get('internal_group', "N/A"),
#                 'name': account_name
#             })
#
#         return {"status": "success", "data": formatted_accounts}
#
#     except Exception as e:
#         return {"status": "error", "message": str(e)}
#
#
# # API route for Sales Orders
# @app.route('/api/sales_orders', methods=['GET'])
# def get_sales_orders():
#     """
#     Public API to fetch sales orders.
#     """
#     result = fetch_sales_orders()
#     return jsonify(result)
#
#
# # API route for Chart of Accounts
# @app.route('/api/chart_of_accounts', methods=['GET'])
# def get_chart_of_accounts():
#     """
#     Public API to fetch the chart of accounts.
#     """
#     result = fetch_chart_of_accounts()
#     return jsonify(result)
#
#
# # Run the Flask app
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)

