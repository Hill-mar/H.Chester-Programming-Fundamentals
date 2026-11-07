# Author: Hilmar Chester
# Date: October 30, 2026
# Description: Collect scores  for two students and compare the results.
# Tier: Base and Intermediate Level
#
# Test Case - Base:
# ------------------------------------
#           STUDENT GRADE REPORT
# ------------------------------------
# Student:      High Performer
# Quiz scores:  [95, 98, 92, 97, 100]
# Average:      96.4 out of 100
# Letter grade: A
# Message:      Excellent work!
# ------------------------------------
#
# ------------------------------------
#           STUDENT GRADE REPORT
# ------------------------------------
# Student:      Average Performer
# Quiz scores:  [75, 82, 70, 68, 80]
# Average:      75.0 out of 100
# Letter grade: C
# Message:      Good effort. Keep working toward your goals!
# ------------------------------------
#
# ------------------------------------
#           STUDENT GRADE REPORT
# ------------------------------------
# Student:      Struggling Student
# Quiz scores:  [55, 48, 60, 52, 58]
# Average:      54.6 out of 100
# Letter grade: F
# Message:      Keep practicing and ask for help when you need it.
# ------------------------------------
#
# Test Case - INTERMEDIATE #1
# ------------------------------------------
#            STUDENT 1 GRADE REPORT
# ------------------------------------------
# Student:      James
# Quiz scores:  [96, 77, 89, 90, 65]
# Average:      83.4 out of 100
# Highest score: 96
# Lowest score:  65
# Letter grade: B
# Message:      Great job. Keep up the solid effort!
# ------------------------------------------

# ------------------------------------------
#            STUDENT 2 GRADE REPORT
# ------------------------------------------
# Student:      John
# Quiz scores:  [96, 77, 89, 90, 65]
# Average:      83.4 out of 100
# Highest score: 96
# Lowest score:  65
# Letter grade: B
# Message:      Great job. Keep up the solid effort!
# ------------------------------------------

# ==========================================================
#                  COMPARISON REPORT
# ==========================================================
# Measure                           James               John
# ----------------------------------------------------------
# Average                            83.4               83.4
# Highest quiz score                   96                 96
# Lowest quiz score                    65                 65
# Letter grade                          B                  B
# ==========================================================
# Higher average: The students tied
# Difference between averages: 0.0 points
# Highest score overall: Both students tied with a score of 96
# Lowest score overall:  Both students tied with a score of 65

# Overall: James and John had the same average.


#Test Case - INTERMEDIATE #2
# ------------------------------------------
#            STUDENT 1 GRADE REPORT
# ------------------------------------------
# Student:      Chris Hopper
# Quiz scores:  [66, 77, 55, 88, 79]
# Average:      73.0 out of 100
# Highest score: 88
# Lowest score:  55
# Letter grade: C
# Message:      Good effort. Keep working toward your goals!
# ------------------------------------------

# ------------------------------------------
#            STUDENT 2 GRADE REPORT
# ------------------------------------------
# Student:      Carl Jones
# Quiz scores:  [78, 90, 85, 92, 81]
# Average:      85.2 out of 100
# Highest score: 92
# Lowest score:  78
# Letter grade: B
# Message:      Great job. Keep up the solid effort!
# ------------------------------------------

# ==========================================================
#                  COMPARISON REPORT
# ==========================================================
# Measure                    Chris Hopper         Carl Jones
# ----------------------------------------------------------
# Average                            73.0               85.2
# Highest quiz score                   88                 92
# Lowest quiz score                    55                 78
# Letter grade                          C                  B
# ==========================================================
# Higher average: Carl Jones
# Difference between averages: 12.2 points
# Highest score overall: Carl Jones (92)
# Lowest score overall:  Chris Hopper (55)

# Overall: Carl Jones outperformed Chris Hopper by 12.2 points.


#Start of Code File 

# Store the letter grades in a tuple.
grade_labels = ("A", "B", "C", "D", "F")

# Welcome both students and explain which scores they will enter.
print("Hey there, students!")
print("Please enter the whole-number scores (0-100) you received for Quizzes 1-5, respectively.")

# Collect Student 1's name and five quiz scores.
student1_name = input("\nPlease enter Student 1's name: ").strip().title()
student1_scores = []

student1_score1 = int(input("Student 1 - Quiz 1 score: "))
student1_scores.append(student1_score1)

student1_score2 = int(input("Student 1 - Quiz 2 score: "))
student1_scores.append(student1_score2)

student1_score3 = int(input("Student 1 - Quiz 3 score: "))
student1_scores.append(student1_score3)

student1_score4 = int(input("Student 1 - Quiz 4 score: "))
student1_scores.append(student1_score4)

student1_score5 = int(input("Student 1 - Quiz 5 score: "))
student1_scores.append(student1_score5)

# Collect Student 2's name and five quiz scores in a separate list.
student2_name = input("\nPlease enter Student 2's name: ").strip().title()
student2_scores = []

student2_score1 = int(input("Student 2 - Quiz 1 score: "))
student2_scores.append(student2_score1)

student2_score2 = int(input("Student 2 - Quiz 2 score: "))
student2_scores.append(student2_score2)

student2_score3 = int(input("Student 2 - Quiz 3 score: "))
student2_scores.append(student2_score3)

student2_score4 = int(input("Student 2 - Quiz 4 score: "))
student2_scores.append(student2_score4)

student2_score5 = int(input("Student 2 - Quiz 5 score: "))
student2_scores.append(student2_score5)

# Calculate each student's average, highest score, and lowest score.
student1_average = sum(student1_scores) / len(student1_scores)
student1_highest = max(student1_scores)
student1_lowest = min(student1_scores)

student2_average = sum(student2_scores) / len(student2_scores)
student2_highest = max(student2_scores)
student2_lowest = min(student2_scores)

# Assign Student 1's letter grade using the average.
if student1_average >= 90:
    student1_grade = grade_labels[0]
elif student1_average >= 80:
    student1_grade = grade_labels[1]
elif student1_average >= 70:
    student1_grade = grade_labels[2]
elif student1_average >= 60:
    student1_grade = grade_labels[3]
else:
    student1_grade = grade_labels[4]

# Choose a message for Student 1 based on the letter grade.
if student1_grade == grade_labels[0]:
    student1_message = "Excellent work!"
elif student1_grade == grade_labels[1]:
    student1_message = "Great job. Keep up the solid effort!"
elif student1_grade == grade_labels[2]:
    student1_message = "Good effort. Keep working toward your goals!"
elif student1_grade == grade_labels[3]:
    student1_message = "Consider visiting office hours for extra help."
else:
    student1_message = "Keep practicing and ask for help when you need it."

# Assign Student 2's letter grade using the average.
if student2_average >= 90:
    student2_grade = grade_labels[0]
elif student2_average >= 80:
    student2_grade = grade_labels[1]
elif student2_average >= 70:
    student2_grade = grade_labels[2]
elif student2_average >= 60:
    student2_grade = grade_labels[3]
else:
    student2_grade = grade_labels[4]

# Choose a message for Student 2 based on the letter grade.
if student2_grade == grade_labels[0]:
    student2_message = "Excellent work!"
elif student2_grade == grade_labels[1]:
    student2_message = "Great job. Keep up the solid effort!"
elif student2_grade == grade_labels[2]:
    student2_message = "Good effort. Keep working toward your goals!"
elif student2_grade == grade_labels[3]:
    student2_message = "Consider visiting office hours for extra help."
else:
    student2_message = "Keep practicing and ask for help when you need it."

# Display Student 1's individual report.
print("\n" + "-" * 42)
print("           STUDENT 1 GRADE REPORT")
print("-" * 42)
print(f"Student:      {student1_name}")
print(f"Quiz scores:  {student1_scores}")
print(f"Average:      {student1_average:.1f} out of 100")
print(f"Highest score: {student1_highest}")
print(f"Lowest score:  {student1_lowest}")
print(f"Letter grade: {student1_grade}")
print(f"Message:      {student1_message}")
print("-" * 42)

# Display Student 2's individual report.
print("\n" + "-" * 42)
print("           STUDENT 2 GRADE REPORT")
print("-" * 42)
print(f"Student:      {student2_name}")
print(f"Quiz scores:  {student2_scores}")
print(f"Average:      {student2_average:.1f} out of 100")
print(f"Highest score: {student2_highest}")
print(f"Lowest score:  {student2_lowest}")
print(f"Letter grade: {student2_grade}")
print(f"Message:      {student2_message}")
print("-" * 42)

# Display a side-by-side comparison using aligned f-string columns.
print("\n" + "=" * 58)
print("                 COMPARISON REPORT")
print("=" * 58)
print(f"{'Measure':<20}{student1_name:>19}{student2_name:>19}")
print("-" * 58)
print(f"{'Average':<20}{student1_average:>19.1f}{student2_average:>19.1f}")
print(f"{'Highest quiz score':<20}{student1_highest:>19}{student2_highest:>19}")
print(f"{'Lowest quiz score':<20}{student1_lowest:>19}{student2_lowest:>19}")
print(f"{'Letter grade':<20}{student1_grade:>19}{student2_grade:>19}")
print("=" * 58)

# Compare the students' averages and calculate their difference.
if student1_average > student2_average:
    average_winner = student1_name
    average_difference = student1_average - student2_average
    overall_summary = (
        f"{student1_name} outperformed {student2_name} "
        f"by {average_difference:.1f} points."
    )
elif student2_average > student1_average:
    average_winner = student2_name
    average_difference = student2_average - student1_average
    overall_summary = (
        f"{student2_name} outperformed {student1_name} "
        f"by {average_difference:.1f} points."
    )
else:
    average_winner = "The students tied"
    average_difference = 0
    overall_summary = (
        f"{student1_name} and {student2_name} had the same average."
    )

# Find which student had the highest single score overall.
if student1_highest > student2_highest:
    highest_score_result = f"{student1_name} ({student1_highest})"
elif student2_highest > student1_highest:
    highest_score_result = f"{student2_name} ({student2_highest})"
else:
    highest_score_result = (
        f"Both students tied with a score of {student1_highest}"
    )

# Find which student had the lowest single score overall.
if student1_lowest < student2_lowest:
    lowest_score_result = f"{student1_name} ({student1_lowest})"
elif student2_lowest < student1_lowest:
    lowest_score_result = f"{student2_name} ({student2_lowest})"
else:
    lowest_score_result = (
        f"Both students tied with a score of {student1_lowest}"
    )

# Display the comparison results and overall summary.
print(f"Higher average: {average_winner}")
print(f"Difference between averages: {average_difference:.1f} points")
print(f"Highest score overall: {highest_score_result}")
print(f"Lowest score overall:  {lowest_score_result}")
print(f"\nOverall: {overall_summary}")
