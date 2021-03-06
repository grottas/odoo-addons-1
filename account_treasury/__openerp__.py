# -*- encoding: utf-8 -*-
##############################################################################
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
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

{
    "name": "Account Treasury",
    "version": "8.0.1.0.0",
    "depends": [
        "account",
        "purchase",
    ],
    "author": "NuoBiT Solutions, S.L., Eric Antones",
    "website": "https://www.nuobit.com",
    'license': 'AGPL-3',
    "category": "Accounting",
    "description": """
        This module manages the treasury.
        Calculates the treasury forecast from supplier and customer invoices,
        recurring payments and variable payments.
    """,
    'data': [
        "security/ir.model.access.csv",
        "wizard/wiz_create_invoice_view.xml",
        "views/account_treasury_forecast_view.xml",
        "views/account_treasury_forecast_template_view.xml",
        "views/account_treasury_report.xml",
        "views/report_account_treasury_forecast.xml",
        "reports/account_treasury_report_view.xml",
    ],
    'demo': [],
    'installable': True,
}
