"""
course.py

This module defines the Course class which contains multiple assignments,
grading categories with weights, and methods to calculate category averages
and final grades.
"""

from typing import List, Dict
from assignment import Assignment

class Course:
    def __init__(self, course_name: str, credit_hours: int, categories: Dict[str, float]):
        """
        Initialize a Course.

        Args:
            course_name (str): Name of the course (e.g., "Math").
            credit_hours (int): Number of credit hours for the course.
            categories (Dict[str, float]): Mapping of category names to their weight percentages.

        Raises:
            ValueError: If category weights do not sum to 100%.
        """
        if abs(sum(categories.values()) - 100) > 0.01:
            raise ValueError("Category weights must sum to 100%")
        self.course_name = course_name
        self.credit_hours = credit_hours
        self.categories = categories  # e.g., {'HOMEWORK': 20, 'QUIZZES': 20, ...}
        self.assignments: List[Assignment] = []

    def add_assignment(self, assignment: Assignment):
        """
        Add an assignment to the course.

        Args:
            assignment (Assignment): Assignment object to add.

        Raises:
            ValueError: If assignment category is not valid for the course.
        """
        if assignment.category not in self.categories:
            raise ValueError(f"Invalid category '{assignment.category}'")
        self.assignments.append(assignment)

    def get_category_average(self, category: str) -> float:
        """
        Calculate the average score for a category.

        Args:
            category (str): The category to calculate average for.

        Returns:
            float: Average percentage score for the category, or None if no assignments.
        """
        assignments_in_category = [a for a in self.assignments if a.category == category]
        if not assignments_in_category:
            return None  # Exclude empty categories
        total = sum(a.score_percentage() for a in assignments_in_category)
        return total / len(assignments_in_category)

    def get_final_grade(self):
        """
        Calculate the weighted final grade for the course.

        Returns:
            tuple: (final_percentage: float, letter_grade: str)
        """
        total_weighted_score = 0
        total_weights_used = 0
        for cat, weight in self.categories.items():
            avg = self.get_category_average(cat)
            if avg is not None:
                total_weighted_score += avg * (weight / 100)
                total_weights_used += weight

        if total_weights_used == 0:
            return 0, 'F'  # No assignments at all

        # Normalize to 100%
        final_percentage = total_weighted_score * (100 / total_weights_used)
        letter = self.get_letter_grade(final_percentage)
        return final_percentage, letter

    @staticmethod
    def get_letter_grade(percentage: float) -> str:
        """
        Convert a percentage score to a letter grade.

        Args:
            percentage (float): Final percentage score.

        Returns:
            str: Letter grade ('A', 'B', 'C', 'D', 'F').
        """
        if percentage >= 90:
            return 'A'
        elif percentage >= 80:
            return 'B'
        elif percentage >= 70:
            return 'C'
        elif percentage >= 60:
            return 'D'
        return 'F'
