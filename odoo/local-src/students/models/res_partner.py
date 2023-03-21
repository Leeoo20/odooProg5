from odoo import fields, models

class ResPartner(models.Model) :
    _inherit="res.partner"

    student_continuous_ids = fields.One2many(
        string="student partner",
        comodel_name="students.student",
        inverse_name="nationalite_id",
    )