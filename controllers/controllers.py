# -*- coding: utf-8 -*-
from odoo import http

# class MethodEquivalenciaFiltroMan(http.Controller):
#     @http.route('/method_equivalencia_filtro_man/method_equivalencia_filtro_man/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_equivalencia_filtro_man/method_equivalencia_filtro_man/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_equivalencia_filtro_man.listing', {
#             'root': '/method_equivalencia_filtro_man/method_equivalencia_filtro_man',
#             'objects': http.request.env['method_equivalencia_filtro_man.method_equivalencia_filtro_man'].search([]),
#         })

#     @http.route('/method_equivalencia_filtro_man/method_equivalencia_filtro_man/objects/<model("method_equivalencia_filtro_man.method_equivalencia_filtro_man"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_equivalencia_filtro_man.object', {
#             'object': obj
#         })