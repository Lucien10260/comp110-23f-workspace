"""River class for ecosystem simulation."""

__author__ = "730521715"

from exercises.ex08.bear import Bear 
from exercises.ex08.fish import Fish 


class River:
    """Represent a river in the ecosystem simulation."""

    def __init__(self, num_fish: int, num_bears: int) -> None:
        """Initialize a river with specified number of fish and bears."""
        self.day = 0
        self.fish = [Fish() for _ in range(num_fish)]
        self.bears = [Bear() for _ in range(num_bears)]

    def view_river(self) -> None:
        """Display the current state of the river, including fish and bear populations."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self) -> None:
        """Simulate one day in the river, aging both fish and bears."""
        for fish in self.fish:
            fish.one_day()
        for bear in self.bears:
            bear.one_day()
        self.day += 1

    def one_river_week(self) -> None:
        """Simulate a week in the river (7 days)."""
        for _ in range(7):
            self.one_river_day()

    def check_ages(self) -> None:
        """Remove fish older than 3 and bears older than 5 from the river."""
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]

    def remove_fish(self, amount: int) -> None:
        """Remove a specified number of fish from the river."""
        self.fish = self.fish[amount:]

    def repopulate_bears(self) -> None:
        """Add new bears to the river based on the current bear population."""
        new_bears = len(self.bears) // 2
        for _ in range(new_bears):
            self.bears.append(Bear())

    def repopulate_fish(self) -> None:
        """Add new fish to the river based on the current fish population."""
        new_fish = (len(self.fish) // 2) * 4
        for _ in range(new_fish):
            self.fish.append(Fish())

    def bears_eating(self) -> None:
        """Simulate bears eating fish if enough fish are available."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self) -> None:
        """Remove any bears from the river with a negative hunger score."""
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]
