# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StudentEnrollment(models.Model):
    _name = 'student.enrollment'
    _description = 'Student Enrollment'
    _rec_name = 'display_name'

    display_name = fields.Char(
        compute='_compute_display_name',
        store=True
    )


    first_name = fields.Char("First Name", required=True)
    middle_name = fields.Char("Middle Name", required=True)
    last_name = fields.Char("Last Name", required=True)
    email = fields.Char("Email")
    phone = fields.Char("Phone")
    course = fields.Selection([
        ('python', 'Python'),
        ('odoo', 'Odoo'),
        ('java', 'Java'),
    ], string="Course")

    display_name = fields.Char(
        compute='_compute_display_name',
        store=True
    )
    
    @api.depends('first_name', 'middle_name', 'last_name', 'course')
    def _compute_display_name(self):
        for rec in self:
            name = " ".join(
            filter(None, [rec.first_name, rec.middle_name, rec.last_name])
        )

        if rec.course:
            course_label = dict(self._fields['course'].selection).get(rec.course)
            rec.display_name = f"{name} ({course_label})"  
        else:
            rec.display_name = name

    # @api.depends('first_name', 'middle_name', 'last_name')
    # def _compute_display_name(self):
    #     for rec in self:
    #         name_parts = filter(None, [
    #             rec.first_name,
    #             rec.middle_name,
    #             rec.last_name
    #         ])
    #         rec.display_name = " ".join(name_parts)

    def action_confirm(self):
        """Confirm the student enrollment."""
        for rec in self:
            rec.status = 'confirmed'
        return True

    def action_view_students(self):
        """Smart button: open all Students (res.partner)."""
        return {
            'type': 'ir.actions.act_window',
            'name': 'All Students',
            'res_model': 'res.partner',
            'view_mode': 'tree,form',
            'target': 'current',
            'domain': [('is_company', '=', False)],
        }

