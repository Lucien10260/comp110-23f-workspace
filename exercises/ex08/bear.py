"""Bear class for river ecosystem simulation."""

__author__ = "730521715"


class Bear:
    """Represent a bear in the river ecosystem."""

    def __init__(self) -> None:
        """Initialize a new bear with age 0 and hunger score 0."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self) -> None:
        """Age the bear by one day and decrease hunger score by 1."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """Increase the bear's hunger score by the number of fish eaten."""
        self.hunger_score += num_fish
