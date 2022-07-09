from placecollection import PlaceCollection
from place import Place


def run_tests():
    """Test PlaceCollection class."""

    # Test empty PlaceCollection (defaults)
    print("Test empty PlaceCollection:")
    place_collection = PlaceCollection()
    print(place_collection)
    assert not place_collection.places  # an empty list is considered False

    # Test loading places
    print("\nTest loading places:")
    place_collection.load_places('places.csv')
    print(place_collection)
    assert place_collection.places  # assuming CSV file is non-empty, non-empty list is considered True

    # Test adding a new Place with values
    print("\nTest adding new place:")
    place_collection.add_place(Place("Smithfield", "Australia", 5, False))
    print(place_collection)

    # Test sorting places
    print("\nTest sorting - priority:")
    place_collection.sort("priority")
    print(place_collection)

    print("\nTest sorting - name:")
    place_collection.sort("name")
    print(place_collection)

    print("\nTest sorting - country:")
    place_collection.sort("country")
    print(place_collection)

    # Test displaying country of index 0 of places list to check whether the following code works or not
    print("\nTest displaying country of index 0 of places list:")
    print("Expected Australia got {}".format(place_collection.places[0].country))

    # Test saving places
    place_collection.save_places('test_placecollection.csv')

    # test number of unvisited places
    print("\nTest get_number_not_visited")
    print("expected 3 got {}".format(place_collection.get_number_not_visited()))

    # Test convert_boolean_value
    print("\nTest converting boolean value:")
    print("Before - ", place_collection)
    place_collection.convert_boolean_value()
    print("After - ", place_collection)

    # Test length of places
    print("\nTest __len__:")
    print("Expected 4 got {}".format(len(place_collection)))


run_tests()
