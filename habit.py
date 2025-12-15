from datetime import date

class Habit:

	def __init__(self, name, description, frequency):
		self.name = name
		self.description = description
		self.frequency = frequency
		self.creation_date = date.today().isoformat()
		self.checked_dates = []

	def to_dict(self):
		return {"name": self.name, "description": self.description, "frequency": self.frequency, "creation_date": self.creation_date, "checked_dates": self.checked_dates}