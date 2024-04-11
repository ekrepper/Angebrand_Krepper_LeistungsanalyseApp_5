import json
from my_functions import build_experiment, estimate_max_hr, build_person

# gewünschten Input vom User abfragen
def get_user_input():
    first_name_supervisor = input("Enter supervisor's first name: ")
    last_name_supervisor = input("Enter supervisors's last name: ")
    sex_supervisor = input("Enter supervisor's sex (male/female): ")
    age_supervisor = int(input("Enter supervisor's age in years: "))
    first_name_user = input("Enter users's first name: ")
    last_name_user = input("Enter user's last name: ")
    sex_user = input("Enter user's sex (male/female): ")
    age_user = int(input("Enter user's age in years: "))
    experiment_name = input("Enter experiment name: ")
    experiment_date = input("Enter experiment date (e.g., YYYY-MM-DD): ")
    return first_name_supervisor, last_name_supervisor, sex_supervisor, age_supervisor, first_name_user, last_name_user, sex_user, age_user, experiment_name, experiment_date


# Hauptfunktion, welche alle anderen Funktionen aufruft
def main():
    first_name_supervisor, last_name_supervisor,sex_supervisor, age_supervisor, first_name_user, last_name_user, sex_user , age_user, experiment_name, experiment_date = get_user_input()
    max_hr = estimate_max_hr(age_user, sex_user)
    supervisor = build_person(first_name_supervisor, last_name_supervisor, sex_supervisor, age_supervisor)
    subject = build_person(first_name_user, last_name_user, sex_user, age_user)
    experiment = build_experiment(experiment_name, experiment_date, supervisor, subject)
    save_experiment_to_file(experiment)

# Funktion, um das Experiment in eine JSON-Datei zu speichern
def save_experiment_to_file(experiment):
    with open("experiment.json", "w") as outfile:
        json.dump(experiment, outfile, indent=4)

# Main-Funktion aufrufen
if __name__ == "__main__":
    main()
