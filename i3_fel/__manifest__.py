# -*- encoding: utf-8 -*-

{
    'name': 'i3_proxy',
    'version': '3.0',
    'category': 'Invoicing',
    'description': """ 
                    Capa base para la configuración de FEL en Odoo para Guatemala.  Esta capa es independiente del certificador y requiere de la capa adicional del certificador específico.
                    Las configuraciones específicas se encuentran en:
                    Company: datos del certificador (credenciales y otros)
                    Journal: define si requiere certificación, el tipo de DTE y otras reglas de la certificacion
                    Facturas: crea campos para almacenar información del DTE
                    """,
    'author': 'Integración Inteligente de Información S.A.',
    'website': 'http://i3.gt',
    'license': 'OPL-1',
    'depends': ['account','l10n_gt'],
    'data': [
        'data/cargar_incoterms.xml',
        'data/cargar_diario.xml',
        'views/account_move_view.xml', 
        # 'views/pre_account.xml',
        'views/journal_view.xml',
    ],
    'demo': [],
    'installable': True
}
