"""Fish class for river ecosystem simulation."""

__author__ = "730521715"


class Fish:
    """Represent a fish in the river ecosystem."""

    def __init__(self) -> None:
        """Initialize a new fish with age 0."""
        self.age = 0

    def one_day(self) -> None:
        """Age the fish by one day."""
        self.age += 1
