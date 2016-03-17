from openerp.osv import orm, fields
import time

class account_ref_motive_report(orm.TransientModel):
	_name = 'account.ref.motive.report'
	_description = 'wizard para la configuraciones del reporte'
	_get_type=[('receipt', 'Cliente'),('payment', 'Proveedor'), ('in_out', 'Cliente/Proveedor')]
	_columns = {
		'date_from': fields.date('Desde', help='Fecha de comienzo para el reporte', required=True),
		'date_to': fields.date('Hasta', help='Fecha de finalizacion para el reporte', required=True),
		'type':fields.selection([
            ('sale','Ventas'),
            ('purchase','Compras'),
            ('payment','Pagos'),
            ('receipt','Recepciones')]),
		'partner_id': fields.many2one('res.partner', 'Empresa'),

	}
	_defaults= {
        'date_from': lambda *a: time.strftime('%Y-%m-%d'),
        'date_to': lambda *a: time.strftime('%Y-%m-%d'),
    }

	def _get_model(self, cr, uid, ids):
		if not hasattr(ids, '__iter__'): ids = [ids]
		select = [wizard.type for wizard in self.browse(cr, uid, ids)]
		if 'purchase' or 'payment' in select : return 'report.account.ref.voucher.print.in'
		if 'sale' or 'receipt' not in select: return 'report.account.ref.voucher.print.out'



	def check_report(self, cr, uid, ids, context=None):
		if context is None:
			context = {}
		data = self.read(cr, uid, ids)[0]
		data['partner_id'] = data['partner_id'][0]
		datas = {
             'ids': context.get('active_ids',[]),
             'model': 'account.voucher',
             'form': data
                 }
		return {
            'type': 'ir.actions.report.xml',
            'report_name': self._get_model(cr, uid, ids),
            'datas': datas,
            }
