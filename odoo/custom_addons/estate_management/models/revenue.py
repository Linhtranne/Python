# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class Revenue(models.Model):
    _name = 'estate.revenue'
    _description = 'Revenue Management'
    _rec_name = 'description'
    _order = 'date desc'

    date = fields.Date(string='Date', required=True, default=fields.Date.today, help='Revenue date')
    amount = fields.Float(string='Amount', required=True, help='Revenue amount')
    description = fields.Text(string='Description', required=True, help='Revenue description')
    
    category = fields.Selection([
        ('sale', 'Property Sale'),
        ('rent', 'Rental Income'),
        ('service', 'Service Fee'),
        ('other', 'Other'),
    ], string='Category', default='sale', help='Revenue category')
    
    def calculate_total_revenue_by_date(self, start_date=None, end_date=None):
        """
        Calculate total revenue within a date range
        
        Args:
            start_date: Start date for calculation (string format 'YYYY-MM-DD' or date object)
            end_date: End date for calculation (string format 'YYYY-MM-DD' or date object)
            
        Returns:
            dict: Dictionary with total revenue and revenue details
        """
        domain = []
        
        if start_date:
            domain.append(('date', '>=', start_date))
        if end_date:
            domain.append(('date', '<=', end_date))
        
        revenues = self.search(domain)
        total = sum(revenues.mapped('amount'))
        
        return {
            'total_revenue': total,
            'record_count': len(revenues),
            'start_date': start_date,
            'end_date': end_date,
            'revenue_details': revenues,
        }
    
    @api.model
    def total_revenue_by_month(self, month, year):
        """
        Calculate total revenue for a specific month
        
        Args:
            month: Month number (1-12)
            year: Year (e.g., 2025)
            
        Returns:
            float: Total revenue for the month
        """
        from datetime import date
        from calendar import monthrange
        
        # Get first and last day of the month
        first_day = date(year, month, 1)
        last_day_num = monthrange(year, month)[1]
        last_day = date(year, month, last_day_num)
        
        result = self.calculate_total_revenue_by_date(
            start_date=first_day.strftime('%Y-%m-%d'),
            end_date=last_day.strftime('%Y-%m-%d')
        )
        
        return result['total_revenue']
    
    @api.model
    def get_revenue_summary(self):
        """
        Get revenue summary statistics
        
        Returns:
            dict: Dictionary with various revenue statistics
        """
        all_revenues = self.search([])
        today = fields.Date.today()
        
        # Today's revenue
        today_revenues = self.search([('date', '=', today)])
        today_total = sum(today_revenues.mapped('amount'))
        
        # This month's revenue
        first_day_month = today.replace(day=1)
        month_revenues = self.search([('date', '>=', first_day_month), ('date', '<=', today)])
        month_total = sum(month_revenues.mapped('amount'))
        
        # Total revenue
        total_revenue = sum(all_revenues.mapped('amount'))
        
        return {
            'today_revenue': today_total,
            'month_revenue': month_total,
            'total_revenue': total_revenue,
            'total_records': len(all_revenues),
        }
