from enum import Enum, auto


class VisitorCategory(Enum):
    ADULT = 1
    KID = 2
    ELDER = 3
    STUDENT = 4


class Ticket:
    """ A class that represents a ticket for an event at the museum. """

    VAT_RATE = 1.05  # 5% VAT

    # Constructor method for initializing a Ticket object with details of the event, age of visitor, and number of tickets
    def __init__(self, event, age, num_tickets, category=VisitorCategory.ADULT):
        self._event = event
        self._age = age
        self._num_tickets = num_tickets
        self._category = category
        self._price = self.calculate_price()

    def get_event(self):
        return self._event

    def set_event(self, event):
        self._event = event

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_num_tickets(self):
        return self._num_tickets

    def set_num_tickets(self, num_tickets):
        self._num_tickets = num_tickets

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def calculate_price(self):
        base_price = 63  # Base price for adults

        # Free tickets for children, seniors, and students
        if self._category in [VisitorCategory.KID, VisitorCategory.ELDER, VisitorCategory.STUDENT]:
            return 0

        # Check for group discount for more than five tickets
        if self._num_tickets >= 5:
            price_before_vat = (base_price * 0.5) * self._num_tickets  # Corrected to 50% discount
        else:
            price_before_vat = base_price * self._num_tickets

        # Apply VAT
        return price_before_vat * Ticket.VAT_RATE
