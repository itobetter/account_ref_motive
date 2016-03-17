# -*- coding: utf-8 -*-
{
    'name': "Flujo de Caja",
    'summary': """categorias y motivos para el flujo de caja""",
    'description': """
        modulo en contabilidad que permite categorizar los motivos del flujo de caja en el pago de clientes y proveedores
    """,
    'author': "promero",
    'category': 'account',
    #Change the version every release for apps.
    'version': '7.0',
    # any module necessary for this one to work correctly
    'depends': [
        'base', 'account_voucher', 'account',
    ],
    # always loaded
    'data': [
        'wizard/account_ref_motive_report.xml',
        'report/account_ref_motive_print.xml',
        'views/motive_account_views.xml',
    ],

    # only loaded in test
}