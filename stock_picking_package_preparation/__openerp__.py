# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Guewen Baconnier
#    Copyright 2015 Camptocamp SA
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

{'name': 'Stock Picking Package Preparation',
 'version': '8.0.1.0.0',
 'author': 'Camptocamp,Odoo Community Association (OCA)',
 'maintainer': 'Camptocamp',
 'license': 'AGPL-3',
 'category': 'Warehouse Management',
 'depends': ['stock',
             ],
 'website': 'http://www.camptocamp.com',
 'data': ['view/stock_picking_package_preparation_view.xml',
          'security/ir.model.access.csv',
          ],
 'test': [],
 'installable': True,
 'auto_install': False,
 }
