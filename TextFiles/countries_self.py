country_info = "country_info.txt"

countries = {}
with open(country_info) as data:
    data.readline()
    for line in data:
        data = line.strip('\n').split('|')
        print(data)
        country, capital, code, code3, dialing, timezone, currency = data
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
