import json
from datetime import datetime

class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def save(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)

# Der Kind-Klasse wird die Elernklasse in Klammern übergeben
class Subject(Person):
    def __init__(self, first_name, last_name, heart_rate, birthdate, sex):
        # Die Funktion super() zeigt Python an, dass die __init__() aus der Elernklasse aufgerufen werden soll
        super().__init__(first_name, last_name)
        # Weitere für die Kindklasse spezielle Attribute können dannach erstellt werden
        self.heart_rate = heart_rate
        # Das Attribut __birth_date ist privat und kann nur innerhalb der Klasse verwendet werden
        self.__birth_date = birthdate
        self.sex = sex

    def estimate_max_hr(self):
        # Berechne das Alter basierend auf dem Geburtsdatum
        age = self._calculate_age()
        if self._sex == "male":
            max_hr_bpm = 223 - 0.9 * age
        elif self._sex == "female":
            max_hr_bpm = 226 - 1.0 * age
        else:
            max_hr_bpm = int(input("Enter maximum heart rate:"))
        return int(max_hr_bpm)

    def _calculate_age(self):
        # Berechne das Alter basierend auf dem Geburtsdatum
        __birth_date = datetime.strptime(self._birth_date, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - __birth_date.year - ((today.month, today.day) < (__birth_date.month, __birth_date.day))
        return age

    def estimate_max_hr(self):
        if self.sex == "male":
            max_hr_bpm =  223 - 0.9 * self._calculate_age
        elif self.sex == "female":
            max_hr_bpm = 226 - 1.0 *  self._calculate_age
        else:
            max_hr_bpm  = input("Enter maximum heart rate:")
        return int(max_hr_bpm)

    
class Examiner(Person):
    def __init__(self, first_name, last_name, ID):
        super().__init__(first_name, last_name)
        self.ID = ID

    def save(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)

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
subject = Subject("Max", "Mustermann", 75, "1990-01-01", "male")
examiner = Examiner("Maria", "Musterfrau", "123456")

# Speichere die Personen in JSON-Dateien
subject.save("subject.json")
examiner.save("examiner.json")


