"""
Name: ADITI AILAWADHI
Date: 30/4/2021
Brief Project Description:
import files
'CHOICES_TO_STATES' for spinner functionality, 'VISITED_COLOR' for visited places and  'UNVISITED_COLOR' for unvisited places constants defined globally
class TravelTrackerApp(App):
    Kivy app constructor class.
    def __init__(self, **kwargs):
        Construct main app.
        Load places from "places.csv".
    def build(self):
        Build the Kivy GUI.
        :return: reference to the root Kivy widget
        self.sort_value = sorted(CHOICES_TO_STATES.keys())
        self.current_sort = self.sort_value[0]
        return self.root
    def create_widgets(self):
        Create buttons from PLaceCollection entries and add them to the GUI.
        Create a button for each place object, specifying the text and the background_color
        Store a reference to the place object in the button object
        add button to the "entries_box" id
      display places_to_visit text
    def press_entry(self, instance):
        place = instance.place
        mark visited place as unvisited and vice- versa and update color
        update button text
        check whether place is visited or unvisited
        check whether place is important or not
        update program_messages
        update places_to_visit
    def widget_instance_text(self, place):
        Display button text.
        return display_widget_instance_text
    def clear(self):
        Clear program_messages and add new places box text inputs.
    def change_sort(self, new_sort):
        Handle change of spinner sort selection.
    def add_new_widget(self, new_name, new_country, new_priority):
        Add a new place object.
        Runs only if all the user inputs are valid
        create a new widget for the new place
        Store a reference to the place object in the button object
        add button to the "entries_box" id
        clear all text fields
        create widgets with sorting
    def is_new_place_valid(self, new_name, new_country, new_priority):
        Check if new place is valid or not.
    def on_stop(self):
        Run when the program ends.
        Updates "places.csv".
GitHub URL: https://github.com/CP1404-BNE-2020-SP22/cp1404-assignment-1---traveltracker-ADITIAILAWADHI
"""
# Create your main program in this file, using the TravelTrackerApp class
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.properties import StringProperty
from kivy.uix.button import Button
from placecollection import PlaceCollection
from place import Place

CHOICES_TO_STATES = {'Name': 'name', 'Country': 'country', 'Priority': 'priority', 'Visited': 'is_visited'}
VISITED_COLOR = (0, 0, 255)
UNVISITED_COLOR = (128, 0, 255)


class TravelTrackerApp(App):
    """Kivy app constructor class."""
    places_to_visit = StringProperty()
    program_messages = StringProperty()
    sort_value = ListProperty()
    current_sort = StringProperty()

    def __init__(self, **kwargs):
        """
        Construct main app.
        Load places from "places.csv".
        """
        super().__init__(**kwargs)
        self.place_collection = PlaceCollection()
        self.place_collection.load_places("places.csv")

    def build(self):
        """
        Build the Kivy GUI.
        :return: reference to the root Kivy widget
        """
        self.title = "TravelTracker"
        self.root = Builder.load_file('app.kv')
        self.sort_value = sorted(CHOICES_TO_STATES.keys())
        self.current_sort = self.sort_value[0]
        return self.root

    def create_widgets(self):
        """
        Create buttons from PLaceCollection entries and add them to the GUI.
        :return: None
        """
        for place in self.place_collection.places:
            # Create a button for each place object, specifying the text and the background_color
            temp_button = Button(text=self.widget_instance_text(place), background_color=VISITED_COLOR if place.is_visited else UNVISITED_COLOR)
            temp_button.bind(on_release=self.press_entry)
            # Store a reference to the place object in the button object
            temp_button.place = place
            # add button to the "entries_box" id
            self.root.ids.entries_box.add_widget(temp_button)
        # display places_to_visit text
        self.places_to_visit = "Places to visit: {}".format(self.place_collection.get_number_not_visited())

    def press_entry(self, instance):
        """on_release button."""
        place = instance.place
        # mark visited place as unvisited and vice- versa and update color
        if place.is_visited:
            place.mark_not_visited()
            instance.background_color = UNVISITED_COLOR
        else:
            place.mark_visited()
            instance.background_color = VISITED_COLOR
        # update button text
        instance.text = self.widget_instance_text(place)
        # check whether place is visited or unvisited
        program_messages_visited = 'You need to visit'
        if place.is_visited:
            program_messages_visited = 'You visited'
        # check whether place is important or not
        important_string = ""
        if place.important():
            if place.is_visited:
                important_string = 'Great travelling!'
            else:
                important_string = 'Get going!'
        # update program_messages
        self.program_messages = "{} {}. {}".format(program_messages_visited, place.name, important_string)
        # update places_to_visit
        self.places_to_visit = "Places to visit: {}".format(self.place_collection.get_number_not_visited())

    def widget_instance_text(self, place):
        """Display button text."""
        visited_string = "(visited)"
        if not place.is_visited:
            visited_string = ""
        display_widget_instance_text = "{} in {}, priority {} {}".format(place.name, place.country, place.priority, visited_string)
        return display_widget_instance_text

    def clear(self):
        """Clear program_messages and add new places box text inputs."""
        self.root.ids.new_name.text = ""
        self.root.ids.new_country.text = ""
        self.root.ids.new_priority.text = ""
        self.program_messages = ""

    def change_sort(self, new_sort):
        """Handle change of spinner sort selection."""
        self.current_sort = new_sort
        # create widgets with sorting
        self.place_collection.sort(CHOICES_TO_STATES[self.current_sort])
        self.root.ids.entries_box.clear_widgets()
        self.create_widgets()

    def add_new_widget(self, new_name, new_country, new_priority):
        """
        Add a new place object.
        Runs only if all the user inputs are valid
        """
        if self.is_new_place_valid(new_name, new_country, new_priority):
            new_priority = int(new_priority)
            self.place_collection.add_place(Place(new_name, new_country, new_priority, False))
            # create a new widget for the new place
            temp_button = Button(text="{} in {}, priority {}".format(new_name, new_country, new_priority), background_color=UNVISITED_COLOR)
            temp_button.bind(on_release=self.press_entry)
            # Store a reference to the place object in the button object
            temp_button.place = self.place_collection.places[0]
            # add button to the "entries_box" id
            self.root.ids.entries_box.add_widget(temp_button)
            # clear all text fields
            self.clear()
            # create widgets with sorting
            self.place_collection.sort(CHOICES_TO_STATES[self.current_sort])
            self.root.ids.entries_box.clear_widgets()
            self.create_widgets()

    def is_new_place_valid(self, new_name, new_country, new_priority):
        """Check if new place is valid or not."""
        input_fields = [new_name, new_country, new_priority]
        # check blank user input
        for user_input in input_fields:
            if user_input == "":
                self.program_messages = "All fields must be completed"
                return False
        # check if new_priority is a valid integer or not
        try:
            new_priority = int(new_priority)
        except ValueError:
            self.program_messages = "Please enter a valid number"
            return False
        # check if new_priority is >= 0
        if new_priority <= 0:
            self.program_messages = "Priority must be > 0"
            return False
        return True

    def on_stop(self):
        """
        Run when the program ends.
        Updates "places.csv".
        """
        self.place_collection.convert_boolean_value()
        self.place_collection.save_places("places.csv")


if __name__ == '__main__':
    TravelTrackerApp().run()
