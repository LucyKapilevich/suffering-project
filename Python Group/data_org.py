import os
import json

in_path = "Python Group/People"
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
    file.write('Name, Birthyear, Deathyear, birthDate, deathDate, Award, Instrument, Training, Height, Field, Background, associatedBand, Genre\n')
    for artist in artist_dict.values():
        artist_data = (f"{artist.get('http://www.w3.org/2000/01/rdf-schema#label')} ,"
                       f"{artist.get('ontology/birthYear')} ,"
                       f"{artist.get('ontology/deathYear')} ,"
                       f"{artist.get('ontology/birthDate')} ,"
                       f"{artist.get('ontology/deathDate')} ,"
                       f"{artist.get('ontology/award_label')} ,"
                       f"{artist.get('ontology/instrument_label')} ,"
                       f"{artist.get('ontology/training_label')} ,"
                       f"{artist.get('ontology/height')} ,"
                       f"{artist.get('ontology/field_label')} ,"
                       f"{artist.get('ontology/background')} ,"
                       f"{artist.get('ontology/associatedBand_label')} ,"
                       f"{artist.get('ontology/genre_label')} \n")
        file.write(artist_data)