# -*- coding: utf-8 -*- 

from odoo import models,fields,api,_
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _inherit = "stock.picking"

    origin_delivery_ref = fields.Char(string='Origin delivery reference',states={'done': [('readonly', True)], 'cancel': [('readonly', True)]},)
    origin_delivery_date = fields.Date(string='Origin delivery date',states={'done': [('readonly', True)], 'cancel': [('readonly', True)]},)
