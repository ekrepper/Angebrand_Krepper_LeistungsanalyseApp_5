import json
from datetime import datetime

class Person():
    def __init__(self, first_name, last_name, birthdate):
        self.first_name = first_name
        self.last_name = last_name
        self.__birthdate = birthdate

    def save(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)

    def get_age(self):
        birth_date = datetime.strptime(self.__birthdate, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

class Subject(Person):
    def __init__(self, first_name, last_name, birthdate, heart_rate, sex):
        super().__init__(first_name, last_name, birthdate)
        self.heart_rate = heart_rate
        self.sex = sex

    def estimate_max_hr(self):
        age = self.get_age()
        if self.sex == "male":
            max_hr_bpm = 223 - 0.9 * age
        elif self.sex == "female":
            max_hr_bpm = 226 - 1.0 * age
        else:
            max_hr_bpm = int(input("Enter maximum heart rate:"))
        return int(max_hr_bpm)

class Examiner(Person):
    def __init__(self, first_name, last_name, birthdate, ID):
        super().__init__(first_name, last_name, birthdate)
        self.ID = ID

class Experiment():
    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject

    def save(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)

# Beispiel einer Person
subject = Subject("Max", "Mustermann", "1990-01-01", 180, "male")
examiner = Examiner("Maria", "Musterfrau", "1985-05-15", "123456")

# Speichere die Personen in JSON-Dateien
subject.save("subject.json")
examiner.save("examiner.json")
