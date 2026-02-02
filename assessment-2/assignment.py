"""
assignment.py

This module defines the Assignment class which represents a single assignment
with points earned, total points possible, and the category it belongs to.
"""

class Assignment:
    def __init__(self, name: str, points_earned: float, points_possible: float, category: str):
        """
        Initialize an Assignment.

        Args:
            name (str): Name of the assignment (e.g., "HW1").
            points_earned (float): Points the student earned.
            points_possible (float): Maximum points possible for the assignment.
            category (str): Category of the assignment (e.g., "HOMEWORK").
        """
        self.name = name
        self.points_earned = points_earned
        self.points_possible = points_possible
        self.category = category

    def score_percentage(self) -> float:
        """
        Calculate the score percentage for the assignment.

        Returns:
            float: Percentage score (0-100). Returns 0 if points_possible is 0.
        """
        if self.points_possible == 0:
            return 0
        return (self.points_earned / self.points_possible) * 100
