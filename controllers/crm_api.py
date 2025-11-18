from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)

class CrmAPI(http.Controller):

    @http.route('/api/crm/create_lead', type='json', auth='public', methods=['POST'], csrf=False)
    def create_lead(self, **kwargs):
        try:
            data = request.jsonrequest
            
            required_fields = ['name', 'email', 'phone']
            missing_fields = [field for field in required_fields if field not in data or not data[field]]
            
            if missing_fields:
                return {
                    'success': False,
                    'error': f'الحقول التالية مطلوبة: {", ".join(missing_fields)}'
                }
            
            if data['email'] and '@' not in data['email']:
                return {
                    'success': False,
                    'error': 'البريد الإلكتروني غير صالح'
                }
            
            lead_vals = {
                'name': data['name'],
                'email_from': data['email'],
                'phone': data['phone'],
            }
            
            lead = request.env['crm.lead'].sudo().create(lead_vals)
            
            return {
                'success': True,
                'message': 'تم إنشاء الليد بنجاح',
                'lead_id': lead.id,
                'lead_name': lead.name
            }
            
        except Exception as e:
            _logger.error(f"Error creating lead: {str(e)}")
            return {
                'success': False,
                'error': f'حدث خطأ أثناء إنشاء الليد: {str(e)}'
            }
