"""CQ07."""

__author__ = "730521715"

class Point:
    def __init__(self, x_init: float, y_init: float):
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int):
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int):
        return Point(self.x * factor, self.y * factor)
