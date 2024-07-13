from odoo import models, fields

class patient(models.Model):
    _inherit = 'res.partner'

    isPatient = fields.Boolean(string="Is Patient")

    visit_ids = fields.One2many(comodel_name="hospital.patient.visit", inverse_name="patient_id", string="Visits")

    hasGuarantor = fields.Boolean(string="Has Guarantor", default=False)
    guarantor_id = fields.Many2one(comodel_name="res.partner", string="Guarantor", domain=[('is_company', '=', True)])
    guarantor_request_ids = fields.One2many(comodel_name="guarantor.request", inverse_name="patient_id", string="Guarantor Requests")
