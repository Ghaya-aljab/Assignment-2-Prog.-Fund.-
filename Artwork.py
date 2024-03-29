import random
from Location import Location

class Artwork:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year
        self._historical_significance = self.generate_random_significance()
        self._location = self.generate_random_location()

    def generate_random_significance(self):
        significance_options = ["Unknown", "Significant", "Notable", "Historically Important"]
        return random.choice(significance_options)

    def generate_random_location(self):
        locations = list(Location)
        return random.choice(locations)

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_artist(self, artist):
        self.artist = artist

    def get_artist(self):
        return self.artist

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_historical_significance(self, significance):
        self._historical_significance = significance

    def get_historical_significance(self):
        return self._historical_significance

    def set_location(self, location):
        self._location = location

    def get_location(self):
        return self._location
