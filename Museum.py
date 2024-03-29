from Artwork import Artwork

class Museum:
    def __init__(self, name):
        self.name = name
        self.artworks = []

    def add_artwork(self, title, artist, year):
        new_artwork = Artwork(title, artist, year)
        self.artworks.append(new_artwork)

    def remove_artwork(self, title):
        for artwork in self.artworks:
            if artwork.title == title:
                self.artworks.remove(artwork)
                break

    def list_artworks(self):
        for artwork in self.artworks:
            print(f"Title: {artwork.title}, Artist: {artwork.artist}, Year: {artwork.year}")
