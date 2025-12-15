from habit import Habit
from datetime import date
import json 

class HabitTracker:

	def __init__(self):
		self.habits = []

	def add_habit(self, name, description, frequency):
		new_habit = Habit(name.capitalize(), description, frequency.lower())
		self.habits.append(new_habit)

	def delete_habit(self, selected_habit):
		targeted_habit = None
		for habit in self.habits:
			if habit.name == selected_habit:
				targeted_habit = habit
				break

		if targeted_habit:
			self.habits.remove(targeted_habit)
			
	def complete_habit(self, selected_habit):
		targeted_habit = None
		for habit in self.habits:
			if habit.name == selected_habit:
				targeted_habit = habit
				break

		if targeted_habit:
			targeted_habit.checked_dates.append(date.today().isoformat())

	def save_to_json(self, filepath):
		with open(filepath, "w") as f:
			data_to_save = []
			for habit in self.habits:
				data_to_save.append(habit.to_dict())
			json.dump(data_to_save, f, indent=2)

	def load_from_json(self, filepath):

		try: 
			with open(filepath, "r") as f:
				data = json.load(f)
				for habit in data:
					loaded_habit = Habit(habit["name"], habit["description"], habit["frequency"])
					loaded_habit.creation_date = habit["creation_date"]
					loaded_habit.checked_dates = habit["checked_dates"]
					self.habits.append(loaded_habit)
		except FileNotFoundError:
			pass

