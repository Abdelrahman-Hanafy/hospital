from odoo import models, fields, api

class doctor(models.Model):
    _inherit = 'res.users'

    isDoctor = fields.Boolean(string="Is Doctor")
    type = fields.Selection([('duty', 'Duty'), ('admission', 'Admission'), ('ER', 'Emergency'), ('consultation', 'Consultation')], string="Type")

    create_employee_id = fields.Many2one(comodel_name="hr.employee", string="Employee", store=True)
    employee_department_id = fields.Many2one(related="create_employee_id.department_id", string="Department", readonly=False, store=True)

    visit_ids = fields.One2many(comodel_name="hospital.patient.visit", inverse_name="doctor_id", string="Visits")

    availability_ids = fields.One2many(comodel_name="doctor.availability", inverse_name="doctor_id", string="Availability")

    @api.model
    def create(self, vals):
        result = super(doctor, self).create(vals)
        result.action_create_employee()
        result.create_employee_id = self.env['hr.employee'].search([('user_id', '=', result.id)])

        return result
    
class doctorAvailability(models.Model):
    _name = 'doctor.availability'

    name = fields.Char(string="Name", compute="_compute_name", store=True)
    doctor_id = fields.Many2one(comodel_name="res.users", string="Doctor")
    weekday = fields.Selection([('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday'), ('sun', 'Sunday')], string="Day")
    start_time = fields.Float(string="Start Time")
    end_time = fields.Float(string="End Time")
    duration = fields.Float(string="Duration", compute="_compute_duration", inverse="_inverse_duration" ,store=True)

    @api.depends('start_time', 'end_time')
    def _compute_duration(self):
        for rec in self:
            rec.duration = rec.end_time - rec.start_time

    def _inverse_duration(self):
        for rec in self:
            rec.end_time = rec.start_time + rec.duration

    @api.depends('doctor_id', 'weekday')
    def _compute_name(self):
        for rec in self:
            rec.name = f"{rec.doctor_id.name} - {rec.weekday}"