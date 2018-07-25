from abc import abstractmethod


class BankAccount:
    """
    By default, Python doesn't know an abstract class.
    Therefore, this class will act as an abstract class
    """

    def __init__(self, customer):
        self._customer = customer # this is the instance holder
        self._balance = 0

    def __str__(self):
        return "BankAccountDetails: " + str(self._customer) + ", balance: " + str(self._balance)

    # deposit amount
    def deposit(self, amount):
        assert amount > 0, "Cannot take a negative value"
        self._balance += amount

    @abstractmethod
    def withdraw(self, amount):
        raise NotImplementedError("This is the abstract method")