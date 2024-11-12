from odoo import fields,models


class PDFCFReport(models.AbstractModel):
    _name = "report.pk_advance_cash_flow_pdf_statement.cash_flow_pdf_temp_id"
    _description = "Advance PDF Cash Flow Report"

    def _get_report_values(self,docids, data=None):
        accounts = self.env['account.account'].search([('account_type', '=', 'asset_cash')])
        date_from = data.get('date_from')
        date_to = data.get('date_to')

        # Prepare list of account details with balances
        account_data = []
        total_bal = 0.0
        for account in accounts:
            account_balance = sum(self.env['account.move.line'].search([
                ('account_id', '=', account.id),
                ('date', '<', date_from),
                ('move_id.state', '=', 'posted')
            ]).mapped('debit'))

            account_data.append({
        'id': account.id, 'name': account.name, 'balance': account_balance})

        total_bal = sum(item['balance'] for item in account_data)
    ################################################################################
        # Adjust account_data to include all lines within the date range
        all_entries = []
        all_account_entries = 0.0
        for account in accounts:
            account_move_lines = self.env['account.move.line'].search([
                ('account_id', '=', account.id),
                ('date', '>=', date_from),
                ('date', '<=', date_to),
                ('move_id.state', '=', 'posted')
            ])

            for line in account_move_lines:
                # Append each line's details to account_data
                all_entries.append({ 'account_id': account.id,'description': line.name, 'debit': line.debit, })

        # Calculate total balance for the date range if needed
        all_account_entries = sum(item['debit'] for item in all_entries)

        ################################################################################
         # today received amount and its total

        today_balances = []  # To store balances for today's total receipt
        today_total = 0.0  # Total of today balances
        current_date = fields.Date.today()

        for account in accounts:
            # Calculate today's balance
            today_balance = sum(self.env['account.move.line'].search([
                ('account_id', '=', account.id),
                ('date', '=', current_date),
                ('move_id.state', '=', 'posted')
            ]).mapped('debit'))
            today_balances.append(today_balance)
            today_total += today_balance
#################################################################################################
        # funds available for use
        # Prepare list of funds available with opening and date range balances
        funds_available = []
        total_funds = 0.0

        for account in accounts:
            # Retrieve opening balance (before the start date)
            opening_balance = sum(self.env['account.move.line'].search([
                ('account_id', '=', account.id),
                ('date', '<', date_from),
                ('move_id.state', '=', 'posted')
            ]).mapped('debit'))

            # Retrieve balance within the date range
            date_range_balance = sum(self.env['account.move.line'].search([
                ('account_id', '=', account.id),
                ('date', '>=', date_from),
                ('date', '<=', date_to),
                ('move_id.state', '=', 'posted')
            ]).mapped('debit'))

            # Append data to funds_available with account details and balances
            funds_available.append({
                'account_id': account.id,
                'opening_balance': opening_balance,
                'date_range_balance': date_range_balance
            })

            # Update total funds
            total_funds += opening_balance + date_range_balance

        ###############################################################################################
        accounts_credit = 0.0
        acc_cre_list = []

        # Iterate over each account to calculate  credit
        for account in accounts:
            # Retrieve account move lines within the date range
            account_move_lines = self.env['account.move.line'].search([
                ('account_id', '=', account.id),
                ('date', '>=', date_from),
                ('date', '<=', date_to),
                ('move_id.state', '=', 'posted')
            ])
            for line in account_move_lines:
                # Append each line's details to account_data
                acc_cre_list.append({ 'account_id': account.id,'description': line.name, 'credit': line.credit, })
            accounts_credit = sum(item['credit'] for item in acc_cre_list)


    ################################################################################
        # total credit of the period
        credit_funds_available = []
        total_credit_funds = 0.0

        for account in accounts:
            # Retrieve credit balance within the date range
            date_range_credit_balance = sum(self.env['account.move.line'].search([
                ('account_id', '=', account.id),
                ('date', '>=', date_from),
                ('date', '<=', date_to),
                ('move_id.state', '=', 'posted')
            ]).mapped('credit'))

            # Append individual account's credit balance to the list if greater than 0
              # Only add if there is a credit balance
            credit_funds_available.append({
                'account_id': account.id,
                'credit_balance': date_range_credit_balance
            })

            # Update total credit funds
            total_credit_funds += date_range_credit_balance

        ############################################################################################
        # Initialize closing balance and totals
        closing_balance = 0.0
        closing_total = []

        total_funds = 0.0
        total_credit_funds = 0.0

        for account in accounts:
            # Retrieve the opening balance (debit sum before the start date)
            opening_balance = sum(self.env['account.move.line'].search([
                ('account_id', '=', account.id),
                ('date', '<', date_from),
                ('move_id.state', '=', 'posted')
            ]).mapped('debit'))

            # Retrieve the date range balance (debit sum within the date range)
            date_range_balance = sum(self.env['account.move.line'].search([
                ('account_id', '=', account.id),
                ('date', '>=', date_from),
                ('date', '<=', date_to),
                ('move_id.state', '=', 'posted')
            ]).mapped('debit'))

            # Retrieve the credit balance within the date range (for deduction)
            date_range_credit_balance = sum(self.env['account.move.line'].search([
                ('account_id', '=', account.id),
                ('date', '>=', date_from),
                ('date', '<=', date_to),
                ('move_id.state', '=', 'posted')
            ]).mapped('credit'))

            # Calculate total funds for this account (debits within and before date range minus credits within range)
            account_funds = (opening_balance + date_range_balance) - date_range_credit_balance

            # Add account-specific closing balance to closing_total
            closing_total.append({
                'account_id': account.id,
                'closing_balance': account_funds,
            })

            # Update cumulative totals for all accounts
            total_funds += opening_balance + date_range_balance
            total_credit_funds += date_range_credit_balance

        # Calculate cumulative closing balance across all accounts
        closing_balance = total_funds - total_credit_funds

        return {
            'account_data': account_data,
            'all_account_entries': all_account_entries,
            'all_entries': all_entries,
            'total_bal': total_bal,
            'today_balance': today_balances,
            'today_total': today_total,
            'funds_available': funds_available,
            'total_funds': total_funds,
            'acc_cre_list': acc_cre_list,
            'accounts_credit': accounts_credit,
            'credit_funds_available': credit_funds_available,
            'total_credit_funds': total_credit_funds,
            'closing_total': closing_total,
            'closing_balance': closing_balance,
            'date_from': date_from,
            'date_to': date_to,
            'current_date':fields.Date.today(),
        }
