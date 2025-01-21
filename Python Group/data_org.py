import os
import json

in_path = "Python Group/People"
os.chdir(in_path)

artist_dict = {}

# Store artists in csv file
with open('../musician_data.csv', 'w', encoding='utf-8',) as file:
    file.write('Name, Birthyear, Nationality, Deathyear, Award, Instrument, Training, Height, Field, Background, associatedBand, Genre\n')

    # Open all .json files from pathname
    for filename in os.listdir():
        if filename.endswith('.json'):
            with open(filename, 'r') as jsonfile:
                data = json.load(jsonfile)
                for person in data:
                    for entry in person["http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label"]:
                        if entry == 'musical artist':

                            # Clean genre
                            genre = person.get('ontology/genre_label')
                            genre = str(genre)
                            genre = genre.strip('[]')
                            genre = genre.replace(',', '|')

                            # Clean instrument
                            instrument = person.get('ontology/instrument_label')
                            instrument = str(instrument)
                            instrument = instrument.strip('[]')
                            instrument = instrument.replace(',', '|')

                            # Clean band
                            band = person.get('ontology/associatedBand_label')
                            band = str(band)
                            band = band.strip('[]')
                            band = band.replace(',', '|')

                            # # Clean birthplace
                            # birthplace = person.get('ontology/birthPlace_label')
                            # for country in 

                            # Write data to csv file
                            artist_data = (f"{person.get('http://www.w3.org/2000/01/rdf-schema#label')} ,"
                                        f"{person.get('ontology/birthYear_label')} ,"
                                        f"{person.get('ontology/nationality_label')} ,"
                                        f"{person.get('ontology/deathYear_label')} ,"
                                        f"{person.get('ontology/award_label')} ,"
                                        f"{instrument} ,"
                                        f"{person.get('ontology/training_label')} ,"
                                        f"{person.get('ontology/height')} ,"
                                        f"{person.get('ontology/field_label')} ,"
                                        f"{person.get('ontology/background')} ,"
                                        f"{band} ,"
                                        f"{genre} \n")
                            file.write(artist_data)