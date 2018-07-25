from model.bankaccount import BankAccount


class CreditCardAccount(BankAccount):
    """
    This is the CreditCardAccount Class
    """

    # static variable
    _interest_rate = 12.75

    def __init__(self, customer):
        super().__init__(customer)
        self._credit_limit = 0

    # set the credit limit
    def set_credit_limit(self, limit):
        if limit == 1000 or limit == 2000 or limit == 5000 or limit == 10000:
            self._credit_limit = limit
        else:
            print("Invalid credit limit")

    # override the tostring method
    def __str__(self):
        return super().__str__() + "\ncredit limit: " + str(self._credit_limit) + "\ninterest rate: " + str(CreditCardAccount._interest_rate)

    # withdraw amount if sufficient fund
    def withdraw(self, amount):
        new_balance = self._balance - amount
        if new_balance + self._credit_limit >= 0:
            self._balance = new_balance
        else:
            print("Insufficient funds for the withdrawal")

    # interest is charged if account overdrawn
    def charge_interest(self):
        if self._balance < 0:
            self._balance += self._balance * (CreditCardAccount._interest_rate / 100)

    @staticmethod
    def set_interest_rate(new_rate):
        CreditCardAccount._interest_rate = new_rate

    @staticmethod
    def get_interest_rate():
        return CreditCardAccount._interest_rate
