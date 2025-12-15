import unittest
from datetime import date
from habit import Habit
from tracker import HabitTracker
import analytics
import os


class TestHabitApp(unittest.TestCase):
    # ---- Habit Class ----
    def test_habit(self):
        habit_to_test = Habit('Reading', 'Read 10 Pages a day', 'Daily')
        self.assertEqual(habit_to_test.name, 'Reading')
        self.assertEqual(habit_to_test.description, 'Read 10 Pages a day')
        self.assertEqual(habit_to_test.frequency, 'Daily')
        self.assertEqual(habit_to_test.creation_date, date.today().isoformat())
        self.assertEqual(habit_to_test.checked_dates, [])

    # ---- HabitTracker Class ----
    def test_add_habit(self):
        manager_test = HabitTracker()
        manager_test.add_habit('Studying', 'Study 1 chapter', 'Daily')

        self.assertEqual(manager_test.habits[0].name, 'Studying')
        self.assertEqual(manager_test.habits[0].description, 'Study 1 chapter')
        self.assertEqual(manager_test.habits[0].frequency, 'daily')
        self.assertEqual(manager_test.habits[0].creation_date, date.today().isoformat())
        self.assertEqual(manager_test.habits[0].checked_dates, [])
    # --------
    def test_complete_habit(self):
        manager_test = HabitTracker()
        manager_test.add_habit('Gym', 'Lift weight in the gym', 'Weekly')

        manager_test.complete_habit('Gym')
        self.assertEqual(manager_test.habits[0].checked_dates, [date.today().isoformat()])
    # --------
    def test_delete_habit(self):
        manager_test = HabitTracker()
        manager_test.add_habit('Monitor finances', 'Monitor and calculate your spending and bills', 'monthly')

        self.assertEqual(manager_test.habits[0].name, 'Monitor finances')
        
        manager_test.delete_habit('Monitor finances')
        self.assertEqual(manager_test.habits, [])
    # --------
    def test_save_and_load_json(self):
        try:
            manager_test = HabitTracker()
            manager_test.add_habit('Cycling', 'Run 60km', 'Weekly')
            manager_test.habits[0].checked_dates = ['2025-10-09', '2025-10-16']
            temporary_json_file = "temporary.json"

            manager_test.save_to_json(temporary_json_file)

            new_manager_test = HabitTracker()
            new_manager_test.load_from_json(temporary_json_file)

            self.assertEqual(len(new_manager_test.habits), 1)
            self.assertEqual(new_manager_test.habits[0].name, 'Cycling')
            self.assertEqual(new_manager_test.habits[0].description, 'Run 60km')
            self.assertEqual(new_manager_test.habits[0].frequency, 'weekly')
            self.assertEqual(new_manager_test.habits[0].checked_dates, ['2025-10-09', '2025-10-16'])
        finally:
            os.remove(temporary_json_file)

    # ---- Analytics Functions ----
    def test_get_all_habits(self):

        manager_test = HabitTracker()
        manager_test.add_habit('Cooking', 'Cook a new meal', 'Weekly')
        manager_test.add_habit('Drinking water', 'Drink 3 liters of water', 'Daily')
        list_of_habits = analytics.get_all_habits(manager_test.habits)

        # Habit 1
        self.assertEqual(list_of_habits[0].name, 'Cooking')
        self.assertEqual(list_of_habits[0].description, 'Cook a new meal')
        self.assertEqual(list_of_habits[0].frequency, 'weekly')
        self.assertEqual(list_of_habits[0].creation_date, date.today().isoformat())
        self.assertEqual(list_of_habits[0].checked_dates, [])
        # Habit 2
        self.assertEqual(list_of_habits[1].name, 'Drinking water')
        self.assertEqual(list_of_habits[1].description, 'Drink 3 liters of water')
        self.assertEqual(list_of_habits[1].frequency, 'daily')
        self.assertEqual(list_of_habits[1].creation_date, date.today().isoformat())
        self.assertEqual(list_of_habits[1].checked_dates, [])
    # --------
    def test_get_all_habits_by_frequency(self):
        
        manager_test = HabitTracker()
        manager_test.add_habit('Drawing', 'Draw one flower', 'Daily')
        manager_test.add_habit('Running', 'Run 10 km', 'Weekly')
        manager_test.add_habit('Travel', 'Travel to a new city', 'Monthly')
        manager_test.add_habit('Family picture', 'Take a family picture at my parent\'s house', 'Yearly')

        list_of_habits = analytics.get_all_habits_by_frequency(manager_test.habits, 'daily')
        self.assertEqual(len(list_of_habits), 1)
        self.assertEqual(list_of_habits[0].name, 'Drawing')
        

        list_of_habits = analytics.get_all_habits_by_frequency(manager_test.habits, 'weekly')
        self.assertEqual(len(list_of_habits), 1)
        self.assertEqual(list_of_habits[0].name, 'Running')

        list_of_habits = analytics.get_all_habits_by_frequency(manager_test.habits, 'monthly')
        self.assertEqual(len(list_of_habits), 1)
        self.assertEqual(list_of_habits[0].name, 'Travel')

        list_of_habits = analytics.get_all_habits_by_frequency(manager_test.habits, 'yearly')
        self.assertEqual(len(list_of_habits), 1)
        self.assertEqual(list_of_habits[0].name, 'Family picture')
    # --------
    def test_longest_streak_all_habits(self):
        
        manager_test = HabitTracker()
        # Daily
        manager_test.add_habit('Drawing', 'Draw one flower', 'Daily')
        manager_test.add_habit('Eating more protein', 'Eat at least 100g protein a day', 'Daily')
        manager_test.habits[0].checked_dates = ['2025-10-01', '2025-10-02', '2025-10-03', '2025-10-05']
        manager_test.habits[1].checked_dates = ['2025-10-01', '2025-10-02', '2025-10-03', '2025-10-04']

        streaks = analytics.get_longest_streak_habits(manager_test.habits, 'daily')
        self.assertEqual(streaks[0], {'Drawing':3, 'Eating more protein':4})
        self.assertEqual(streaks[1], {'Eating more protein':4})

        # Weekly
        manager_test.add_habit('Running', 'Run 10 km', 'Weekly')
        manager_test.add_habit('Visiting my parents', 'Visit my parents every sunday', 'Weekly')
        manager_test.habits[2].checked_dates = ['2025-11-01', '2025-11-08', '2025-11-17', '2025-11-26']
        manager_test.habits[3].checked_dates = ['2025-11-01', '2025-11-08', '2025-11-15', '2025-11-22']

        streaks = analytics.get_longest_streak_habits(manager_test.habits, 'weekly')
        self.assertEqual(streaks[0], {'Running':2, 'Visiting my parents':4})
        self.assertEqual(streaks[1], {'Visiting my parents':4})

        # Monthly
        manager_test.add_habit('Finances reporting', 'Make a report of the monthly finances status', 'Monthly')
        manager_test.add_habit('Traveling', 'Travel to a new city', 'Monthly')
        manager_test.habits[4].checked_dates = ['2023-07-01', '2023-08-01', '2023-09-01', '2023-10-01']
        manager_test.habits[5].checked_dates = ['2024-09-05', '2024-11-05', '2024-12-05', '2025-01-05']

        streaks = analytics.get_longest_streak_habits(manager_test.habits, 'monthly')
        self.assertEqual(streaks[0], {'Finances reporting':4, 'Traveling':3})
        self.assertEqual(streaks[1], {'Finances reporting':4})

        # Yearly
        manager_test.add_habit('Renovation', 'Renovate the house', 'Yearly')
        manager_test.add_habit('Family picture', 'Take a family picture at my parent\'s house', 'Yearly')
        manager_test.habits[6].checked_dates = ['2009-11-01', '2010-11-01', '2011-11-01', '2012-11-26']
        manager_test.habits[7].checked_dates = ['2001-11-01', '2002-11-08', '2003-11-15', '2004-11-22', '2005-11-08','2006-11-08']

        streaks = analytics.get_longest_streak_habits(manager_test.habits, 'yearly')
        self.assertEqual(streaks[0], {'Renovation':4, 'Family picture':6})
        self.assertEqual(streaks[1], {'Family picture':6})
    # --------
    def test_get_struggling_habit(self):
        
        # Daily
        manager_test = HabitTracker()
        manager_test.add_habit('Practicing latte art', 'Draw two heart every day', 'Daily')
        manager_test.add_habit('Walking', 'walk 10000 steps a day', 'Daily')
        manager_test.habits[0].checked_dates = ['2025-10-01', '2025-10-02', '2025-10-04', '2025-10-05', '2025-10-08', '2025-10-09', '2025-10-11']
        manager_test.habits[1].checked_dates = ['2025-10-01', '2025-10-02', '2025-10-03', '2025-10-04', '2025-10-06']

        breaks = analytics.get_longest_break_habits(manager_test.habits, 'daily')
        self.assertEqual(breaks[0], {'Practicing latte art':3, 'Walking':1})
        self.assertEqual(breaks[1], {'Practicing latte art':3})

        # Weekly
        manager_test.add_habit('Running', 'Run 10 km', 'Weekly')
        manager_test.add_habit('Visiting my parents', 'Visit my parents every sunday', 'Weekly')
        manager_test.habits[2].checked_dates = ['2025-11-01', '2025-11-08', '2025-11-17', '2025-11-24','2025-12-03']
        manager_test.habits[3].checked_dates = ['2025-11-01', '2025-11-08', '2025-11-15', '2025-11-22' ,'2025-11-29', '2025-12-07']
        
        breaks = analytics.get_longest_break_habits(manager_test.habits, 'weekly')
        self.assertEqual(breaks[0], {'Running':2, 'Visiting my parents':1})
        self.assertEqual(breaks[1], {'Running':2})

        # Monthly
        manager_test.add_habit('Finances reporting', 'Make a report of the monthly finances status', 'Monthly')
        manager_test.add_habit('Traveling', 'Travel to a new city', 'Monthly')
        manager_test.habits[4].checked_dates = ['2023-07-01', '2023-08-01', '2023-10-01', '2023-11-01', '2023-12-15']
        manager_test.habits[5].checked_dates = ['2024-09-05', '2024-11-05', '2024-12-05', '2025-01-05']

        breaks = analytics.get_longest_break_habits(manager_test.habits, 'monthly')
        self.assertEqual(breaks[0], {'Finances reporting':2, 'Traveling':1})
        self.assertEqual(breaks[1], {'Finances reporting':2})

        # Yearly
        manager_test.add_habit('Renovation', 'Renovate the house', 'Yearly')
        manager_test.add_habit('Family picture', 'Take a family picture at my parent\'s house', 'Yearly')
        manager_test.habits[6].checked_dates = ['2009-11-01', '2011-11-01', '2012-11-01', '2014-12-26']
        manager_test.habits[7].checked_dates = ['2001-11-01', '2002-11-08', '2003-11-15', '2004-11-22', '2006-11-08','2007-11-08']

        breaks = analytics.get_longest_break_habits(manager_test.habits, 'yearly')
        self.assertEqual(breaks[0], {'Renovation':2, 'Family picture':1})
        self.assertEqual(breaks[1], {'Renovation':2})


if __name__ == '__main__':
    unittest.main()
