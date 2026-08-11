
🧾 Bill Splitter


\

«A beginner-friendly Python mini-project that calculates how much each person owes when splitting a restaurant bill, including a 25% tip.»

This project was built as part of my Python learning journey, with a focus on strengthening fundamental programming concepts through a simple, real-world problem.

---

📖 Table of Contents

- "About the Project" (#-about-the-project)
- "What It Does" (#-what-it-does)
- "Concepts Practiced" (#-concepts-practiced)
- "Example" (#-example)
- "How to Run" (#-how-to-run)
- "Project Structure" (#-project-structure)
- "Planned Improvements" (#-planned-improvements)
- "About" (#-about)
- "License" (#-license)

---

 About the Project

Ever gone out to eat with friends and had to do awkward mental math to figure out who owes what?

Bill Splitter solves this simple problem using only core Python fundamentals.

The program takes the cost of different parts of a meal—such as appetizers, main courses, desserts, and drinks—and calculates the amount each person should pay after adding a 25% tip.

The project intentionally uses fixed values to keep the focus on learning Python syntax and fundamental programming concepts.

---

 What It Does

The program:

1. Stores the cost of different parts of a meal.
2. Calculates the total meal cost.
3. Adds a 25% tip.
4. Divides the final bill equally among the group.
5. Rounds the amount to two decimal places.
6. Displays the results at each stage.

Calculation Flow

Meal Costs
    │
    ▼
Calculate Total Bill
    │
    ▼
Add 25% Tip
    │
    ▼
Calculate Total With Tip
    │
    ▼
Divide Among Friends
    │
    ▼
Round to 2 Decimal Places
    │
    ▼
Amount Per Person

---

 Concepts Practiced

Concept| Application
Variable assignment| Storing meal costs and group size
Float arithmetic| Performing dollar-and-cents calculations
Augmented assignment ("+=")| Building the running total
"round()"** function**| Rounding the final amount
"print()"** formatting**| Displaying results clearly

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

📊 Example Output

Total Bill so far: 198.83
Tip amount: 49.71
Total with tip: 248.54
Bill per person: 62.13
Each person pays: 62.13

💰 Final Result

With the values used in this example:

**Each person pays: **"$62.13"

---

🚀 How to Run

Prerequisites

Make sure Python 3.x is installed on your system.

1. Clone the Repository

git clone <your-repository-url>
cd <repository-name>

2. Run the Program

python bill_splitter.py

You can also open and run the code directly in Google Colab or Jupyter Notebook.

---

📁 Project Structure

bill-splitter/
│
├── bill_splitter.ipynb
└── README.md

---

🔭 Planned Improvements

The current version uses fixed values to keep the focus on core Python syntax.

Learning Journey

This is one of my first hands-on Python projects.

I'm building a portfolio of small, practical projects while developing my programming fundamentals and working toward pursuing a Master's degree in a technical field abroad.

The goal is to gradually move from simple Python exercises to more complex and useful projects.

«Small projects → Strong fundamentals → More complex projects»

More projects and more complexity coming soon! 🚀

---
