import os
import json

in_path = "Python Group/People"
os.chdir(in_path)

artist_dict = {}

countries = [
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
    'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh',
    'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina',
    'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 
    'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros',
    'Congo', 'Congo (Democratic Republic)', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic',
    'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea',
    'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia',
    'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti',
    'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy',
    'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait',
    'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania',
    'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania',
    'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique',
    'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria',
    'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru',
    'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis',
    'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia',
    'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands',
    'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland',
    'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago',
    'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom',
    'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen',
    'Zambia', 'Zimbabwe'
]

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

                            # Clean birthplace
                            birthplace_label = person.get('ontology/birthPlace_label')
                            birthplace = 'None'
                            if birthplace_label:
                                for place in birthplace_label:
                                    if place in countries:
                                        birthplace = place
                                        break

                            # Write data to csv file
                            artist_data = (f"{person.get('http://www.w3.org/2000/01/rdf-schema#label')} ,"
                                        f"{person.get('ontology/birthYear_label')} ,"
                                        f"{birthplace} ,"
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