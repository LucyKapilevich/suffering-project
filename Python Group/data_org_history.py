import os
import json
import csv

# Rewrites path, change in_path if you want to change the directory to access your data
in_path = "Python Group/People"
os.chdir(in_path)

# Don't remove this
artist_dict = {}

# Writes a huge list of countries why isn't there an easier solution aaaaaaaaaaaaa
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

people_list = list()

# Open all .json files from pathname
for filename in os.listdir():
    if filename.endswith('.json'): # In case there are rouge .csv files in the directory
        with open(filename, 'r') as jsonfile:
            data = json.load(jsonfile)
            for person in data:

                # Name all my variables so I don't have to write out all of them again aaaaaaaaaaaaa
                name = f"{person.get('http://www.w3.org/2000/01/rdf-schema#label')}"
                birthyear = person.get('ontology/birthYear')
                deathyear = person.get('ontology/deathYear')
                deathcause = person.get('ontology/deathCause_label')
                height = person.get('ontology/height')
                religion = person.get('ontology/religion_label')
                occupation_unit = person.get('ontology/occupation_label') # Different
                deathyear = person.get('ontology/deathYear')
                birthyear = person.get('ontology/birthYear')

                # Clean birthplace to make it specific to a country
                birthplace_label = person.get('ontology/birthPlace_label')
                birthplace = 'NA'
                if birthplace_label:
                    for place in birthplace_label:
                        if place in countries:
                            birthplace = place
                            break # Stop the for loop from sifting through all the countries, improves efficiency

                # Clean award/award number so the data is easier to sift through
                award = person.get('ontology/award_label')
                if isinstance(award, list):
                    award_num = len(award) # Skip this entry if death_year is None or empty
                elif isinstance(award, str):
                    award_num = 1
                else:
                    award_num = 0
                
                # Clean spouse/spouse number so the data is easier to sift through
                spouse = person.get('ontology/spouse')
                if isinstance(spouse, list):
                    spouse_num = len(spouse) # Skip this entry if death_year is None or empty
                elif isinstance(spouse, str):
                    spouse_num = 1
                else:
                    spouse_num = 0

                # If there is more than one entry for birthyear or deathyear, skip this entry
                # I do this so we avoid any weird data entries without an exact date
                if isinstance(deathyear, list):
                    continue
                if isinstance(birthyear, list):
                    continue

                # Take the first death cause/religion to make it easier to sift through the data
                if isinstance(religion, list):
                    religion = religion[0]
                if isinstance(deathcause, list):
                    deathcause = deathcause[0]

                try:
                    birthyear = int(birthyear) # Turn birthyear into integers so it can be processed in R
                except:
                    TypeError # So it doesn't crash
                try:
                    deathyear = int(deathyear) # Turn deathyear into integers so it can be processed in R
                except:
                    TypeError # So it doesn't crash

                occupation = list()

                # Filter occupation
                try:
                    if isinstance(occupation_unit, list):
                        for occ in occupation_unit:
                            if not any(char in occ for char in '_:.,;-1234567890'):
                                occupation.append()
                        else:
                            occupation = 'NA'  # Default value if no valid occupation is found
                    elif isinstance(occupation, str):
                        if any(char in occupation for char in '_:.,;-1234567890'):
                            occupation.append()
                except:
                    TypeError

                # Makes the dict available
                person_dict = {}

                # Write data to csv file so that I can print out each person later
                # I put them all into one dictionary each to make it easier to insert each person per line
                person_dict = {"Name":name,
                               "Birth Year":birthyear,
                               "Birth Place":birthplace,
                               "Death Year":deathyear,
                               "Death Cause":deathcause,
                               "Award Number":award_num,
                               "Religion":religion,
                               "Spouse Number":spouse_num,
                               "Height":height,
                               "Occupation":occupation
                               }
                
                # Rewrites all "None" entries to 'NA' for R analysis
                for key in person_dict:
                    if person_dict[key] == None:
                        person_dict[key] = 'NA'
                people_list.append(person_dict) # Adds the dictionary to a larger list, so it can be written line by line into the .csv file

# Store data in csv file
with open('../history_data.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Birth Year", "Birth Place", "Death Year", "Death Cause", "Award Number", "Religion", "Spouse Number", "Height", "Occupation"])
    writer.writeheader()
    for person in people_list:
        writer.writerow(person)