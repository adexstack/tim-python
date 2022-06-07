import csv

input_filename = '../country_info.txt'

dialect = csv.excel # using excel class dialect
dialect.delimiter = '|' # changing the default excel "," delimiter to '|'

countries = {}
with open(input_filename, encoding='utf-8', newline='') as country_file:
    # Get the column headings from the first line of the file
    headings = country_file.readline().strip('\n').split(dialect.delimiter)
    for index, heading in enumerate(headings):
        headings[index] = heading.casefold()

    dict_reader = csv.DictReader(country_file, dialect=dialect, fieldnames=headings)
    for row in dict_reader:
        countries[row['country'].casefold()] = row
        countries[row['cc'].casefold()] = row
print(countries)

while True:
    chosen_country = input("Please enter a country: ")
    country_key = chosen_country.casefold()
    if country_key == "quit":
        break
    elif country_key in countries:
        country_data = countries[country_key]
        print(f"The capital of {chosen_country} is {country_data['capital']}")
    else:
        print("That country does not exist in the list")

