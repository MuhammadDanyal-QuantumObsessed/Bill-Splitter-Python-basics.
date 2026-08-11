# Bill Splitter
 
A beginner-friendly Python mini-project that calculates how much each person in a group owes after splitting a restaurant bill, including a 25% tip.

This project was built as part of my Python learning journey, with a focus on practicing variables, arithmetic operations, and augmented assignment through a simple, real-world problem.
 
## Table of Contents
* About the Project
* What It Does
* Concepts Practiced
* Code
* Example Output
* How to Run
* Project Structure
* Planned Improvements
* Learning Journey

### About the Project

Ever gone out to eat with friends and had to do awkward mental math to figure out who owes what?

Bill Splitter solves this simple problem using core Python fundamentals.

The program takes the cost of different parts of a meal:

 * Appetizers
 * Main courses
 * Desserts
 * Drinks

It then calculates the total bill, adds a 25% tip, and divides the final amount equally among the group.

##### Note:

The project intentionally uses fixed values to keep the focus on learning fundamental Python syntax.

### What It Does
The program:

  1. Calculates the total meal cost.
  2. Adds a 25% tip.
  3. Calculates the total bill including the tip.
  4. Splits the total evenly among the group.
  5. Rounds the amount to two decimal places.
  6. Displays the results.

### Calculation Flow

Meal Costs

    |
    v

Calculate Total Bill

    |
    v

Add 25% Tip

    |
    v

Calculate Total With Tip

    |
    v

Divide Among Friends

    |
    v

Round to 2 Decimal Places

    |
    v

Amount Per Person

### Concepts Practiced

##### Concept      
#####Application
Variable assignment
Storing meal costs and number of friends
Float arithmetic
Performing dollar-and-cents calculations
Augmented assignment (+=)
Building the running total
round() function
Rounding the final amount
print() formatting
Displaying results clearly
Code
running_total = 0
num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

running_total += appetizers + main_courses + desserts + drinks
print("Total Bill so far:", running_total)

tip = running_total * 0.25
print("Tip amount:", tip)

running_total += tip
print("Total with tip:", running_total)

final_bill = running_total / num_of_friends
print("Bill per person:", final_bill)

each_pays = round(final_bill, 2)
print("Each person pays:", each_pays)
Example Output
Total Bill so far: 198.83
Tip amount: 49.71
Total with tip: 248.54
Bill per person: 62.13
Each person pays: 62.13
How to Run
Prerequisites
Make sure you have Python 3 installed.
Run the Program
python bill_splitter.py
You can also open the project directly in Google Colab or Jupyter Notebook.
Project Structure
bill-splitter/
|
├── bill_splitter.py
└── README.md
Planned Improvements
The current version uses fixed values to keep the focus on core Python syntax.
Future improvements:
[ ] Accept live user input using input()
[ ] Allow users to enter the number of people
[ ] Wrap the calculation logic in reusable functions
[ ] Allow users to choose a custom tip percentage
[ ] Handle edge cases such as zero people and negative amounts
[ ] Add a simple command-line interface (CLI)
[ ] Explore a graphical user interface (GUI)
Learning Journey
This is one of my first hands-on projects while learning Python.
I'm building a portfolio of small, practical projects while developing my programming fundamentals and working toward pursuing a Master's degree in a technical field abroad.
The goal is to gradually progress from simple Python exercises to more complex and useful projects.
Small projects → Strong fundamentals → More complex projects
More projects and more complexity coming soon.