# -*- coding: utf-8 -*-
{
    'name': "Kolom Tanda Tangan di SO",

    'summary': """
        Modifikasi Cetakan Sales Order
        """,

    'description': """
        Add On untuk menambahkan kolom tanda tangan pada cetakan Sales Order untuk :
        - Salesman
        - Sales Supervisor / Manager
        - Petugas gudang yang terima DO
        
    """,

    'author': "IT@Indoguna",
    'website': "http://www.indoguna.co.id",

    # Kategori bisa digunakan untuk mem-filter module
    'category': 'Indoguna',
    'version': '0.1',

    # Modul yang harus ada
    'depends': ['base'],

    # Load file terkait
    'data': [
        'reports/so_inherited.xml',
    ],
}