from place import Place
from operator import attrgetter


class PlaceCollection:
    def __init__(self):
        """List of Place objects"""
        self.places = []

    def __str__(self):
        """Return a string representation of places list."""
        place_collection = []
        for place in self.places:
            place_collection.append(str(place))
        return str(place_collection)

    def __len__(self):
        """Return length of places list."""
        return len(self.places)

    def load_places(self, load_file):
        """Read content from the csv file and append to places list."""
        csv_file = open('{}'.format(load_file), 'r')
        for content in csv_file:
            row = content.strip().split(',')
            if row[3] == "v":
                place = Place(row[0], row[1], int(row[2]), True)
            else:
                place = Place(row[0], row[1], int(row[2]), False)
            self.places.append(place)
        csv_file.close()

    def save_places(self, save_file):
        """Save (overwrites) places content to save_file."""
        updated_csv_file = open('{}'.format(save_file), 'w')
        for place in self.places:
            updated_csv_file.write("{}\n".format(place))
        updated_csv_file.close()

    def add_place(self, new_place):
        """Add a new place to the places list."""
        self.places.append(new_place)

    def get_number_not_visited(self):
        """Returns number of unvisited places."""
        places_not_visited = 0
        for place in self.places:
            if not place.is_visited:
                places_not_visited += 1
        return places_not_visited

    def sort(self, keyword):
        """Sort list of Place objects by keyword attribute."""
        self.places.sort(key=attrgetter(keyword, "priority"))

    def convert_boolean_value(self):
        """Set is_visited from True and False to 'v' and 'n' respectively."""
        for place in self.places:
            if place.is_visited:
                place.is_visited = "v"
            else:
                place.is_visited = "n"
