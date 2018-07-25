class Customer:
    """
    This is the Customer class, notes that "double underscore" to represent private variables
    """

    def __init__(self, _id, name):
        self.__id = _id
        self.__name = name

    def __str__(self):
        return "name: " + self.__name + ", id: " + str(self.__id)
