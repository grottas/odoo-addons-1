# -*- coding: utf-8 -*-
#/#############################################################################
#
#   Odoo, Open Source Management Solution
#   Copyright (C) 2015 NuoBiT Solutions, S.L. (<http://www.nuobit.com>).
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#/#############################################################################

from openerp import api, models, fields, SUPERUSER_ID
from openerp.api import Environment



import logging

_logger = logging.getLogger(__name__)

class ProductProduct(models.Model):
    _inherit = 'product.product'

    wk_make_to_order = fields.Boolean('Make to order')


class Website(models.Model):
    _inherit = 'website'

    @api.model
    def get_in_of_stock_message_template(self, product_obj=False, product_qty=0.0, config_vals={}):
        values = super(Website, self).get_in_of_stock_message_template(product_obj=product_obj,
                                                                        product_qty=product_qty, config_vals=config_vals)
        if product_obj and product_obj.type != 'service':
            product_var_object = product_obj.product_variant_ids[0]
            if product_var_object.wk_make_to_order:
                values = [False, config_vals.get('wk_in_stock_msg')]

        return values

    @api.model
    def get_in_of_stock_message(self, product_obj=False, product_qty=0.00, config_vals={}):
        values = super(Website, self).get_in_of_stock_message(product_obj=product_obj,
                                                                       product_qty=product_qty, config_vals=config_vals)
        if product_obj and product_obj.type != 'service':
            if product_obj.wk_make_to_order:
                values = [False, config_vals.get('wk_in_stock_msg')]

        return values