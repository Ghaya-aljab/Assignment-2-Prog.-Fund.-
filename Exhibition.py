from Event import Event
from Location import Location
from Artwork import Artwork

class Exhibition(Event):
    """A class that represents an exhibition at the museum, inheriting from Event and adding artworks and special features."""

    def __init__(self, name, start_date, end_date, location: Location, artworks : Artwork, special_features):
        # Assuming that location is an instance of the Location class
        super().__init__(name, start_date, end_date, location)
        self._artworks = artworks  # This should be a list of Artwork instances
        self._special_features = special_features  # This could be a list or dictionary of special features

    # Getter and setter for artworks
    def get_artworks(self):
        return self._artworks

    def set_artworks(self, artworks):
        self._artworks = artworks

    # Getter and setter for special_features
    def get_special_features(self):
        return self._special_features

    def set_special_features(self, special_features):
        self._special_features = special_features
