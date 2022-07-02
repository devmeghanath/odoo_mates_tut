from odoo import fields,models,api;
from datetime import date;

class hospitalPatients(models.Model):
    _name='hospital.patients'
    _description='hospital patients info'
    _inherit=['mail.thread','mail.activity.mixin']

    name=fields.Char(string='Name',tracking=True)
    date_of_birth=fields.Date(string="DOB")
    ref=fields.Char(string='referance')
    age=fields.Integer(string='Age',compute='computed_age')
    gender=fields.Selection([('male','Male'),('female','Female')])
    active=fields.Boolean(string='Active',default=True)

    @api.depends('date_of_birth')
    def computed_age(self):

        for rec in self:
            today = date.today()

            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year

            else:
                rec.age=0;






