# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#	 Change: rsosa, 21/07/2015  Funcion para que el combo retorne correctamente los motivos en una relacion many2one
#
#
##############################################################################

from osv import osv
from osv import fields

class correccion_stock_motivos(osv.osv):
    _name = "correccion.stock.motivos"
    _description = "Registro de motivos validos para realizar correccion de stock"

    #rsosa Cambio 21/07/2015 Funcion para que el combo retorne correctamente los motivos en una relacion many2one
    # def name_get(self, cr, uid, ids, context={}):
    #     res = []
    #     if not len(ids):
    #         return res
    #
    #     for emp in self.browse(cr, uid, ids,context=context):
    #         res.append((emp.id,emp.motivo)) #emp.codigo,
    #         return res
    #randarad:modificacion para observar el codigo y la cuenta en los campos.
    def name_get(self, cr, uid, ids, context=None):
        if isinstance(ids, (int, long)):
            ids = [ids]
        if not ids:
            return []
        if isinstance(ids, (int, long)):
            ids = [ids]
        reads = self.read(cr, uid, ids, ['motivo','codigo'], context, load='_classic_write')
        return [(x['id'], (x['codigo'] and (x['codigo'] + ' - ') or '') + x['motivo']) \
                for x in reads]

    def name_search(self, cr, uid, name, args=None, operator='ilike', context=None, limit=80):
        """
        Funcion para busqueda por codigo y nombre de los motivos.
        """
        if args is None:
            args = []
        if context is None:
            context = {}
        ids = []
        if name:
            ids = self.search(cr, uid, [('codigo', 'ilike', name)] + args, limit=limit)
        if not ids:
            ids = self.search(cr, uid, [('motivo', operator, name)] + args, limit=limit)
        return self.name_get(cr, uid, ids, context=context)


    _columns = {
        'codigo': fields.char('Codigo', size=10, required = True),
        'motivo': fields.char('Motivo', size=200, required = True),
        'account_id': fields.many2one('account.account', 'Cuenta Contable', required=True),
        'account_analytic_id': fields.many2one('account.analytic.account', 'Cuenta Analitica'),
    }
    _defaults = {}
    _sql_constraints = [
        ('codigo_uniq', 'unique(codigo)', 'El Codigo del motivo ya existe'),
        ('account_account_analytic_uniq', 'unique(account_id, account_analytic_id)', 'La combinacion de Cuenta Contable y Cuenta Analitica ya existe'),
    ]


correccion_stock_motivos()
