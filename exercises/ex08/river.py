"""River."""

__author__ = "730521715"

def check_ages(self):
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]

def remove_fish(self, amount):
        self.fish = self.fish[amount:]


def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

def check_hunger(self):
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]

def repopulate_bears(self):
        new_bears = len(self.bears) // 2
        self.bears.extend([Bear() for _ in range(new_bears)])

def repopulate_fish(self):
        new_fish = (len(self.fish) // 2) * 4
        self.fish.extend([Fish() for _ in range(new_fish)])
