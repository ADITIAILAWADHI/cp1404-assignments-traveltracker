class Place:
    """Place class for storing details of a place."""
    def __init__(self, name="", country="", priority=0, is_visited=False):
        """Initialise a Place."""
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visited = is_visited

    def __str__(self):
        """Return a string representation of a Place."""
        return "{self.name},{self.country},{self.priority},{self.is_visited}".format(self=self)

    def mark_visited(self):
        """Set a Place as visited."""
        self.is_visited = True

    def mark_not_visited(self):
        """Set a Place as not visited."""
        self.is_visited = False

    def important(self):
        """Check whether a Place is important or not."""
        if self.priority <= 2:
            return True
        else:
            return False
