import os
import json
import csv

# Rewrites path, change in_path if you want to change the directory to access your data
in_path = "Python Group/People"
os.chdir(in_path)

# Makes all necessary dictionaries we'll use, add as needed
occupation_dict = {}
religion_dict = {}
deathcause_dict = {}

# Open all .json files from pathname
for filename in os.listdir():
    if filename.endswith('.json'):
        with open(filename, 'r') as jsonfile:
            data = json.load(jsonfile)
            for person in data:
                
                birthyear = person.get('ontology/birthYear')
                deathyear = person.get('ontology/deathYear')

                # If there is more than one entry for birthyear or deathyear, skip this entry, otherwise it causes a crash
                if isinstance(deathyear, list):
                    continue
                if isinstance(birthyear, list):
                    continue

                # If entry doesn't exist, skip this entry, otherwise it causes a crash
                if not deathyear:
                    continue
                if not birthyear:
                    continue

                try:
                    birthyear = int(birthyear)
                except:
                    TypeError # Makes sure it doesn't crash
                try:
                    deathyear = int(deathyear)
                except:
                    TypeError # Makes sure it doesn't crash

                # Takes out everyone born before 0 and after 1950
                if birthyear > 1950:
                    continue
                if birthyear < 0:
                    continue

                # Store all the variables for processing
                deathcause = person.get('ontology/deathCause_label')
                religion = person.get('ontology/religion_label')
                occupation = person.get('ontology/occupation_label')
                
                # It's easier to store lifespan rather than deathyear or birthyear
                lifespan = deathyear - birthyear

                # Creates occupation dictionary to count all occupation entries
                if isinstance(occupation, list):
                    for occ in occupation:
                        if not any(char in occ for char in '_:.,;-1234567890'): # So artefacts don't enter our data
                            if occ not in occupation_dict:
                                occupation_dict[occ] = {"Lifespan": []} # Creates new dictionary if it isn't already available
                            occupation_dict[occ]["Lifespan"].append(lifespan)
                elif isinstance(occupation, str):
                    if not any(char in occupation for char in '_:.,;-1234567890'): # So artefacts don't enter our data
                        if occupation not in occupation_dict:
                            occupation_dict[occupation] = {"Lifespan": []} # Creates new dictionary if it isn't already available
                        occupation_dict[occupation]["Lifespan"].append(lifespan)

                # Creates religion dictionary to count all religion entries
                if isinstance(religion, list):
                    for rel in religion:
                        if not any(char in rel for char in '_:.,;-1234567890'): # So artefacts don't enter our data
                            if rel not in religion_dict:
                                religion_dict[rel] = {"Lifespan": []} # Creates new dictionary if it isn't already available
                            religion_dict[rel]["Lifespan"].append(lifespan)
                elif isinstance(religion, str):
                    if not any(char in religion for char in '_:.,;-1234567890'): # So artefacts don't enter our data
                        if religion not in religion_dict:
                            religion_dict[religion] = {"Lifespan": []} # Creates new dictionary if it isn't already available
                        religion_dict[religion]["Lifespan"].append(lifespan)
                                # Creates religion dictionary to count all religion entries

                # Creates deathcause dictionary to count all deathcause entries
                if isinstance(deathcause, list):
                    for rel in deathcause:
                        if not any(char in rel for char in '_:.,;-1234567890'): # So artefacts don't enter our data
                            if rel not in deathcause_dict:
                                deathcause_dict[rel] = {"Lifespan": []} # Creates new dictionary if it isn't already available
                            deathcause_dict[rel]["Lifespan"].append(lifespan)
                elif isinstance(deathcause, str):
                    if not any(char in deathcause for char in '_:.,;-1234567890'): # So artefacts don't enter our data
                        if deathcause not in deathcause_dict:
                            deathcause_dict[deathcause] = {"Lifespan": []} # Creates new dictionary if it isn't already available
                        deathcause_dict[deathcause]["Lifespan"].append(lifespan)

# Store occupation in csv file
with open('../occupation_data.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Occupation", "Lifespans"])
    writer.writeheader()
    for occupation, data in occupation_dict.items():
        writer.writerow({"Occupation": occupation, "Lifespans": data["Lifespan"]})

# Store religion in csv file
with open('../religion_data.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Occupation", "Lifespans"])
    writer.writeheader()
    for religion, data in religion_dict.items():
        writer.writerow({"Occupation": religion, "Lifespans": data["Lifespan"]})

# Store deathcause in csv file
with open('../deathcause_data.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Occupation", "Lifespans"])
    writer.writeheader()
    for deathcause, data in deathcause_dict.items():
        writer.writerow({"Occupation": deathcause, "Lifespans": data["Lifespan"]})