"""
student.py

This module defines the Student class, representing a student with multiple
courses enrolled.
"""

from typing import List
from course import Course

class Student:
    def __init__(self, student_id: str, name: str):
        """
        Initialize a Student.

        Args:
            student_id (str): Unique student ID.
            name (str): Student's full name.
        """
        self.student_id = student_id
        self.name = name
        self.courses: List[Course] = []

    def enroll(self, course: Course):
        """
        Enroll the student in a course.

        Args:
            course (Course): Course object to enroll in.
        """
        self.courses.append(course)

    def get_course(self, course_name: str):
        """
        Retrieve a course by name.

        Args:
            course_name (str): Name of the course.

        Returns:
            Course: Course object if found, else None.
        """
        for c in self.courses:
            if c.course_name == course_name:
                return c
        return None
