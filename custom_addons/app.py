from flask import Flask, jsonify, request
import xmlrpc.client
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch values from environment variables
url = os.getenv('ODOO_URL')  # Odoo URL
db = os.getenv('ODOO_DB')  # Database name
username = os.getenv('ODOO_USERNAME')  # Odoo login
api_key = os.getenv('ODOO_API_KEY')  # API key

# Flask app initialization
app = Flask(__name__)


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


# API route
@app.route('/api/sales_orders', methods=['GET'])
def get_sales_orders():
    """
    Public API to fetch sales orders.
    """
    result = fetch_sales_orders()
    return jsonify(result)


# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
