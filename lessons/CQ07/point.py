"""CQ07."""

__author__ = "730521715"


from typing import Union

class Point:
    """Represents a point in a 2D space with x and y coordinates."""

    def __init__(self, x_init: 'float', y_init: 'float'):
        """Initialize a new Point instance with x and y coordinates."""
        self.x = x_init
        self.y = y_init


    def scale_by(self, factor: int) -> None:
        """Scale the point by a given factor in place."""
        self.x *= factor
        self.y *= factor


    def scale(self, factor: int) -> 'Point':
        """Scale the point by a given factor and return a new Point object."""
        return Point(self.x * factor, self.y * factor)
    

    def __str__(self) -> str:
        """String representation of a Point."""
        return f"x: {self.x}; y: {self.y}"

    def __mul__(self, factor: Union[int, float]) -> 'Point':
        """Multiply the point's coordinates by a factor."""
        return Point(self.x * factor, self.y * factor)

    def __add__(self, factor: Union[int, float]) -> 'Point':
        """Add a value to the point's coordinates."""
        return Point(self.x + factor, self.y + factor)
