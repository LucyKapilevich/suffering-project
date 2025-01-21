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
with open('../history_data.csv', 'w', encoding='utf-8',) as file:
    file.write('Name, Birthyear, Birthplace, Deathyear, Deathcause, awardNumber, Height, Religion, spouseNumber\n')

    # Open all .json files from pathname
    for filename in os.listdir():
        if filename.endswith('.json'):
            with open(filename, 'r') as jsonfile:
                data = json.load(jsonfile)
                for person in data:

                    # Check if death year exists
                    deathyear = person.get('ontology/deathYear')
                    if not deathyear:
                        continue  # Skip this entry if death_year is None or empty

                    # Check if birth year exists
                    birthyear = person.get('ontology/birthYear')
                    if not birthyear:
                        continue  # Skip this entry if death_year is None or empty

                    # Clean birthplace
                    birthplace_label = person.get('ontology/birthPlace_label')
                    birthplace = 'NA'
                    if birthplace_label:
                        for place in birthplace_label:
                            if place in countries:
                                birthplace = place
                                break
                    
                    # Clean award/award number
                    award = person.get('ontology/award_label')
                    if award == None:
                        award_num = 'NA'  # Award is empty if no award
                    else:
                        award_num = len(award)

                    # Clean spouse/spouse number
                    spouse = person.get('ontology/spouse')
                    if spouse == None:
                        spouse_num = 'NA'  # Skip this entry if death_year is None or empty
                    else:
                        spouse_num = len(spouse)

                    # Write data to csv file
                    name = f"{person.get('http://www.w3.org/2000/01/rdf-schema#label')}"
                    birthyear = person.get('ontology/birthYear')
                    deathyear = person.get('ontology/deathYear')
                    deathcause = person.get('ontology/deathCause_label')
                    height = person.get('ontology/height')
                    religion = person.get('ontology/religion_label')
                    occupation = person.get('ontology/occupation_label')

                    # If there is more than one entry for birthyear or deathyear, skip this entry
                    if isinstance(deathyear, list):
                        deathyear = deathyear[0]
                    if isinstance(birthyear, list):
                        birthyear = birthyear[0]
                    if isinstance(religion, list):
                        religion = religion[0]
                    if isinstance(deathcause, list):
                        deathcause = deathcause[0]
                    if isinstance(occupation, list):
                        occupation = occupation[0]

                    # Write data to csv file
                    file.write((f"{name}, {int(birthyear)}, {birthplace}, {int(deathyear)}, {deathcause}, {award_num}, {height}, {religion}, {spouse_num}\n").replace('None', 'NA'))