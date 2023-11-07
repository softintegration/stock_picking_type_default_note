# -*- coding: utf-8 -*- 

from odoo import models,fields,api,_
from odoo.exceptions import UserError


class Picking(models.Model):
    _inherit = "stock.picking"

    @api.onchange('picking_type_id', 'partner_id')
    def _onchange_picking_type(self):
        res = super(Picking,self)._onchange_picking_type()
        if self.picking_type_id:
            self.update({
                'note':self.picking_type_id.note
            })
        return res

    @api.model
    def create(self, vals):
        recs = super(Picking,self).create(vals)
        for rec in recs:
            # because the backorder picking will inherit automatically the parent picking note ,we have considered this case as exception to the rule
            if not rec.note or rec.backorder_id:
                rec.note = rec.picking_type_id.note
        return recs

