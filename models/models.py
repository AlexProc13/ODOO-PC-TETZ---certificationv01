# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
 
from openerp import models, fields, api, tools, _
# from openerp.osv import fields as fields_old
# import openerp.addons.decimal_precision as dp



class Status(models.Model):
    _name = 'status'
    _rec_name='status'
    _description = 'status'
    status = fields.Char()
    
 
class TypeOfCertificate(models.Model):
    _name = 'type_of_certificate'
    _rec_name='type_of_certificate'
    _description = 'type_of_certificate'
    type_of_certificate = fields.Char()
	

class Registr(models.Model):
    _name = 'registr'
    _rec_name='number'
    _description = 'registr'
    _inherit = 'ir.needaction_mixin'

    number = fields.Char( required=True,)
    description = fields.Text()
    country_id = fields.Many2one('res.country', string='Country',)
    status_id = fields.Many2one('status', string='Status',)
    end_data = fields.Date()
    start_data = fields.Date()
    expire = fields.Boolean('Expire', help="Expire", default=True)
    type_certification_id = fields.Many2one('type_of_certificate', string='Type of certificate',)
    registr_id = fields.Many2one('res.partner', string='Organ', required=True,)
    put_in = fields.Char()
    float = fields.Float()
    production_id = fields.Many2one('product.template', string='Production',)

  
class MyCustomPartner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"

# Add new field
    organ = fields.Boolean("Organ", default=False)
    
