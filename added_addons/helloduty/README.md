Here are the instructions on how to install an Odoo Module using Git:
*Connect to the Server via SSH:*
- Access your remote server using SSH. If you're unfamiliar with SSH, follow a guide to connect to your VPS.
*Navigate to the Addons Directory:*
- Use SSH to navigate to your Odoo addons directory. For example, if you're using Odoo13, use the command: cd /opt/odoo/odoo13-custom-addons
*Clone the Git Repository:*
- Clone the module from GitHub into your addons folder using the following command: git clone https://gitlab.com/hello_duty/published/odoo.git
*Restart the Odoo Service:*
- Restart the Odoo service for the changes to take effect. Use the command: sudo systemctl restart odoo13.service
*Update the Addons List:*
- Activate developer mode in your Odoo installation. Go to settings, then under "Developer Tools," click on "Activate the developer mode (with assets)."
- Navigate to the Apps page on the main menu. Click on "Update Apps List" from the top menu.
*Install the Module:*
- After updating the Apps list, search for the module and click on the install button to install it.
Congratulations! You have successfully installed a module from GitHub into your Odoo installation.