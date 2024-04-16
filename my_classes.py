import json

class Person():
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def estimate_max_hr(self):
        if self.sex == "male":
            max_hr_bpm =  223 - 0.9 * self.age
        elif self.sex == "female":
            max_hr_bpm = 226 - 1.0 *  self.age
        else:
            max_hr_bpm  = input("Enter maximum heart rate:")
        return int(max_hr_bpm)
        

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

    
# Erstelle eine Instanz der Person-Klasse
person = Person("Greta", "Angebrand", 23, "female")

# Rufe die save()-Methode der Person-Instanz auf und speichere sie als JSON-Datei
person.save("person.json")

# Erstelle eine Instanz der Experiment-Klasse
experiment = Experiment("My Experiment", "2024-04-16", "Elisabeth Krepper", "Greta Angebrand")

# Rufe die save()-Methode der Experiment-Instanz auf und speichere sie als JSON-Datei
experiment.save("experiment.json")


