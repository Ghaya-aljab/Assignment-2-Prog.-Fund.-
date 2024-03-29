from Artwork import Artwork

class Museum:
    """ A class that represents a Museum. """

    # Constructor method for initializing a Museum object with a name and an empty list of artworks
    def __init__(self, name):
        self.name = name  # Name of the museum
        self.artworks = []  # An empty list to store artworks

    # Method to add a new artwork to the museum's collection
    def add_artwork(self, title, artist, year):
        new_artwork = Artwork(title, artist, year)
        self.artworks.append(new_artwork)  # Adding the new artwork to the collection

    # Method to remove an artwork from the museum's collection by its title
    def remove_artwork(self, title):
        for artwork in self.artworks:
            if artwork.title == title:  # Check if the current artwork's title matches the one to remove
                self.artworks.remove(artwork)  # Removes the artwork from the list/collection
                break

    # Method to print out a list of all artworks in the museum's collection
    def list_artworks(self):
        for artwork in self.artworks:
            print(f"Title: {artwork.title}, Artist: {artwork.artist}, Year: {artwork.year}")
