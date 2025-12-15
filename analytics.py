from datetime import datetime, timedelta

def get_all_habits(habits):
	"""
    Retrieves a list of all habit objects from the provided iterable.
    Args: 
		habits (iterable): An iterable containing Habit objects.
    Returns: 
		list: A list containing all the Habit objects.
    """

	list_of_habits = [habit for habit in habits]
	return list_of_habits

def get_all_habits_by_frequency(habits, frequency):
	"""
    Filters and returns a list of habits that match a specific frequency.

    Args:
        habits (iterable): An iterable containing Habit objects.
        frequency (str): The target frequency to filter by (e.g., 'daily', 'weekly').

    Returns:
        list: A list of Habit objects that match the specified frequency.
    """

	list_of_habits = []
	for habit in habits:
		if habit.frequency == frequency:
			list_of_habits.append(habit)

	return list_of_habits

def get_longest_streak_habits(habits, frequency):
	"""
    Calculates the longest streak of consecutive completions for habits of a specific frequency.
    
    This function analyzes the 'checked_dates' of each habit to determine the maximum
    number of consecutive periods (days, weeks, months, or years) the habit was performed.

    Args:
        habits (iterable): An iterable containing Habit objects.
        frequency (str): The frequency category to analyze (e.g., 'daily', 'weekly', 'monthly', 'yearly').

    Returns:
        tuple: A tuple containing two dictionaries:
            - habit_streak (dict): A mapping of {habit_name: longest_streak_count} for all habits.
            - biggest_streak_habit (dict): A mapping of {habit_name: longest_streak_count} for 
              the habit(s) with the highest streak overall.
    """


	habits_by_frequency = get_all_habits_by_frequency(habits, frequency)
	frequency_check = None

	if frequency == "daily":
		frequency_check = timedelta(days=1)
	elif frequency == "weekly":
		frequency_check = timedelta(weeks=1)

	habit_streak = {}

	for habit in habits_by_frequency:
		# Default streaks value
		streak = 1
		longest_streak = 0

		if habit.checked_dates:

			# -----------
			# 1 checked date 
			if len(habit.checked_dates) == 1:
				longest_streak = 1
				
			# -----------
			# Handles Daily and Weekly streaks
			elif frequency_check:
				for date in range(len(habit.checked_dates)-1):
					if datetime.fromisoformat(habit.checked_dates[date+1]) - datetime.fromisoformat(habit.checked_dates[date]) == frequency_check:
						streak += 1
					else:
						streak = 1

					if 	streak > longest_streak:
						longest_streak = streak
			
			# -----------
			# Handles Monthly streaks
			elif frequency.lower() == "monthly":
				for date in range(len(habit.checked_dates)-1):

					# New Year scenario
					if datetime.fromisoformat(habit.checked_dates[date+1]).year == datetime.fromisoformat(habit.checked_dates[date]).year + 1 and (datetime.fromisoformat(habit.checked_dates[date]).month == 12 and datetime.fromisoformat(habit.checked_dates[date+1]).month == 1):

						# 31 days monthly streak deadline
						if 0 < (datetime.fromisoformat(habit.checked_dates[date+1]) - datetime.fromisoformat(habit.checked_dates[date])).days <= 31:
							streak += 1

					# Months in the year
					elif datetime.fromisoformat(habit.checked_dates[date+1]).year == datetime.fromisoformat(habit.checked_dates[date]).year and datetime.fromisoformat(habit.checked_dates[date+1]).month == datetime.fromisoformat(habit.checked_dates[date]).month + 1:

						# 31 days monthly streak deadline
						if 0 < (datetime.fromisoformat(habit.checked_dates[date+1]) - datetime.fromisoformat(habit.checked_dates[date])).days <= 31:
							streak += 1

					else:
						streak = 1

					if 	streak > longest_streak:
						longest_streak = streak
			
			# -----------
			# Handles Yearly streaks
			elif frequency.lower() == "yearly":
				for date in range(len(habit.checked_dates)-1):

					# Next Year same month
					if datetime.fromisoformat(habit.checked_dates[date+1]).year == datetime.fromisoformat(habit.checked_dates[date]).year + 1 and datetime.fromisoformat(habit.checked_dates[date+1]).month == datetime.fromisoformat(habit.checked_dates[date]).month:
						streak += 1
					else:
						streak = 1

					if 	streak > longest_streak:
						longest_streak = streak

		# Each habit and its longest number of streaks
		habit_streak[habit.name] = longest_streak

	biggest_streak = 0
	biggest_streak_habit = {}

	# Checks for the biggest streak habit
	for habit, value in habit_streak.items():
		if value > biggest_streak:
			biggest_streak = value

	# The habit with the biggest streak value, can insert more than 1 if other habits have similar streak numbers
	for habit, value in habit_streak.items():
		if value == biggest_streak:
			biggest_streak_habit.update({habit: value})


	return habit_streak, biggest_streak_habit

def get_longest_break_habits(habits, frequency):
	"""
    Calculates the total number of breaks for habits of a specific frequency.

    This function iterates through the 'checked_dates' to count how many times the user 
    failed to maintain the habit continuity based on the specified frequency constraints.

    Args:
        habits (iterable): An iterable containing Habit objects.
        frequency (str): The frequency category to analyze (e.g., 'daily', 'weekly', 'monthly', 'yearly').

    Returns:
        tuple: A tuple containing two dictionaries:
            - habit_report (dict): A dictionary {habit_name: total_break_count} for all habits.
            - biggest_breaks_habit (dict): A dictionary {habit_name: total_break_count} for 
              the habit(s) with the highest number of breaks overall.
    """

	habits_by_frequency = get_all_habits_by_frequency(habits, frequency)
	frequency_check = None

	if frequency == "daily":
		frequency_check = timedelta(days=1)
	elif frequency == "weekly":
		frequency_check = timedelta(weeks=1)

	habit_report = {}

	for habit in habits_by_frequency:

		# Default breaks value
		breaks = 0
		
		if habit.checked_dates:

			# -----------
			# Handles Daily and Weekly breaks
			if frequency_check:
				for date in range(len(habit.checked_dates)-1):
					if datetime.fromisoformat(habit.checked_dates[date+1]) - datetime.fromisoformat(habit.checked_dates[date]) > frequency_check:
						breaks += 1

			# -----------
			# Handles Monthly breaks
			elif frequency == "monthly":
				for date in range(len(habit.checked_dates)-1):

					# New Year 
					if datetime.fromisoformat(habit.checked_dates[date+1]).year == datetime.fromisoformat(habit.checked_dates[date]).year + 1 and (datetime.fromisoformat(habit.checked_dates[date]).month == 12 and datetime.fromisoformat(habit.checked_dates[date+1]).month > 1): 
						breaks += 1
					
					# More than one month
					elif datetime.fromisoformat(habit.checked_dates[date+1]).year == datetime.fromisoformat(habit.checked_dates[date]).year and datetime.fromisoformat(habit.checked_dates[date+1]).month > datetime.fromisoformat(habit.checked_dates[date]).month + 1:
						breaks += 1

					# New year but more than 31 days (e.g. 10 Dec - 20 Jan)
					elif datetime.fromisoformat(habit.checked_dates[date+1]).year == datetime.fromisoformat(habit.checked_dates[date]).year + 1 and (datetime.fromisoformat(habit.checked_dates[date]).month == 12 and datetime.fromisoformat(habit.checked_dates[date+1]).month == 1): 
						# 31 days check
						if (datetime.fromisoformat(habit.checked_dates[date+1]) - datetime.fromisoformat(habit.checked_dates[date])).days > 31:
							breaks += 1

					# Same year 1 month ahead but more than 31 days (e.g. 01 Jan - 19 Feb)
					elif datetime.fromisoformat(habit.checked_dates[date+1]).year == datetime.fromisoformat(habit.checked_dates[date]).year and datetime.fromisoformat(habit.checked_dates[date+1]).month == datetime.fromisoformat(habit.checked_dates[date]).month + 1:
						# 31 days check
						if (datetime.fromisoformat(habit.checked_dates[date+1]) - datetime.fromisoformat(habit.checked_dates[date])).days > 31:
							breaks += 1
				
			# -----------
			# handles Yearly breaks
			elif frequency == "yearly":
				for date in range(len(habit.checked_dates)-1):

					# More than one year
					if datetime.fromisoformat(habit.checked_dates[date+1]).year > datetime.fromisoformat(habit.checked_dates[date]).year + 1:
						breaks += 1

					# One year difference but more than 12 months 
					elif datetime.fromisoformat(habit.checked_dates[date+1]).year == datetime.fromisoformat(habit.checked_dates[date]).year + 1 and datetime.fromisoformat(habit.checked_dates[date+1]).month > datetime.fromisoformat(habit.checked_dates[date]).month + 1:
						breaks += 1
					

		# Each habit and its longest number of breaks
		habit_report[habit.name] = 	breaks

	biggest_breaks = 0
	biggest_breaks_habit = {}

	# Checks for the biggest break habit	
	for habit, value in habit_report.items():
		if value > biggest_breaks:
			biggest_breaks = value

	# The habit with the biggest break value, can insert more than 1 if other habits have similar break numbers
	for habit, value in habit_report.items():
		if value == biggest_breaks:
			biggest_breaks_habit.update({habit: value})

	return habit_report, biggest_breaks_habit