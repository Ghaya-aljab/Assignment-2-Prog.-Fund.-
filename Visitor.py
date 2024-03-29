from Person import Person

class Visitor(Person):
    ''' A class representing a museum visitor, inheriting attributes from the Person class '''

    # Constructor method for initializing a Visitor object with specific visitor attributes and inheritance from Person
    def __init__(self, name, age, national_id, ):
        # inherits attributes from person class (the parent class)
        super().__init__(name, age, national_id)
        self.__tickets = []  # Initializes an empty list for tickets, now with name mangling

    # Setter and getter function for visitor attributes
    def get_tickets(self):
        return self.__tickets

    def add_tickets(self, value):
        self.__tickets = value

    def purchase_ticket(self, ticket):
        self.__tickets.append(ticket)
