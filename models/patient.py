from odoo import models, fields

class patient(models.Model):
    _inherit = 'res.partner'

    isPatient = fields.Boolean(string="Is Patient")
    patient_type = fields.Selection([('inpatient', 'Inpatient'), ('outpatient', 'Outpatient'), ('reserve', 'Reserve')], string="Patient Type")

    doctor_id = fields.Many2one(comodel_name="res.users", string="Doctor", domain=[('isDoctor', '=', True)])

    hasGuarantor = fields.Boolean(string="Has Guarantor", default=False)
    guarantor_request_ids = fields.One2many(comodel_name="guarantor.request", inverse_name="patient_id", string="Guarantor Requests")
