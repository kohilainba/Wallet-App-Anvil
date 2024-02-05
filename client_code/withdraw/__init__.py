from ._anvil_designer import withdrawTemplate
from anvil import *
import anvil.users
import anvil.server
from datetime import datetime


class withdraw(withdrawTemplate):
    def __init__(self, user=None, **properties):
        # Set Form properties and Data Bindings
        self.user = user
        self.init_components(**properties)

  
    def button_1_click(self, **event_args):
      current_datetime = datetime.now()
      

      if self.user is not None:
        wallet3 = anvil.server.call('generate_unique_id', self.user['username'], self.user['phone'])

        if wallet3 is None:
            self.label_2.text = "Error: Wallet is empty"
            return

        money3_numeric = ''.join(filter(str.isdigit, str(self.text_box_3.text)))
        money_value = float(money3_numeric) if money3_numeric else 0.0

        selected_symbol = self.drop_down_1.selected_value

        entered_account_number = self.text_box_2.text
        
        user_currencies = anvil.server.call('get_currency_data',entered_account_number)
        

        if len(str(entered_account_number)) < 10 or not str(entered_account_number).isdigit():
          self.label_2.text = "Error: Invalid account number. Please enter at least 10 digits."
          return
        
        
       
        if user_currencies is not None:
            user_currency = user_currencies

            if selected_symbol == '€':
                current_balance = float(user_currency['money_euro'] or 0)
            elif selected_symbol == '$':
                current_balance = float(user_currency['money_usd'] or 0)
            elif selected_symbol == '₣':
                current_balance = float(user_currency['money_swis'] or 0)
            elif selected_symbol == '₹':
                current_balance = float(user_currency['money_inr'] or 0)
            else:
                self.label_2.text = "Error: Invalid currency symbol selected."
                return

            if money_value > current_balance:
                self.label_2.text = "Insufficient Funds for Withdrawal"
                return

            # Deduct the withdrawal amount from the balance
            if selected_symbol == '€':
                user_currency['money_euro'] = str(current_balance - money_value)
            elif selected_symbol == '$':
                user_currency['money_usd'] = str(current_balance - money_value)
            elif selected_symbol == '₣':
                user_currency['money_swis'] = str(current_balance - money_value)
            elif selected_symbol == '₹':
                user_currency['money_inr'] = str(current_balance - money_value)

            user_currency.update()

            new_transaction = app_tables.transactions.add_row(
                user=self.user['username'],
                casa=int(entered_account_number),
                e_wallet=wallet3,
                money=f"{selected_symbol}-{money_value}",
                date=current_datetime,
                transaction_type="Withdrawal"
            )

            self.label_2.text = "Withdrawal successful"
        else:
            self.label_2.text = "Error: No matching wallet found for the user or invalid account number."
      else:
        self.label_2.text = "Error: User information is not available"

    def link_2_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("deposit",user=self.user)

    def link_3_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("transfer",user=self.user)

    def link_4_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("withdraw",user=self.user)

    def link_7_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("service",user=self.user)

    def link_1_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("customer",user=self.user)

    def link_13_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("Home")

    def link_8_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("service",user=self.user)

