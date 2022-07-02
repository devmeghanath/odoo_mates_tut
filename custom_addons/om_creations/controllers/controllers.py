# -*- coding: utf-8 -*-
# from odoo import http


# class OmCreations(http.Controller):
#     @http.route('/om_creations/om_creations', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_creations/om_creations/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_creations.listing', {
#             'root': '/om_creations/om_creations',
#             'objects': http.request.env['om_creations.om_creations'].search([]),
#         })

#     @http.route('/om_creations/om_creations/objects/<model("om_creations.om_creations"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_creations.object', {
#             'object': obj
#         })
