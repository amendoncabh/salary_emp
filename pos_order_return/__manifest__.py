# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
{
    "name": "POS Order Return",
    "summary": "This module is use to Return orders in running point of sale session.",
    "category": "Point Of Sale",
    "version": "3.4.4",
    "sequence": 1,
    "author": "Webkul Software Pvt. Ltd.",
    "license": "Other proprietary",
    "website": "https://store.webkul.com/Odoo-POS-Order-Return.html",
    "description": """http://webkul.com/blog/pos-order-return/""",
    "live_test_url": "http://odoodemo.webkul.com/?module=pos_order_return&version=10.0&custom_url=/pos/web",
    "depends": [
        'pos_customize',
        'pos_orders_return_product',
        'tr_core_update',
    ],
    "data": [
        'views/pos_order_return_view.xml',
        'views/template.xml',
    ],
    "qweb": ['static/src/xml/pos_order_return.xml'],
    "images": ['static/description/Banner.png'],
    "application": True,
    "installable": True,
    "auto_install": False,
    "price": 22,
    "currency": "EUR",
    "pre_init_hook": "pre_init_check",
}
#################################################################################
