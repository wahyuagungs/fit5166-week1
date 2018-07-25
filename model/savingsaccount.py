from model.bankaccount import BankAccount


class SavingsAccount(BankAccount):

    # static variable
    _withdraw_charge = 2

    def __init__(self, customer):
        super().__init__(customer)

    def __str__(self):
        return super().__str__() + " withdraw charge: " + str(SavingsAccount._withdraw_charge)

    # withdraw amoung
    def withdraw(self, amount):
        new_balance = self._balance - amount - SavingsAccount._withdraw_charge
        if new_balance >= 0:
            self._balance = new_balance
        else:
            print("Insufficient funds for the withdraw")

    @staticmethod
    def set_withdraw_charge(new_charge):
        SavingsAccount._withdraw_charge = new_charge

    @staticmethod
    def get_withdraw_charge():
        return SavingsAccount._withdraw_charge
