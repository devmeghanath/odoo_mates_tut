from odoo import fields,models,api;


class hospitalPatients(models.Model):
    _name='hospital.appoinment'
    _description='hospital patients info'
    _inherit=['mail.thread','mail.activity.mixin']


    patient_id=fields.Many2one('hospital.patients',string="patients")
    gender=fields.Selection(related='patient_id.gender' )
    Appoinment_Time=fields.Datetime(string="Appoinment Time",default=fields.Datetime.now)
    Booking_Date=fields.Date(string="Booking Date",default=fields.Date.context_today)
    ref=fields.Char(string="reference")



    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref=self.patient_id.ref


