# -*- coding: utf-8 -*-

from odoo import models, fields, api

class claves_sat(models.Model):
    _name = 'inventario_expandido.clave_sat'
    _rec_name = 'clave'

    clave = fields.Char('Clave SAT')

class medidass_sat(models.Model):
    _name = 'inventario_expandido.medida_sat'
    _rec_name = 'medida'

    medida = fields.Char('Unidad medida SAT')

class inventario_expandido(models.Model):
    _inherit = 'product.template'

    ubicacion = fields.Char('Ubicación', size=16)
    pedimento = fields.Char('Pedimento')
    clave_sat = fields.Many2one('inventario_expandido.clave_sat', string ='Clave SAT')
    unidad_sat = fields.Many2one('inventario_expandido.medida_sat', string = 'Unidad Medida SAT')

class orden_entrega_expandido(models.Model):
    _inherit = 'stock.picking'

    empleado = fields.Many2one('hr.employee', string = 'Surtido por')