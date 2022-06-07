input_filename = 'country_info.txt'

countries = {}
with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
        print(country_dict)
        countries[country.casefold()] = country_dict
        countries[code.casefold()] = country_dict

print(countries)

while True:
    chosen_country = input("Please enter a country: ")
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_capital = countries[country_key]["capital"]
        country_name = countries[country_key]["name"]
        if country_capital == "":
            print(f"The capital of {country_name} is {country_name}")
        else:
            print(f"The capital of {country_name} is {country_capital}")
    elif chosen_country == "quit":
        break
    else:
        print("That country does not exist in the list")

