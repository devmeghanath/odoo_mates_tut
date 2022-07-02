# -*- coding: utf-8 -*-
# from odoo import http


# class OmNewMod(http.Controller):
#     @http.route('/om_new_mod/om_new_mod', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_new_mod/om_new_mod/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_new_mod.listing', {
#             'root': '/om_new_mod/om_new_mod',
#             'objects': http.request.env['om_new_mod.om_new_mod'].search([]),
#         })

#     @http.route('/om_new_mod/om_new_mod/objects/<model("om_new_mod.om_new_mod"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_new_mod.object', {
#             'object': obj
#         })
