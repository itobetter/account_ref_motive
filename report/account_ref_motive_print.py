# -*- coding: utf-8 -*-
# #############################################################################
#
# Odoo, Open Source Management Solution
#    Copyright (C) 2010 - 2014 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
#
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
##############################################################################
import logging
_logger = logging.getLogger(__name__)
import re
import time
from datetime import datetime
from openerp.tools import config
from openerp.report import report_sxw
from openerp.tools.translate import _

class report_print_ref(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(report_print_ref, self).__init__(cr, uid, name, context)
        self.localcontext.update({
            'time': time,
            'get_filter': self._get_filter


        })
    def get_user(self):
        return self.pool.get('res.users').browse(self.cr, self.uid, self.uid).name
    def strToDate(dt):
        if dt:
            dt_date=datetime.date(int(dt[0:4]),int(dt[5:7]),int(dt[8:10]))
            return dt_date
        else:
            return
    def _get_filter(self, voucher, datas=None):
        if datas == None: datas = {}
        filter_voucher = voucher
        if datas.get('form', False):
            filter_voucher = filter(lambda l: self.strToDate(l.date) > self.strToDate(datas['form']['date_from']) and self.strToDate(l.date) < self.strToDate(datas['form']['date_to']), voucher)
            if datas['form'].get('type', False):
                filter_voucher = filter(lambda l: l.type == datas['type'], filter_voucher)
            if datas['form'].get('partner_id', False):
                filter_voucher = filter(lambda l: l.partner.id == datas['partner_id'], filter_voucher)

        return filter_voucher


report_sxw.report_sxw(
    'report.account.ref.voucher.print.out',
    'account.voucher',
    'modules/account_ref_motive/report/account_ref_voucher_out_print.rml',
    parser=report_print_ref, header=False
)

report_sxw.report_sxw(
    'report.account.ref.voucher.print.in',
    'account.voucher',
    'modules/account_ref_motive/report/account_ref_voucher_in_print.rml',
    parser=report_print_ref, header=False
)
