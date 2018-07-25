from model.bankaccount import BankAccount
from model.customer import Customer
from model.savingsaccount import SavingsAccount
from model.creditcardaccount import CreditCardAccount
import validator


def main():

    # creates 3 customers
    customers = [Customer(1, "Doe"), Customer(2, "Ray"), Customer(3, "Me")]

    # creates 3 accounts
    accounts = [CreditCardAccount(customers[0]), (SavingsAccount(customers[1])), CreditCardAccount(customers[2])]

    # task 1
    for account in accounts:
        if isinstance(account, CreditCardAccount):
            credit_limit_account = validator.get_int("Enter credit card limit: ", 0, True)
            account.set_credit_limit(credit_limit_account)

    # task 2
    wdr_charge_amount = validator.get_int("Enter savings withdrawal charge: ", 0, True)
    SavingsAccount.set_withdraw_charge(wdr_charge_amount)

    # task 3
    for account in accounts:
        # deposit to account
        deposit_amount = validator.get_int("Enter deposit amount: ", 0, True)
        account.deposit(deposit_amount)

        # withdraw from account
        withdrawal_amount = validator.get_int("Enter withdrawal amount: ", 0, True)
        account.withdraw(withdrawal_amount)

    # print the new details of the account
    for account in accounts:
        print(account)


if __name__ == '__main__':
    main()
