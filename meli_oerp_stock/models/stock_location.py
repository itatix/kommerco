# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import fields, osv, models, api
from odoo.tools.translate import _
import logging
_logger = logging.getLogger(__name__)

import pdb

#from .meli_oerp_config import *
#from .warning import warning

import requests
#from ..melisdk.meli import Meli

class stock_location(models.Model):
    
    _inherit = "stock.location"
    
    mercadolibre_active = fields.Boolean(string="Ubicacion activa para MercadoLibre",index=True)
    mercadolibre_logistic_type = fields.Char(string="Logistic Type Asociado",index=True)
    
class DeliveryCarrier(models.Model):
    
    _inherit = "delivery.carrier"
    
    ml_tracking_url = fields.Char(string="Default tracking url")
    
    def get_tracking_link(self, picking):
        if self.ml_tracking_url and picking and picking.carrier_tracking_ref:
            return self.ml_tracking_url+str(picking.carrier_tracking_ref)
            
        return super(DeliveryCarrier, self).get_tracking_link(picking)
    
