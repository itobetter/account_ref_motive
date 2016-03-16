from openerp.report import report_sxw
from openerp.tools import amount_to_text_en
import time

class report_account_ref_issued_check(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(report_account_ref_voucher_print, self).__init__(cr, uid, name, context)
        self.localcontext.update({
            'time': time,
            # 'get_title': self.get_title,
            # 'get_lines':self.get_lines,
            # 'get_on_account':self.get_on_account,
            'convert':self.convert
        })

    def convert(self, amount, cur):
        amt_en = amount_to_text_en.amount_to_text(amount, 'en', cur)
        return amt_en

    def get_lines(self, voucher):
        result = []
        if voucher.type in ('payment','receipt'):
            type = voucher.line_ids and voucher.line_ids[0].type or False
            for move in voucher.move_ids:
                res = {}
                amount = move.credit
                if type == 'dr':
                    amount = move.debit
                if amount > 0.0:
                    res['pname'] = move.partner_id.name
                    res['ref'] = 'Agst Ref'+" "+str(move.name)
                    res['aname'] = move.account_id.name
                    res['amount'] = amount
                    result.append(res)
        else:
            type = voucher.line_ids and voucher.line_ids[0].type or False
            for move in voucher.move_ids:
                res = {}
                amount = move.credit
                if type == 'dr':
                    amount = move.debit
                if amount > 0.0:
                    res['pname'] = move.partner_id.name
                    res['ref'] =  move.name
                    res['aname'] = move.account_id.name
                    res['amount'] = amount
                    result.append(res)
        return result

    def get_title(self, type):
        title = ''
        if type:
            title = type[0].swapcase() + type[1:] + " Voucher"
        return title

    def get_on_account(self, voucher):
        name = ""
        if voucher.type == 'receipt':
            name = "Received cash from "+str(voucher.partner_id.name)
        elif voucher.type == 'payment':
            name = "Payment from "+str(voucher.partner_id.name)
        elif voucher.type == 'sale':
            name = "Sale to "+str(voucher.partner_id.name)
        elif voucher.type == 'purchase':
            name = "Purchase from "+str(voucher.partner_id.name)
        return name

report_sxw.report_sxw(
    'report.account.third.check.voucher.ref.print',
    'report.account.third.check',
    'addons/account_voucher/report/account_ref_voucher_print.rml',
    parser=report_account_ref_issued_check, header="external"
)

class report_account_issued_check(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(report_account_ref_voucher_print, self).__init__(cr, uid, name, context)
        self.localcontext.update({
            'time': time,
            # 'get_title': self.get_title,
            # 'get_lines':self.get_lines,
            # 'get_on_account':self.get_on_account,
            'convert':self.convert
        })

    def convert(self, amount, cur):
        amt_en = amount_to_text_en.amount_to_text(amount, 'en', cur)
        return amt_en

    def get_lines(self, voucher):
        result = []
        if voucher.type in ('payment','receipt'):
            type = voucher.line_ids and voucher.line_ids[0].type or False
            for move in voucher.move_ids:
                res = {}
                amount = move.credit
                if type == 'dr':
                    amount = move.debit
                if amount > 0.0:
                    res['pname'] = move.partner_id.name
                    res['ref'] = 'Agst Ref'+" "+str(move.name)
                    res['aname'] = move.account_id.name
                    res['amount'] = amount
                    result.append(res)
        else:
            type = voucher.line_ids and voucher.line_ids[0].type or False
            for move in voucher.move_ids:
                res = {}
                amount = move.credit
                if type == 'dr':
                    amount = move.debit
                if amount > 0.0:
                    res['pname'] = move.partner_id.name
                    res['ref'] =  move.name
                    res['aname'] = move.account_id.name
                    res['amount'] = amount
                    result.append(res)
        return result

    def get_title(self, type):
        title = ''
        if type:
            title = type[0].swapcase() + type[1:] + " Voucher"
        return title

    def get_on_account(self, voucher):
        name = ""
        if voucher.type == 'receipt':
            name = "Received cash from "+str(voucher.partner_id.name)
        elif voucher.type == 'payment':
            name = "Payment from "+str(voucher.partner_id.name)
        elif voucher.type == 'sale':
            name = "Sale to "+str(voucher.partner_id.name)
        elif voucher.type == 'purchase':
            name = "Purchase from "+str(voucher.partner_id.name)
        return name

report_sxw.report_sxw(
    'report.account.issued.check.ref.print',
    'report.account.issued.check',
    'addons/account_voucher/report/account_ref_voucher_print.rml',
    parser=report_account_issued_check, header="external"
)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
