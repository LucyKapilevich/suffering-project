import os
import json
import csv

in_path = "Python Group/People"
os.chdir(in_path)

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

                # If there is more than one entry for birthyear or deathyear, skip this entry
                if isinstance(deathyear, list):
                    continue
                if isinstance(birthyear, list):
                    continue
                if not deathyear:
                    continue
                if not birthyear:
                    continue

                try:
                    birthyear = int(birthyear)
                except:
                    TypeError
                try:
                    deathyear = int(deathyear)
                except:
                    TypeError

                if birthyear > 1950:
                    continue
                if birthyear < 0:
                    continue

                # Write data to csv file
                deathcause = person.get('ontology/deathCause_label')
                religion = person.get('ontology/religion_label')
                occupation = person.get('ontology/occupation_label')
                
                lifespan = deathyear - birthyear

                # if isinstance(religion, list):
                #     for rel in religion:
                #         if not any(char in rel for char in '_:.,;-1234567890'):
                #             religion_dict[rel] = {}
                #             religion_dict[religion].append(lifespan)
                # elif isinstance(religion, str):
                #     if not any(char in religion for char in '_:.,;-1234567890'):
                #         religion_dict[religion] = 
                #         religion_dict[religion].append(lifespan)
                # else:
                #     religion = None

                # Creates occupation dictionary to count all occupation entries
                if isinstance(occupation, list):
                    for occ in occupation:
                        if not any(char in occ for char in '_:.,;-1234567890'):
                            if occ not in occupation_dict:
                                occupation_dict[occ] = {"Lifespan": []}
                            occupation_dict[occ]["Lifespan"].append(lifespan)
                elif isinstance(occupation, str):
                    if not any(char in occupation for char in '_:.,;-1234567890'):
                        if occupation not in occupation_dict:
                            occupation_dict[occupation] = {"Lifespan": []}
                        occupation_dict[occupation]["Lifespan"].append(lifespan)

print(occupation_dict)

# Store data in csv file
with open('../occupation_data.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Occupation", "Lifespans"])
    writer.writeheader()
    for occupation, data in occupation_dict.items():
        writer.writerow({"Occupation": occupation, "Lifespans": data["Lifespan"]})