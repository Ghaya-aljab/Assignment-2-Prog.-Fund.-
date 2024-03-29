from Event import Event

class Ticket:
    """ A class that represents a ticket for an event at the museum. """

    VAT_RATE = 1.05  # 5% VAT

    def __init__(self, event : Event, age, num_tickets):
        self._event = event
        self._age = age
        self._num_tickets = num_tickets
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
        if self._age < 18 or self._age > 60:
            return 0  # Free tickets for children and seniors
        elif self._num_tickets > 5:  # Group discount for more than five tickets
            price_before_vat = (base_price * 0.5) * self._num_tickets
        else:
            price_before_vat = base_price * self._num_tickets
        return price_before_vat * Ticket.VAT_RATE

