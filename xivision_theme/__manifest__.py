# -*- coding: utf-8 -*-
{
    'name': 'xIVISION Theme — Odoo 19 Enterprise',
    'version': '19.0.1.0.0',
    'summary': 'Branding ExcelVision / xIVISION — cores, tipografia e identidade visual',
    'description': """
        Módulo de personalização visual para o backend e frontend do Odoo 19 Enterprise.
        Aplica o Design System oficial da ExcelVision (xIVISION) sem modificar ficheiros core.
        Compatível com Odoo 19 Enterprise em cloud (não-SH).
    """,
    'category': 'Themes/Backend',
    'author': 'ExcelVision, Lda.',
    'website': 'https://excelvision.pt',
    'license': 'LGPL-3',
    'depends': ['web', 'base_setup'],
    'assets': {
        # ── 1. Variáveis SCSS — carregadas ANTES de tudo o resto ──────────────
        #    "prepend" garante que as nossas variáveis sobrescrevem as do Odoo.
        'web._assets_primary_variables': [
            ('prepend', 'xivision_theme/static/src/scss/primary_variables.scss'),
        ],
        # ── 2. Estilos complementares do backend ──────────────────────────────
        #    Aplicados depois do bundle principal para personalizar componentes
        #    específicos do Enterprise (kanban, form view, chatter, etc.)
        'web.assets_backend': [
            'xivision_theme/static/src/scss/backend_overrides.scss',
        ],
        # ── 3. Estilos do portal / website público ────────────────────────────
        'web.assets_frontend': [
            'xivision_theme/static/src/scss/frontend_overrides.scss',
        ],
    },
    'images': ['static/description/icon.svg'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
