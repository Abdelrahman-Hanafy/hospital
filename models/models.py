# -*- coding: utf-8 -*-

from odoo import models, fields, api

class patient(models.Model):
    _inherit = 'res.partner'

    isPatient = fields.Boolean(string="Is Patient")
    patient_type = fields.Selection([('inpatient', 'Inpatient'), ('outpatient', 'Outpatient'), ('reserve', 'Reserve')], string="Patient Type")

class guarantorRequest(models.Model):
    _name = 'guarantor.request'
    _description = 'Guarantor Request'

    name = fields.Char(string="Name", default="New", readonly=True)
    patient_id = fields.Many2one(comodel_name="res.partner", string="Patient", domain=[('isPatient', '=', True)])
    what_to_do = fields.Text(string="What to do?")
    date = fields.Date(string="Date", default=fields.Date.today())
    state = fields.Selection([('draft', 'Draft'), ('sent', 'Sent') ,('accepted', 'Accepted'), ('rejected', 'Rejected')], string="State", default="draft")

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('guarantor.request') or 'New'
        result = super(guarantorRequest, self).create(vals)
        return result