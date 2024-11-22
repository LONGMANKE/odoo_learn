# -*- coding: utf-8 -*-
{
    'name': "Odoo Phone for Kenya, Uganda, Nigeria, Tanzania, South Africa, Ghana, Mexico, United States, Australia - Helloduty",

    'summary': """
        Make and receive calls and SMS, sync contacts, 
        capture conversation history and recordings right from your Odoo Platform. 
        Optimized for Kenya, Uganda, Nigeria, Tanzania, South Africa, Ghana, Mexico, US, and Australia.
    """,

    'description': """
<h2>Odoo Phone by Helloduty - Integrated Communication Suite for Multiple Countries</h2>

<h3>Overview:</h3>
<p>Odoo Phone by Helloduty is a powerful communication integration for Odoo, tailored for businesses operating in Kenya, Uganda, Nigeria, Tanzania, South Africa, Ghana, Mexico, the United States, and Australia. This solution streamlines your business communications directly within your Odoo platform, bringing advanced telephony features to your fingertips. Compatible with both Odoo 17 Enterprise Edition (EE) and Community Edition (CE).</p>

<h3>Key Features:</h3>
<ul>
    <li><strong>International Calling:</strong> Make and receive calls seamlessly across Kenya, Uganda, Nigeria, Tanzania, South Africa, Ghana, Mexico, the US, and Australia.</li>
    <li><strong>SMS Integration:</strong> Send and receive text messages directly from your Odoo interface, with support for local number formats.</li>
    <li><strong>Contact Synchronization:</strong> Keep your Odoo contacts up-to-date with automatic syncing, including international number formats.</li>
    <li><strong>Conversation History:</strong> Capture and store detailed call and message logs for future reference, essential for international business communications.</li>
    <li><strong>Call Recordings:</strong> Record important calls and access them easily within Odoo, compliant with local regulations.</li>
</ul>

<h3>Benefits:</h3>
<ul>
    <li><strong>Enhanced Global Productivity:</strong> Manage all your communications from a single platform, regardless of geographical location.</li>
    <li><strong>Improved International Customer Service:</strong> Access customer information instantly during calls, with support for multiple time zones and languages.</li>
    <li><strong>Streamlined Cross-Border Workflows:</strong> Reduce time spent switching between different communication tools and adapting to various international systems.</li>
    <li><strong>Comprehensive International Record Keeping:</strong> Maintain detailed logs of all customer interactions across different countries.</li>
</ul>

<h3>Technical Details:</h3>
<ul>
    <li><strong>Version:</strong> 1.0</li>
    <li><strong>Category:</strong> Productivity</li>
    <li><strong>License:</strong> OPL-1</li>
    <li><strong>Compatibility:</strong> Odoo 17 EE and CE</li>
    <li><strong>Installation:</strong> Easy to install and configure, with options for local number integration</li>
</ul>

<p>Boost your team's global productivity and take your international customer communications to the next level with Odoo Phone by Helloduty!</p>
    """,

    'author': "Helloduty",
    'website': "https://www.helloduty.com/",

    'category': 'Productivity',
    'version': '1.0',
    'license': 'OPL-1',
    'application': True,
    'installable': True,
    'auto_install': False,

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],
    'data': [
           'views/settings.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'helloduty/static/src/js/app.js'
        ],
    },
     'images': [
        'static/description/screenshot.gif',
    ],
}