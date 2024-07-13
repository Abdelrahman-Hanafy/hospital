from odoo import models, fields, api

class doctor(models.Model):
    _inherit = 'res.users'

    isDoctor = fields.Boolean(string="Is Doctor")
    type = fields.Selection([('duty', 'Duty'), ('admission', 'Admission'), ('ER', 'Emergency'), ('consultation', 'Consultation')], string="Type")

    create_employee_id = fields.Many2one(comodel_name="hr.employee", string="Employee", store=True)
    employee_department_id = fields.Many2one(related="create_employee_id.department_id", string="Department", readonly=False, store=True)

    visit_ids = fields.One2many(comodel_name="hospital.patient.visit", inverse_name="doctor_id", string="Visits")


    @api.model
    def create(self, vals):
        result = super(doctor, self).create(vals)
        result.action_create_employee()
        result.create_employee_id = self.env['hr.employee'].search([('user_id', '=', result.id)])

        return result