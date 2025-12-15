# Habita - Habit Tracking App

**Habita** is a solid text-based (CLI) habit tracking application built with Python. Users can define how often they want to repeat tasks - ranging from daily to yearly - as needed. Besides logging progress, it includes tools to review progress and insights of habits over time.


![15 12 2025_14 49 52_REC-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/31db3f4f-fc05-4dfc-90d4-49334df56eee)


The app includes a "Habit Lab" section that gives users a detailed insight about their habits and which ones are succeeding or struggling. Because it lets people set habits, mark then done, and review how far they’ve come, it supports it maintains steady positive routines and feedback loops that are necessary for habits to stick.


![loplo-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/2df24c8b-f3f9-47e8-81ff-991c93fa8706)


## Features

* **Habit Tracking:** Users can create, view habit's list and delete ones they no longer need.
* **Flexible Frequency:** The app supports Daily, Weekly, Monthly and Yearly habitsm this way users can get broad frequency selections.
* **Tracking:** User can track their habits easily by either viewing them or analyzing their streaks explained in the Habit Lab below
  
* **Analytics "Habit Lab":**
    * Get to Calculate longest streaks for any habit and returns winning habit.
    * Get to Identify struggling habits and returns most struggling habit.
    * Plus the option to filter habits by periodicity.
      
* **Data:** All data is autoamtically saved and loaded using a local JSON database file.
* **Predefined Habits:** The app comes with 5 predefined habits examples and 4 weeks of tracking data so users can test the flow of app and get an idea on how it will display and work with their personal habits. 


<img width="883" height="589" alt="image" src="https://github.com/user-attachments/assets/fa3c7cb9-e804-444e-9202-25a3aaef07b9" />

## Technologies

* **Programming language:** Python 3.12
* **Build Architecture:** Object-Oriented Programming (OOP)
* **Data Storage:** JSON
* **Testing:** Unittest framework
* **Modules:** `datetime`, `json`, `os`, `unittest` (Standard Python Libraries)

## How to install

1.  First, make sure that Python 3 is installed on your machine.
```bash
python --version
```
3.  You can either clone the repository or download the zip file of the source code, to clone this repository you run the following command:
```bash
git clone https://github.com/Faroukla99/Habita.git
```
5.  This project is only utilizing standard libraries, so there is no need for any pip or extra ​‍​‌‍​‍‌​‍​‌‍​‍‌installation.

## How to Run the Application

1.  Open your terminal or command prompt.
2.  Navigate to the project directory.
3.  Run the main application file:

```bash
python main.py
