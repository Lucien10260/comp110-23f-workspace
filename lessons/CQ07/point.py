"""Module for the Point class used in CQ07 challenge question.

This module contains the Point class which represents a (x, y) coordinate point.
It includes methods for scaling and arithmetic operations on points.
"""

from __future__ import annotations

__author__ = "730521715"


class Point:
    """Class to represent a (x, y) coordinate point."""

    def __init__(self, init_x: float = 0.0, init_y: float = 0.0):
        """Construct a point with optional default values."""
        self.x = init_x
        self.y = init_y

    def __str__(self) -> str:
        """Return a string representation of the point."""
        return f"x: {self.x}; y: {self.y}"

    def __mul__(self, factor: int | float) -> Point:
        """Return a new Point with scaled x and y coordinates."""
        return Point(self.x * factor, self.y * factor)

    def __add__(self, factor: int | float) -> Point:
        """Return a new Point with increased x and y coordinates."""
        return Point(self.x + factor, self.y + factor)

    def scale_by(self, factor: int) -> None:
        """Modify the point."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Make a new point."""
        return Point(self.x * factor, self.y * factor)
