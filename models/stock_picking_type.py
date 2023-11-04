# -*- coding: utf-8 -*- 

from odoo import models,fields,api,_
from odoo.exceptions import UserError


class StockPickingType(models.Model):
    _inherit = "stock.picking.type"

    note = fields.Html('Notes',help="This is a default notes that will be used when creating picking with this type")


