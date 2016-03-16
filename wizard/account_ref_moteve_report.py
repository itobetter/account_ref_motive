from openerp.osv import orm, fields
import time

class account_ref_motive_report(orm.TransientModel):
	_name = 'account.ref.motive.report'
	_description = 'wizard para la configuraciones del reporte'
	_get_type=[('receipt', 'Cliente'),('payment', 'Proveedor'), ('in_out', 'Cliente/Proveedor')]
	_columns = {
		'date_from': fields.date('Desde', help='Fecha de comienzo para el reporte', required=True),
		'date_to': fields.date('Hasta', help='Fecha de finalizacion para el reporte', required=True),
		'type': fields.selection(_get_type, 'Tipo', help='Determina si es para pao de Proveedores o Clientes'),
		'partner_id': fields.many2one('res.partner', 'Empresa'),

	}
	_defaults= {
        'date_from': lambda *a: time.strftime('%Y-%m-01'),
        'date_to': lambda *a: time.strftime('%Y-%m-%d'),
    }

	def check_report(self, cr, uid, ids, context=None):
		if context is None:
			context = {}
		data = self.read(cr, uid, ids)[0]
		datas = {
             'ids': context.get('active_ids',[]),
             'model': 'account.voucher',
             'form': data
                 }
		return {
            'type': 'ir.actions.report.xml',
            'report_name': 'account.ref.voucher.print',
            'datas': datas,
            }