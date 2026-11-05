import math

class FieldPosition:
    """ Represents 2D position (x,y) on the football field"""

    def __init__(self, x: float, y:float):
        self.x = float(x)
        self.y = float(y)

    def distance_to(self, other: "FieldPosition") -> float:
        """ Calculates the Euclidean distance to another field position."""
        return math.sqrt( (self.x - other.x)**2 + (self.y - other.y)**2 )

    def is_within_bounds(self, length: float = 100.0, width: float = 50.0) -> bool:
        """Checks if the position lies within standard CRFC field dimensions (in feet)"""
        return 0.0 <= self.x < length and 0.0 <= self.y < width

    def _repr__(self) -> str:
        return f"FieldPosition(x={self.x}, y={self.y})"