
Bill Splitter

"Python" (https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
"Project Status" (https://img.shields.io/badge/Status-Learning%20Project-orange)

A beginner-friendly Python mini-project that calculates how much each person in a group owes after splitting a restaurant bill, including a 25% tip.

This project was built as part of my Python learning journey, with a focus on practicing variables, arithmetic operations, and augmented assignment through a simple, real-world problem.

---

Table of Contents

- "About the Project" (#about-the-project)
- "What It Does" (#what-it-does)
- "Concepts Practiced" (#concepts-practiced)
- "Code" (#code)
- "Example Output" (#example-output)
- "How to Run" (#how-to-run)
- "Project Structure" (#project-structure)
- "Planned Improvements" (#planned-improvements)
- "Learning Journey" (#learning-journey)
- "License" (#license)

---

About the Project

Ever gone out to eat with friends and had to do awkward mental math to figure out who owes what?

Bill Splitter solves this simple problem using core Python fundamentals.

The program takes the cost of different parts of a meal, including:

- Appetizers
- Main courses
- Desserts
- Drinks

It then calculates the total bill, adds a 25% tip, and divides the final amount equally among the group.

The project intentionally uses fixed values to keep the focus on learning fundamental Python syntax.

---

What It Does

The program performs the following steps:

1. Calculates the running total of the meal.
2. Adds a 25% tip.
3. Calculates the total bill including the tip.
4. Splits the total evenly among the group.
5. Rounds the amount to two decimal places.
6. Displays the results at each stage.

Calculation Flow

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

---

Concepts Practiced

Concept| Where It Is Used
Variable assignment| Storing meal costs and number of friends
Float arithmetic| Performing dollar-and-cents calculations
Augmented assignment ("+=")| Building the running total step by step
"round()" function| Rounding the final per-person amount
"print()" formatting| Displaying results clearly

These concepts provide practice with some of the basic building blocks of Python programming.

---

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

---

Example Output

Total Bill so far: 198.83
Tip amount: 49.71
Total with tip: 248.54
Bill per person: 62.13
Each person pays: 62.13

---

How to Run

Prerequisites

Make sure you have Python 3 installed.

Clone the Repository

git clone <your-repository-url>
cd <repository-name>

Run the Program

python bill_splitter.py

You can also open the project directly in Google Colab or Jupyter Notebook.

---

Project Structure

bill-splitter/
│
├── bill_splitter.py
└── README.md

---

Planned Improvements

The current version uses fixed values to keep the focus on core Python syntax.

Future improvements include:

- [ ] Accept live user input using "input()" for meal costs and group size
- [ ] Wrap the calculation logic in reusable functions
- [ ] Allow users to set a custom tip percentage
- [ ] Handle edge cases such as zero people and negative amounts
- [ ] Add a simple command-line interface (CLI)
- [ ] Explore a graphical user interface (GUI)

---

Learning Journey

This is one of my first hands-on projects while learning Python.

I'm building a portfolio of small, practical tools while developing my programming fundamentals and working toward pursuing a Master's degree in a technical field abroad.

The goal is to gradually progress from simple Python exercises to more complex and useful projects.

«Small projects → Strong fundamentals → More complex projects»

More projects and more complexity coming soon.

---

License

This project is currently intended as a learning project.

If an open-source license is added to the repository in the future, this section will be updated accordingly.