import json
import os

# New path
in_path = "./People"
os.chdir(in_path)

artist_dict = {}

# Open all .json files from pathname
for filename in os.listdir():
    if filename.endswith('.json'):
        with open(filename, 'r') as file:
            data = json.load(file)
            for person in data:
                for entry in person["http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label"]:
                    if entry == 'musical artist':
                        name = person["title"]
                        artist_dict[name] = person

# Revert path
in_path = ".."
os.chdir(in_path)

# Store artists in csv file
with open('musician_data.csv', 'w', encoding='utf-8') as file:
    file.write(str(artist_dict))
