from odoo import fields, models, api
from odoo.exceptions import UserError
from datetime import date
import base64
import io
import xlsxwriter

class CrmLeadReportWizard(models.TransientModel):
    _name = 'crm.lead.report.wizard'
    _description = 'CRM Lead Report Wizard'

    date_from = fields.Date(string='Date From', required=True, default=date.today())
    date_to = fields.Date(string='Date To', required=True, default=date.today())

    def _get_filtered_leads(self):
        if self.date_from and self.date_to and self.date_from > self.date_to:
            raise UserError("Date From cannot be greater than Date To.")
        domain = [
            ('next_activity_date', '>=', self.date_from),
            ('next_activity_date', '<=', self.date_to),
        ]
        return self.env['crm.lead'].search(domain)

    def action_print_pdf(self):
        leads = self._get_filtered_leads()
        if not leads:
            raise UserError("No leads found for the selected date range.")
        data = {
            'ids': leads.ids,
            'model': 'crm.lead',
            'form': {
                'date_from': self.date_from,
                'date_to': self.date_to,
                'lead_ids': leads.ids,
            },
        }
        return self.env.ref('odoo_crm_custom.action_report_crm_lead_pdf').report_action(self, data=data)

    def action_print_excel(self):
        leads = self._get_filtered_leads()
        if not leads:
            raise UserError("No leads found for the selected date range.")
        
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet('CRM Leads Report')
        
        header_format = workbook.add_format({
            'bold': True,
            'fg_color': '#366092',
            'font_color': 'white',
            'border': 1,
            'align': 'center',
            'valign': 'vcenter'
        })
        
        date_format = workbook.add_format({'num_format': 'yyyy-mm-dd', 'border': 1})
        text_format = workbook.add_format({'border': 1})
        
        headers = [
            'Lead Name', 
            'Next Activity Date', 
            'Stage', 
            'Priority', 
            'Salesperson',
            'Company',
            'Email',
            'Phone',
            'Create Date'
        ]
        
        for col, header in enumerate(headers):
            worksheet.write(0, col, header, header_format)
        
        row = 1
        for lead in leads:
            worksheet.write(row, 0, lead.name or '', text_format)
            worksheet.write(row, 1, lead.next_activity_date or '', date_format)
            worksheet.write(row, 2, lead.stage_id.name or '', text_format)
            worksheet.write(row, 3, lead.priority or '', text_format)
            worksheet.write(row, 4, lead.user_id.name or '', text_format)
            worksheet.write(row, 5, lead.partner_name or '', text_format)
            worksheet.write(row, 6, lead.email_from or '', text_format)
            worksheet.write(row, 7, lead.phone or '', text_format)
            worksheet.write(row, 8, lead.create_date.strftime('%Y-%m-%d') if lead.create_date else '', date_format)
            row += 1
        
        worksheet.set_column('A:A', 30)
        worksheet.set_column('B:B', 18)
        worksheet.set_column('C:C', 20)
        worksheet.set_column('D:D', 12)
        worksheet.set_column('E:E', 20)
        worksheet.set_column('F:F', 25)
        worksheet.set_column('G:G', 25)
        worksheet.set_column('H:H', 15)
        worksheet.set_column('I:I', 15)
        
        title_format = workbook.add_format({
            'bold': True,
            'font_size': 16,
            'align': 'center'
        })
        
        worksheet.merge_range('A1:I1', f'CRM Leads Report - {self.date_from} to {self.date_to}', title_format)
        
        stats_format = workbook.add_format({'bold': True, 'italic': True})
        worksheet.write(row + 2, 0, f'Total Leads: {len(leads)}', stats_format)
        
        workbook.close()
        
        excel_file = base64.b64encode(output.getvalue())
        output.close()
        
        attachment = self.env['ir.attachment'].create({
            'name': f'crm_leads_report_{self.date_from}_to_{self.date_to}.xlsx',
            'datas': excel_file,
            'type': 'binary',
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        })
        
        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{attachment.id}?download=true',
            'target': 'self',
        }