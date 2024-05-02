# Lesson 4: Assignments | Python Loop Statements
# 1. The Range Riddle
# Objective:
# The aim of this assignment is to deepen your understanding of Python's range() function and its application in loops. You will correct a code snippet, simulate moods for different days, and create a countdown timer.
# Task 1: Your Mood Today
# Write a program that prints off different moods for each day of the week. Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". Using the range() function, loop through the days of the week and for each day, randomly select a mood from the list and print it. Ensure that your program includes the use of the random module to select the mood.
# Example Outcome: An example output could be "On Wednesday, you were feeling happy." "On Thursday you were feeling sad."
moods = ["Happy", "Sad", "Energetic", "Calm"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
import random
for day in days:
    mood = random.choice(moods)
    print(f"For {day}, you were feeling {mood}.")

# 2. Double Scoop with Nested Loops
# Objective:
# The aim of this assignment is to practice using nested loops in Python. You will correct a nested loop code snippet, simulate a mood tracker, and generate a multiplication table.
# Task 1: Your Mood Tracker
# Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week. Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day. For each time, randomly select a mood from a predefined list and print it.
# Example Outcome: An example would be "On Tuesday afternoon you were sad" "On Tuesday night you were happy" "On Wednesday morning you were tired"
moods = ["Happy", "Sad", "Energetic", "Calm", "Tired", "Excited"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
times = ["morning", "afternoon", "evening"]
import random
for day in days:
    for time in times:
        mood = random.choice(moods)
        print(f"On {day} {time} you were {mood}.")