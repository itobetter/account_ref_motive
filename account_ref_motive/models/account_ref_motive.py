from openerp.osv import osv, fields

class account_ref_motive_voucher(osv.Model):
	_inherit = 'account.voucher'

	_columns ={
		'reference': fields.many2one('account.voucher.motive', 'Ref. pago', help='Motivo del pago'),
	}

class account_ref_motive(osv.Model):
	_name = 'account.voucher.motive'

	def name_search(self, cursor, uid, name, args=None, operator='ilike', context=None, limit=80):
		if args is None: args = []
		if not context: context = {}
		search_params = [] + args
		if name:
			search_params_parent = [('name', operator, name), ('motive_id', '=', False)]
			parent_id = self.search(cursor, uid, search_params_parent, limit=limit, context=context)
			if parent_id: search_params += ['|', ('motive_id', '=', parent_id), ('name', operator, name)]
			else: search_params += [('name', operator, name)]
		ids = self.search(cursor, uid, search_params, limit=limit, context=context)

		return self.name_get(cursor, uid, ids, context=context)


	def name_get(self, cursor, uid, ids, context=None):
		if not context: context = {}
		if not ids:
			return []
		res = []
		res = [(record.id, record.motive_id.name+'/'+record.name if record.motive_id else  record.name) for record in self.browse(cursor, uid, ids, context=context)]
		return res


	_inherit = ['mail.thread']
	_get_type=[('receipt', 'Cliente'),('payment', 'Proveedor'), ('in_out', 'Cliente/Proveedor')]
	_columns = {

		'name': fields.char('Nombre', size=60, help='Nombre dela flujo de la caja', required=True),
		'motive_id': fields.many2one('account.voucher.motive', 'Padre', help=''),
		'code': fields.char('Codigo', size=60, help='Codigo flujo'),
		'type': fields.selection(_get_type, 'Tipo', help='Determina si es para pao de Proveedores o Clientes', required=True),
		'description': fields.text('Descripcion', help='Breve descripcion del motivo'),
	}
