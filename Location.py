from enum import Enum

class Location(Enum):
    ''' An enumeration representing the possible locations for artworks in the museum '''
    PERMANENT_GALLERY = 1
    EXHIBITION_HALL = 2
    OUTDOOR_SPACE = 3
