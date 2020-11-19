# -*- coding: utf-8 -*-
{
    'name': "method_equivalencia_filtro_man",

    'summary': """
        Campos para alojar los codigos man de los filtros
        para realizar busquedas de equivalencia""",

    'description': """
        Equivalencia filtros man
    """,

    'author': "Method ERP",
    'website': "http://www.method.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}