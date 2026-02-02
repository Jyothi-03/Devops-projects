"""
test_gradebook.py

Unit tests for the GradeBook project using Python's unittest framework.
Tests core functionality of Assignment, Course, Student, and GradeBook classes.
"""

import unittest
from assignment import Assignment
from course import Course
from student import Student
from gradebook import GradeBook

class TestGradeBook(unittest.TestCase):

    def setUp(self):
        """
        Set up a GradeBook with sample students, courses, and assignments for testing.
        This runs before each test.
        """
        # Initialize gradebook
        self.gb = GradeBook()

        # Add students
        self.gb.add_student("S001", "Alice")
        self.gb.add_student("S002", "Bob")

        # Enroll students in courses
        self.gb.enroll_in_course("S001", "Math", 3)
        self.gb.enroll_in_course("S001", "History", 4)
        self.gb.enroll_in_course("S002", "Math", 3)

        # Add assignments for Alice in Math
        self.gb.add_assignment("S001", "Math", Assignment("HW1", 80, 100, "HOMEWORK"))
        self.gb.add_assignment("S001", "Math", Assignment("HW2", 90, 100, "HOMEWORK"))
        self.gb.add_assignment("S001", "Math", Assignment("Quiz1", 70, 100, "QUIZZES"))
        self.gb.add_assignment("S001", "Math", Assignment("Midterm", 85, 100, "MIDTERM"))
        self.gb.add_assignment("S001", "Math", Assignment("Final", 95, 100, "FINAL_EXAM"))

        # Add assignments for Alice in History
        self.gb.add_assignment("S001", "History", Assignment("HW1", 100, 100, "HOMEWORK"))
        self.gb.add_assignment("S001", "History", Assignment("Quiz1", 90, 100, "QUIZZES"))
        self.gb.add_assignment("S001", "History", Assignment("Midterm", 80, 100, "MIDTERM"))
        self.gb.add_assignment("S001", "History", Assignment("Final", 85, 100, "FINAL_EXAM"))

        # Bob has no assignments yet in Math (edge case)

    def test_assignment_percentage(self):
        """Test that Assignment.score_percentage calculates correct percentage."""
        a = Assignment("Test", 45, 50, "HOMEWORK")
        self.assertEqual(a.score_percentage(), 90)

        # Edge case: points_possible = 0
        a_zero = Assignment("Zero", 10, 0, "QUIZZES")
        self.assertEqual(a_zero.score_percentage(), 0)

    def test_course_category_average(self):
        """Test category averages for a course."""
        math_course = self.gb.students["S001"].get_course("Math")
        self.assertAlmostEqual(math_course.get_category_average("HOMEWORK"), 85)  # (80+90)/2
        self.assertAlmostEqual(math_course.get_category_average("QUIZZES"), 70)
        self.assertIsNone(math_course.get_category_average("Nonexistent"))  # No assignments

    def test_course_final_grade(self):
        """Test final course grade calculation including letter grade."""
        math_course = self.gb.students["S001"].get_course("Math")
        percentage, letter = math_course.get_final_grade()
        # Manually compute weighted:
        # HOMEWORK: 85*0.2 = 17
        # QUIZZES: 70*0.2 = 14
        # MIDTERM: 85*0.25 = 21.25
        # FINAL: 95*0.35 = 33.25
        # Total = 17+14+21.25+33.25 = 85.5
        self.assertAlmostEqual(percentage, 85.5)
        self.assertEqual(letter, "B")

    def test_gradebook_course_grade(self):
        """Test GradeBook.get_course_grade returns correct tuple."""
        percentage, letter = self.gb.get_course_grade("S001", "History")
        self.assertAlmostEqual(percentage, 87.75)  #weighted sum
        self.assertEqual(letter, "B")

        # Edge case: student with no assignments
        percentage_bob, letter_bob = self.gb.get_course_grade("S002", "Math")
        self.assertEqual(percentage_bob, 0)
        self.assertEqual(letter_bob, "F")

    def test_calculate_gpa(self):
        """Test GradeBook.calculate_gpa weighted by credit hours."""
        gpa = self.gb.calculate_gpa("S001")
        # History (4 credits, 88.75 -> B=3.0), Math (3 credits, 85.5 -> B=3.0)
        # Weighted GPA = (3*4 + 3*3)? Wait, careful:
        # Math = 3 credits, B=3.0 => 3*3=9
        # History = 4 credits, B=3.0 => 4*3=12
        # Total points = 21, total credits = 7
        self.assertAlmostEqual(gpa, 3.0)

        # Edge case: student with no courses
        self.gb.add_student("S003", "Charlie")
        self.assertEqual(self.gb.calculate_gpa("S003"), 0.0)

    def test_transcript_generation(self):
        """Test transcript output format and content."""
        transcript = self.gb.generate_transcript("S001")
        self.assertIn("Transcript for Alice", transcript)
        self.assertIn("Math: 85.50% (B)", transcript)
        self.assertIn("History: 87.75% (B)", transcript)
        self.assertIn("Cumulative GPA: 3.00", transcript)

if __name__ == '__main__':
    # Run all tests
    unittest.main()
