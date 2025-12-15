# Habita - Habit Tracking App

Habita is a robust, text-based (CLI) habit tracking application developed in Python. It helps users create and track their habits in an efficient and flexible way by allowing multiple frequencies (i.e. Daily to Yearly).

The app features a "Habit Lab" section that gives users detailed insight about their habits and which ones are succeeding or struggling. By allowing them to create habits, track completions, and analyze their progress, it maintains positive routines and feedback loops that are necessary for habits to stick.

## Features

* **Habit Management:** Create, view your list and delete habits you no longer need.
* **Flexible Frequency:** The app supports Daily, Weekly, Monthly and Yearly habits.
* **Tracking:** Add date autoamtically when completing a habit..
* **Analytics "Habit Lab":**
    * Calculate longest streaks for any habit and returns winning habit.
    * Identify struggling habits and returns most struggling habit.
    * Option to filter habits by periodicity.
* **Data Persistence:** All data is autoamtically saved and loaded using a local JSON database.
* **Predefined Data:** The app comes with 5 predefined habits examples and 4 weeks of tracking data for testing and exploration.

## Technologies Used

* **Programming language:** Python 3.12
* **Build Architecture:** Object-Oriented Programming (OOP)
* **Data Storage:** JSON
* **Testing:** Unittest framework
* **Modules:** `datetime`, `json`, `os`, `unittest` (Standard Python Libraries)

## Installation

1.  **First thing:** Make sure that Python 3 is installed on your computer.
2.  **Get the code:** Clone the repository or download the zip file of the source code.
3.  **No Extras Needed:** This project is only utilizing standard libraries, therefore, there is no need for any pip ​‍​‌‍​‍‌​‍​‌‍​‍‌installation.

## How to Run the Application

1.  Open your terminal or command prompt.
2.  Navigate to the project directory.
3.  Run the main application file:

```bash
python main.py
