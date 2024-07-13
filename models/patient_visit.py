from odoo import models, fields, api


class PatientVisit(models.Model):
    _name = 'hospital.patient.visit'
    _description = 'Patient Visit'

    name = fields.Char(string='Name', default="New", readonly=True)
    start_time = fields.Datetime(string='Start Time', required=True)
    end_time = fields.Datetime(string='End Time')
    patient_id = fields.Many2one('res.partner', string='Patient', domain=[('isPatient', '=', True)])

    department_id = fields.Many2one("hr.department", string="Department")
    doctor_id = fields.Many2one('res.users', string='Doctor', domain= [('isDoctor', '=', True)])
    
    visit_type = fields.Selection([('inpatient', 'Inpatient'), ('outpatient', 'Outpatient'), ('reserve', 'Reserve')], string="Patient Type")

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('patient.visit') or 'New'
        result = super(PatientVisit, self).create(vals)
        return result