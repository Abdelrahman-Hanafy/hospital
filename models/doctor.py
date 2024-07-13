from odoo import models, fields, api

class doctor(models.Model):
    _inherit = 'res.users'

    isDoctor = fields.Boolean(string="Is Doctor")
    type = fields.Selection([('duty', 'Duty'), ('admission', 'Admission'), ('ER', 'Emergency'), ('consultation', 'Consultation')], string="Type")

    create_employee_id = fields.Many2one(related="employee_id", string="Employee", store=True)
    employee_department_id = fields.Many2one(related="create_employee_id.department_id", string="Department", readonly=False)

    @api.model
    def create(self, vals):
        result = super(doctor, self).create(vals)
        self.create_employee_id = self.env['hr.employee'].search([('user_id', '=', result.id)])