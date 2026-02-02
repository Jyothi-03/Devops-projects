"""
main.py

Demonstration of the GradeBook system:
- Adds students
- Enrolls them in courses
- Adds assignments
- Shows category averages, final grades, GPA, and transcripts
"""

from gradebook import GradeBook
from assignment import Assignment

# Initialize the gradebook
gb = GradeBook()

# -----------------------------
# 1. Add students
# -----------------------------
gb.add_student("S001", "Alice")
gb.add_student("S002", "Bob")
gb.add_student("S003", "Charlie")

# -----------------------------
# 2. Enroll students in courses
# -----------------------------
gb.enroll_in_course("S001", "Math", 3)
gb.enroll_in_course("S001", "History", 4)

gb.enroll_in_course("S002", "Math", 3)
gb.enroll_in_course("S002", "Science", 4)

gb.enroll_in_course("S003", "History", 4)
gb.enroll_in_course("S003", "Science", 3)

# -----------------------------
# 3. Add assignments
# -----------------------------

# Alice - Math
gb.add_assignment("S001", "Math", Assignment("HW1", 85, 100, "HOMEWORK"))
gb.add_assignment("S001", "Math", Assignment("HW2", 90, 100, "HOMEWORK"))
gb.add_assignment("S001", "Math", Assignment("Quiz1", 70, 100, "QUIZZES"))
gb.add_assignment("S001", "Math", Assignment("Midterm", 80, 100, "MIDTERM"))
gb.add_assignment("S001", "Math", Assignment("Final", 95, 100, "FINAL_EXAM"))

# Alice - History
gb.add_assignment("S001", "History", Assignment("HW1", 100, 100, "HOMEWORK"))
gb.add_assignment("S001", "History", Assignment("Quiz1", 90, 100, "QUIZZES"))
gb.add_assignment("S001", "History", Assignment("Midterm", 80, 100, "MIDTERM"))
gb.add_assignment("S001", "History", Assignment("Final", 85, 100, "FINAL_EXAM"))

# Bob - Math (only one assignment, to show partial data)
gb.add_assignment("S002", "Math", Assignment("HW1", 60, 100, "HOMEWORK"))

# Charlie - Science
gb.add_assignment("S003", "Science", Assignment("HW1", 75, 100, "HOMEWORK"))
gb.add_assignment("S003", "Science", Assignment("Quiz1", 80, 100, "QUIZZES"))
gb.add_assignment("S003", "Science", Assignment("Midterm", 70, 100, "MIDTERM"))
gb.add_assignment("S003", "Science", Assignment("Final", 90, 100, "FINAL_EXAM"))

# -----------------------------
# 4. Print category averages and final grades
# -----------------------------
print("Category Averages and Final Grades:\n")

students = ["S001", "S002", "S003"]
for sid in students:
    student = gb.students[sid]
    print(f"Student: {student.name} (ID: {sid})")
    for course in student.courses:
        print(f"  Course: {course.course_name}")
        # Print category averages
        for cat in course.categories:
            avg = course.get_category_average(cat)
            if avg is not None:
                print(f"    {cat} Average: {avg:.2f}%")
        # Final grade
        percentage, letter = course.get_final_grade()
        print(f"    Final Grade: {percentage:.2f}% ({letter})")
    # Cumulative GPA
    gpa = gb.calculate_gpa(sid)
    print(f"  Cumulative GPA: {gpa:.2f}\n")

# -----------------------------
# 5. Generate full transcripts
# -----------------------------
print("\n--- Transcripts ---\n")
for sid in students:
    print(gb.generate_transcript(sid))
