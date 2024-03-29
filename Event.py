from Location import Location # calling the location class
import random
from datetime import datetime, timedelta

class Event:
    ''' A class representing an Event '''
    # Constructor method for initializing an Event object with all necessary attributes
    def __init__(self, name, start_date, end_date, location: Location, is_tour=False, guide_name=None, group_size=None):
        self._name = name
        self._start_date = start_date
        self._end_date = end_date
        self._location = location
        self.is_tour = is_tour
        self._guide_name = guide_name
        self._group_size = group_size

    # Setter and getter function for event attributes
    def get_name(self):
        return self._name

    def get_start_date(self):
        return self._start_date

    def get_end_date(self):
        return self._end_date

    def get_location(self):
        return self._location

    def get_guide_name(self):
        return self._guide_name

    def get_group_size(self):
        return self._group_size

    def set_name(self, name):
        self._name = name

    def set_start_date(self, start_date):
        self._start_date = start_date

    def set_end_date(self, end_date):
        self._end_date = end_date

    def set_location(self, location):
        self._location = location

    def set_guide_name(self, guide_name):
        self._guide_name = guide_name

    def set_group_size(self, group_size):
        self._group_size = group_size

    def generate_random_event():
        event_names = ['Night at the Museum', 'Historical Treasures', 'Art & Wine Night', 'Ancient Civilizations', 'Modern Art Madness']
        locations = [Location.EXHIBITION_HALL, Location.OUTDOOR_SPACE, Location.PERMANENT_GALLERY]
        start_date = datetime.now()
        end_date = start_date + timedelta(days=random.randint(1, 5))
        name = random.choice(event_names)
        location = random.choice(locations)
        is_tour = random.choice([True, False])
        guide_name = 'Saif' if is_tour else None
        group_size = random.randint(15, 40) if is_tour else None

        return Event(name, start_date, end_date, location, is_tour, guide_name, group_size)

    def __str__(self):
        start_date_str = self._start_date.strftime('%Y-%m-%d')
        end_date_str = self._end_date.strftime('%Y-%m-%d')
        return f"{self._name} - Location: {self._location.value}, Start: {start_date_str}, End: {end_date_str}"

