# ** Immutable Course Archive **

# Problem Statement:
# Universities store course records as immutable data to prevent accidental modification.
# You are required to write a Python function as described below.

# 2. course_ends(courses)
# Input:
# A tuple courses containing course names.

# Output:
# Return a tuple containing:
# the first course, and
# the last course.

# Notes:
# If the tuple is empty, return an empty tuple.
# If the tuple contains only one element, return a tuple with that element repeated twice.
# The original tuple must not be modified.

# Important Constraints and Clarifications:
# Do not print anything inside the function.
# Do not use input() inside the function.
# The function must return its result.
# Output must be a tuple.

# code:

def course_ends(courses):
    if len(courses) == 0:
        return ()
    if len(courses) == 1:
        return (courses[0], courses[0])
    return (courses[0], courses[-1])
