from Person import Person

class Visitor(Person):
    ''' A class representing a museum visitor, inheriting attributes from the Person class '''

    def __init__(self, name, age, national_id, ):
        super().__init__(name, age, national_id)
        self.__tickets = []  #Initializes an empty list for tickets, now with name mangling

    def get_tickets(self):
        return self.__tickets

    def add_tickets(self, value):
        self.__tickets = value

    def purchase_ticket(self, ticket):
        self.__tickets.append(ticket)

    #
    # def show_tickets(self): #Prints details of each ticket owned by the visitor
    #     for ticket in self.__tickets:
    #         event = ticket.get_event()
    #         print(f"Event: {event.name}, Price: {ticket.get_price()}")
    #
#aggregation relationship ( line at visitor)
