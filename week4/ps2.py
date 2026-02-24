# ** Student Marks Analyzer **

# Problem Statement
# An academic platform stores student performance data in the form of a dictionary.
# Each key in the dictionary represents a student’s name, and the corresponding value is a list of integers representing the marks obtained by that student in different assessments.

# Function Specification
# top_student(records)
# Input:

# A dictionary records where:
# Each key is a string representing a student’s name.
# Each value is a non-empty list of integers representing the marks obtained by that student.

# Output:

# Return the name of the student whose total marks (sum of all marks in their list) is the highest.

# Rules and Clarifications

# The total marks of a student is the sum of all integers in their marks list.
# If multiple students have the same highest total marks, return the student
# who appears first during dictionary traversal.
# You must return the student name.
# Do not print anything inside the function.
# Do not use input() inside the function.
# The function must return a string.

# Example Behaviour 
# {'A':[10,20], 'B':[30]} - A
# {'X':[50,50], 'Y':[40,40,10]} - X
# {'A':[1,1], 'B':[1,1]}  A

# code:

def top_student(records):
    top_name = None
    top_total = -1
    
    for name, marks in records.items():
        total = sum(marks)
        if total > top_total:
            top_total = total
            top_name = name
    
    return top_name
  