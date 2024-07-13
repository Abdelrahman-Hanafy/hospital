from odoo import models, fields, api, Command


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
    invoice_id = fields.Many2one(comodel_name='account.move', string="Invoice")

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('patient.visit') or 'New'
        result = super(PatientVisit, self).create(vals)
        return result
    
    ### Actions ###
    def action_create_invoice(self):
        res = self.env['account.move'].create({
            "move_type": "out_invoice",
            'partner_id': self.patient_id.id,
            'invoice_date': fields.Date.today(),
            'invoice_line_ids': [
                Command.create(
                    {"product_id": 1, "quantity": 1, "price_unit": 115}
                )
            ]

        })
        self.invoice_id = res.id


    def action_view_invoice(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "res_model": "account.move",
            "view_mode": "form",
            "res_id": self.invoice_id.id,
        }