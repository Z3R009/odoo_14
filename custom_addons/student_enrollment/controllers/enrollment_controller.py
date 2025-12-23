# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class EnrollmentController(http.Controller):

    @http.route('/enroll/submit', type='http', auth="public", website=True)
    def enroll_submit(self, **post):
        request.env['student.enrollment'].sudo().create(post)
        return request.render('student_enrollment.enroll_thank_you')
