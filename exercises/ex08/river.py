"""River."""

__author__ = "730521715"

from bear import Bear
from fish import Fish

class River:
    def __init__(self, num_fish, num_bears):
        self.day = 0
        self.fish = [Fish() for _ in range(num_fish)]
        self.bears = [Bear() for _ in range(num_bears)]

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        for fish in self.fish:
            fish.one_day()
        for bear in self.bears:
            bear.one_day()
        self.day += 1

    def one_river_week(self):
        for _ in range(7):
            self.one_river_day()

    def check_ages(self):
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]

    def remove_fish(self, amount):
        self.fish = self.fish[amount:]

    def repopulate_bears(self):
        new_bears = len(self.bears) // 2
        for _ in range(new_bears):
            self.bears.append(Bear())

    def repopulate_fish(self):
        new_fish = (len(self.fish) // 2) * 4
        for _ in range(new_fish):
            self.fish.append(Fish())

    def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self):
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]