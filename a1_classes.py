from place import Place
from placecollection import PlaceCollection
# MENU constant defined globally
MENU = """
L - List places
A - Add new place
M - Mark a place as visited
Q - Quit"""


def main():
    places_collection = PlaceCollection()
    places_collection.load_places("places.csv")
    places_collection.sort('priority')
    print("Travel Tracker 2.0 - by Aditi Ailawadhi")
    print("{} places_collection loaded from places.csv".format(len(places_collection)))
    print("Menu: ", MENU)
    user_input = input(">>> ").upper()
    while user_input != 'Q':
        if user_input == 'L':
            display_places(places_collection)
            if places_collection.get_number_not_visited() == 0:
                print("{} places. No places left to visit. Why not add a new place?".format(len(places_collection)))
            else:
                print("{} places. You still want to visit {} places.".format(len(places_collection), places_collection.get_number_not_visited()))
        elif user_input == 'A':
            add_place(places_collection)
        elif user_input == 'M':
            mark_place(places_collection)
        else:
            print("Invalid menu choice")
        print("Menu:", MENU)
        user_input = input(">>> ").upper()
    places_collection.convert_boolean_value()
    places_collection.save_places("places.csv")
    print("{} places saved to places.csv".format(len(places_collection)))
    print("Have a nice day :)")


def display_places(places_collection):
    """Displays (sorted by is_visited) unvisited places labelled with *."""
    places_collection.sort('is_visited')
    for i, place in enumerate(places_collection.places, 1):
        visited_sign = ' '
        if not place.is_visited:
            visited_sign = '*'
        print("{}{}. {:<12s} in {:<14s} priority {:2d}".format(visited_sign, i, place.name, place.country, place.priority))


def add_place(places_collection):
    """Adds new place."""
    new_name = get_string_value("Name")
    new_priority = get_int_value()
    new_country = get_string_value("Country")
    places_collection.add_place(Place(new_name, new_country, new_priority, False))
    print("{} in {} (priority {}) added to Travel Tracker".format(new_name, new_country, new_priority))


def get_string_value(content):
    """Return string value with Error Checking."""
    user_input = input("{}: ".format(content))
    while user_input == "":
        print("Input can not be blank")
        user_input = input("{}: ".format(content))
    return user_input


def get_int_value():
    """Return int value with Error Checking."""
    while True:
        try:
            new_priority = int(input("Priority: "))
            if new_priority <= 0:
                print("Number must be > 0")
            else:
                break
        except ValueError:
            print("Invalid input; enter a valid number")
    return new_priority


def mark_place(places_collection):
    """Set an unvisited place as visited."""
    if places_collection.get_number_not_visited() == 0:
        print("No unvisited places")
    else:
        display_places(places_collection)
        marked_place = get_marked_place(places_collection)
        set_visited(marked_place-1, places_collection)


def get_marked_place(places_collection):
    """Returns marked place with error checking"""
    while True:
        try:
            user_input = int(input("Enter the number of a place to mark as visited\n>>> "))
            while user_input <= 0 or user_input > len(places_collection):
                if user_input <= 0:
                    print("Number must be > 0")
                else:
                    print("Invalid place number")
                user_input = int(input("Enter the number of a place to mark as visited\n>>> "))
            return user_input
        except ValueError:
            print("Invalid input; enter a valid number")


def set_visited(marked_place, places_collection):
    """Mark the place as visited"""
    if places_collection.places[marked_place].is_visited:
        print("The place is already visited {}".format(places_collection.places[marked_place].name))
    else:
        places_collection.places[marked_place].mark_visited()
        print("{} in {} visited!".format(places_collection.places[marked_place].name, places_collection.places[marked_place].country))


if __name__ == '__main__':
    main()
