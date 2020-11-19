# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Productos(models.Model):
    _inherit = 'product.template'

    codigo_man = fields.Char(
        string='Código Filtro MANN',
        required=False)
    marca_filtro_id = fields.Many2one(
        comodel_name='marcas.filtros',
        string='Marca',
        required=False)


class MarcasFiltros(models.Model):
    _name = 'marcas.filtros'

    name = fields.Char(string="Nombre de la marca")


