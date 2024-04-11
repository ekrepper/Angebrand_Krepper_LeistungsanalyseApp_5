import json
from my_functions import build_experiment, estimate_max_hr, build_person

def get_user_input():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    sex = input("Enter sex (male/female): ")
    age = int(input("Enter age in years: "))
    experiment_name = input("Enter experiment name: ")
    date = input("Enter date (e.g., YYYY-MM-DD): ")
    return first_name, last_name, sex, age, experiment_name, date

def main():
    first_name, last_name, sex, age, experiment_name, date = get_user_input()
    max_hr = estimate_max_hr(age, sex)
    supervisor = build_person(first_name, last_name, sex, age)  
    subject = build_person(first_name, last_name, sex, age)
    experiment = build_experiment(experiment_name, date, supervisor, subject)
    save_experiment_to_file(experiment)

def save_experiment_to_file(experiment):
    with open("experiment.json", "w") as outfile:
        json.dump(experiment, outfile, indent=4)

if __name__ == "__main__":
    main()
