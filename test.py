import json
from my_functions import build_experiment, estimate_max_hr, build_person

# gewünschten Input vom User abfragen
def get_user_input():
    first_name_supervisor = "Max"
    last_name_supervisor = "Mustermann"
    sex_supervisor = "male"
    age_supervisor = 44
    first_name_user = "Pauline"
    last_name_user = "Musterfrau"
    sex_user = "female"
    age_user = 64
    experiment_name = "Experiment 1"
    experiment_date = "2024-04-16"
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