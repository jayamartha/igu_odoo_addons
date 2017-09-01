# -*- coding: utf-8 -*-

{
    'name': 'Otoritas HPP',
    'summary': """Lihat HPP (Cost) di produk, hanya oleh Group Tertentu""",
    'version': '10.0.1.0.0',
    'description': """Lihat HPP (Cost) di produk, hanya oleh Group Tertentu""",
    'author': 'IT@Indoguna',
    'website': 'http://www.indoguna.co.id',
    'category': 'Indoguna',
    'depends': ['base', 'purchase'],
    'license': 'AGPL-3',
    'data': [
        'security/view_cost_price.xml',
        'views/hide_product_cost.xml'
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,

}
