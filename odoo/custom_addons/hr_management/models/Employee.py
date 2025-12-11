
from datetime import date
from attrs import fields
from odoo import models
class Employee(models.Model):
    _name = 'hr.employee'
    _description = 'Employee Management'

    name = fields.Char(string='Employee Name', required=True)
    position = fields.Selection([
        ('manager', 'Manager'),
        ('developer', 'Developer'),
        ('hr', 'HR'),
    ], string='Position', required=True)
    salary = fields.Float(string='Salary', default=1000.0)
    start_date = fields.Date(string='Start Date', default=date.today)