# Student GradeBook System

## Project Overview

This project implements a Student GradeBook system in Python that tracks assignments across weighted categories, calculates final grades, and computes GPA for students. It demonstrates object-oriented programming using nested data structures, arithmetic calculations, and proper data validation.

The system supports:

- Multiple students  
- Multiple courses per student  
- Multiple assignments per course  
- Weighted grading categories  
- Letter grade calculation  
- GPA calculation weighted by credit hours  
- Generating formatted transcripts  

---

## Features

- **Assignment Class**: Stores assignment name, points earned, points possible, and category.  
- **Course Class**: Stores course name, credit hours, grading categories (with weights), and assignments.  
  - Calculates category averages  
  - Calculates weighted final grade  
  - Converts final grade to letter grade  
- **Student Class**: Stores student ID, name, and enrolled courses.  
- **GradeBook Class**: Manages all students, enrollments, assignments, and provides:  
  - Add student  
  - Enroll in course  
  - Add assignment  
  - Get category average  
  - Get course grade  
  - Calculate cumulative GPA  
  - Generate transcript  

- **Edge Case Handling**:  
  - Missing assignments are scored as 0  
  - Categories with no assignments are excluded from weighted calculations  
  - Courses with no assignments are handled gracefully  

---

## How to Run

### Run the demo

`python main.py`

### Run unit tests

Unit tests are written using Python’s built-in unittest framework.

`python -m unittest test_gradebook.py`

## Sample Input and Output 

Input : 

```
from gradebook import GradeBook
from assignment import Assignment

gb = GradeBook()
gb.add_student("S001", "Alice")
gb.enroll_in_course("S001", "Math", 3)
gb.add_assignment("S001", "Math", Assignment("HW1", 85, 100, "HOMEWORK"))
print(gb.generate_transcript("S001"))
```
Output :

```
Transcript for Alice (ID: S001)
----------------------------------------
Math: 85.00% (B)
----------------------------------------
Cumulative GPA: 3.00
```


# Testing Objectives Checklist

- [x] Arithmetic calculations (percentages, averages, weighted sums, GPA)
- [x] Nested data structures (GradeBook -> Student -> Course -> Assignment)
- [x] Weighted averages (course grade calculation using category weights, excluding empty categories)
- [x] Data validation and formatting (category weights sum to 100, valid assignment categories, formatted transcripts)

# Assignment Requirements Checklist

- [x] Classes: Assignment, Course, Student, GradeBook
- [x] Weighted categories: HOMEWORK (20%), QUIZZES (20%), MIDTERM (25%), FINAL_EXAM (35%)
- [x] Multiple assignments per category
- [x] Letter grades: A (90-100), B (80-89), C (70-79), D (60-69), F (<60)
- [x] GPA points: A=4.0, B=3.0, C=2.0, D=1.0, F=0.0
- [x] Edge cases: missing assignments scored as 0, categories with no assignments excluded
- [x] Demonstration with 3 students, 2-3 courses each, varying assignments
- [x] Unit tests for all core methods
- [x] Config files included (if any)
- [x] README includes setup, sample input/output, and assumptions

# Assumptions

- Category weights for each course must sum to 100%
- Students can have any number of courses, and courses can have any number of assignments per category
- Missing assignments are treated as 0 points
- Categories with no assignments do not affect weighted average calculation
- GPA is calculated weighted by credit hours
- Only numeric points are allowed for assignments
- Letter grades strictly follow the defined ranges





