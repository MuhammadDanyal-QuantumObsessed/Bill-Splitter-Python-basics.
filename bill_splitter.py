
Bill Splitter

A beginner Python project that calculates how much each person owes
after splitting a group restaurant bill, including tip.

Concepts practiced:
- Variable assignment
- Float arithmetic
- Augmented assignment (+=)
- round()

# Running total starts at 0 — we'll build up the bill step by step
running_total = 0

# Number of people splitting the bill
num_of_friends = 4

# Cost of each course of the meal (in dollars)
appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

# Add all courses to the running total
running_total += appetizers + main_courses + desserts + drinks
print("Total Bill so far:", running_total)

# Calculate a 25% tip based on the total so far
tip = running_total * 0.25
print("Tip amount:", tip)

# Add the tip to the running total
running_total += tip
print("Total with tip:", running_total)

# Split the total evenly among all friends
final_bill = running_total / num_of_friends
print("Bill per person:", final_bill)

# Round the final amount to 2 decimal places (cents)
each_pays = round(final_bill, 2)
print("Each person pays:", each_pays)
