import json
from datetime import datetime
import requests

class Person():
    def __init__(self, first_name, last_name=None, birthdate=None, sex=None, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.__birthdate = birthdate  # Geburtsdatum als privates Attribut
        self.sex = sex
        if birthdate and sex:
            self.heart_rate = self.estimate_max_hr()
        else:
            self.heart_rate = None

    def save(self, filename):
        # Nur öffentliche Attribute speichern
        data = {"first_name": self.first_name, "last_name": self.last_name, "sex":self.sex, "heart_rate": self.heart_rate}
        with open(filename, 'w') as file:
            json.dump(data, file)

    def get_age(self):
        if self.__birthdate:
            birth_date = datetime.strptime(self.__birthdate, "%Y-%m-%d")
            today = datetime.today()
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            return age
        else:
            return None

    def estimate_max_hr(self):
        if self.__birthdate and self.sex:
            age = self.get_age()
            if self.sex == "male":
                max_hr_bpm = int(223 - 0.9 * age)
            elif self.sex == "female":
                max_hr_bpm = int(226 - 1.0 * age)
            else:
                max_hr_bpm = int(input("Enter maximum heart rate:"))
            return max_hr_bpm
        else:
            return None
            

    @classmethod
    def put(cls):
        new_name = input("Geben Sie den Namen der neuen Person ein:")
        def add_name_to_json(filename, new_name):
            try:
                # Versuche, die vorhandenen Daten aus der JSON-Datei zu lesen
                with open(filename, 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                # Wenn die Datei nicht vorhanden ist, lege eine leere Liste an
                data = []

            # Füge den neuen Namen zur Liste hinzu
            data.append({"name": new_name})

            # Schreibe die aktualisierten Daten zurück in die JSON-Datei
            with open(filename, 'w') as file:
                json.dump(data, file, indent=2)

        # Erstelle die Person und sende sie an die API
        person = cls(new_name)
        data = {"name": person.first_name}
        data_json = json.dumps(data)
        url = "http://localhost:5000/person/"  # Die URL für das Erstellen einer neuen Person
        try:
            response = requests.post(url, data=data_json)
            if response.status_code == 200:
                print("Person successfully created:", response.json())
            else:
                print("Failed to create person:", response.text)
        except requests.exceptions.RequestException as e:
            print("Error:", e)

Person.put()
   
class Subject(Person):
    def __init__(self, first_name, last_name=None, birthdate=None, sex=None, email=None):
        super().__init__(first_name, last_name, birthdate, sex)
        self.email = email

    def update_email(self, first_name, new_email):
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print("JSON-Datei nicht gefunden.")
            return

        # Suche nach dem Vornamen und aktualisiere die E-Mail-Adresse, falls vorhanden
        updated = False
        for person in data:
            if person.get('name').strip() == first_name.strip():
                if 'email' in person:
                    person['email'] = new_email
                    updated = True

        # Wenn keine Übereinstimmung gefunden wurde, geben wir eine entsprechende Meldung aus
        if not updated:
            print("Kein Eintrag für den angegebenen Namen gefunden oder keine E-Mail-Adresse vorhanden.")

        # Speichere die aktualisierten Daten im JSON-File
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=2)

        # Sende die aktualisierten Daten an den API-Server
        try:
            response = requests.put("http://localhost:5000/person/", json=data)
            if response.status_code == 200:
                print("E-Mail erfolgreich aktualisiert:", response.json())
            else:
                print("Fehler beim Aktualisieren der E-Mail-Adresse auf dem Server:", response.text)
        except requests.exceptions.RequestException as e:
            print("Fehler:", e)

# Benutzereingabe für den Vornamen und die neue E-Mail-Adresse
first_name = input("Enter first name:")
new_email = input("Enter new email:")

# Instanzieren des Subjects und Aufruf der update_email-Methode
subject = Subject(first_name, new_email)
subject.update_email(first_name, new_email)

# Erstelle eine Instanz der Klasse Subject
subject = Subject("Max", "Mustermann", "1990-01-01", "male")


class Examiner(Person):
    def __init__(self, first_name, last_name, ID):
        super().__init__(first_name, last_name)
        self.ID = ID
        

    # Überschreibe die save-Methode, um nur öffentliche Attribute zu speichern
    def save(self, filename):
        data = {"first_name": self.first_name, "last_name": self.last_name, "ID": self.ID}
        with open(filename, 'w') as file:
            json.dump(data, file)

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
subject = Subject("Max", "Mustermann", "1990-01-01", "male")

examiner = Examiner("Maria", "Musterfrau", "123456")

# Speichere die Personen in JSON-Dateien
subject.save("subject.json")
examiner.save("examiner.json")
