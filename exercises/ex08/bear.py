"""Bear."""

__author__ = "730521715"

class Bear:
    def __init__(self):
        self.age = 0
        self.hunger_score = 0

class Fish:
    def __init__(self):
        self.age = 0

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

    def one_river_week(self):
        for _ in range(7):
            self.one_river_day()

    def one_day(self):
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish):
        self.hunger_score += num_fish
