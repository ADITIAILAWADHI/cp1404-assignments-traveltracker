from place import Place


def run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    print("Test empty place:")
    default_place = Place()
    print(default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.is_visited

    # Test initial-value place
    print("\nTest initial-value place:")
    new_place = Place("Malagar", "Spain", 1, False)
    print("Expected: Malagar,Spain,1,False\nGot: {}".format(new_place))

    # Test mark_visited method to set is_visited True
    place1 = Place("Malagar", "Spain", 1, False)
    print("\nTest mark_visited method:")
    print("Before - Expected: False \tGot: {}".format(place1.is_visited))
    place1.mark_visited()
    print("After - Expected: True   \tGot: {}".format(place1.is_visited))

    # Test mark_not_visited method to set is_visited False
    place2 = Place("Malagar", "Spain", 1, True)
    print("\nTest mark_not_visited method:")
    print("Before - Expected: True \tGot: {}".format(place2.is_visited))
    place2.mark_not_visited()
    print("After - Expected: False \tGot: {}".format(place2.is_visited))

    # test important method to check whether a place is important or not
    place3 = Place("Malagar", "Spain", 2, True)
    print("\nTest important method:")
    print("Expected: True \tGot: {}".format(place3.important()))

    # test important method to check whether a place is important or not
    place4 = Place("Malagar", "Spain", 3, True)
    print("\nTest important method:")
    print("Expected: False \tGot: {}".format(place4.important()))


run_tests()
