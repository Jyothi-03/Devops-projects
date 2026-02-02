"""
gradebook.py

This module defines the GradeBook class which manages students, courses,
assignments, and GPA calculations.
"""

from typing import Dict
from student import Student
from course import Course
from assignment import Assignment

class GradeBook:
    def __init__(self):
        """
        Initialize a GradeBook.
        """
        self.students: Dict[str, Student] = {}

    def add_student(self, student_id: str, name: str):
        """
        Add a new student to the gradebook.

        Args:
            student_id (str): Unique student ID.
            name (str): Student name.
        """
        self.students[student_id] = Student(student_id, name)

    def enroll_in_course(self, student_id: str, course_name: str, credit_hours: int):
        """
        Enroll a student in a course with default category weights.

        Args:
            student_id (str): Student ID.
            course_name (str): Name of the course.
            credit_hours (int): Credit hours for GPA calculation.
        """
        categories = {
            'HOMEWORK': 20,
            'QUIZZES': 20,
            'MIDTERM': 25,
            'FINAL_EXAM': 35
        }
        course = Course(course_name, credit_hours, categories)
        self.students[student_id].enroll(course)

    def add_assignment(self, student_id: str, course_name: str, assignment: Assignment):
        """
        Add an assignment for a student in a specific course.

        Args:
            student_id (str): Student ID.
            course_name (str): Course name.
            assignment (Assignment): Assignment object.
        """
        course = self.students[student_id].get_course(course_name)
        if course:
            course.add_assignment(assignment)

    def get_category_average(self, student_id: str, course_name: str, category: str):
        """
        Get the average for a specific category in a course.

        Returns:
            float: Category average percentage, or None if no assignments.
        """
        course = self.students[student_id].get_course(course_name)
        if course:
            return course.get_category_average(category)
        return None

    def get_course_grade(self, student_id: str, course_name: str):
        """
        Get the final grade for a course.

        Returns:
            tuple: (percentage, letter grade)
        """
        course = self.students[student_id].get_course(course_name)
        if course:
            return course.get_final_grade()
        return None

    def calculate_gpa(self, student_id: str):
        """
        Calculate the GPA for a student weighted by credit hours.

        Returns:
            float: GPA (0.0 - 4.0)
        """
        student = self.students[student_id]
        total_points = 0
        total_credits = 0
        grade_to_points = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}

        for course in student.courses:
            _, letter = course.get_final_grade()
            total_points += grade_to_points[letter] * course.credit_hours
            total_credits += course.credit_hours

        if total_credits == 0:
            return 0.0
        return total_points / total_credits

    def generate_transcript(self, student_id: str):
        """
        Generate a formatted transcript for a student.

        Returns:
            str: Transcript string showing courses, grades, and cumulative GPA.
        """
        student = self.students[student_id]
        transcript = f"Transcript for {student.name} (ID: {student.student_id})\n"
        transcript += "-" * 40 + "\n"

        for course in student.courses:
            percentage, letter = course.get_final_grade()
            transcript += f"{course.course_name}: {percentage:.2f}% ({letter})\n"

        transcript += "-" * 40 + "\n"
        transcript += f"Cumulative GPA: {self.calculate_gpa(student_id):.2f}\n"
        return transcript
