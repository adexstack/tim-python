import csv

input_filename = '../country_info.txt'

# with open(input_filename, encoding='utf-8', newline='') as countries_data:
#     country_reader = csv.reader(countries_data, delimiter='|') # the csv will use the | as the separators
#     for row in country_reader:
#         print(row)

#dialect usage
# Using sniffer to automatically work out the delimiter as we might be reading dynamic data from internet
# with open(input_filename, encoding='utf-8', newline='') as countries_data:
#     sample = countries_data.read()
#     country_dialect = csv.Sniffer().sniff(sample)
#     countries_data.seek(0) # Go back to the start of the line as above .read() has read the entire file
#     country_reader = csv.reader(countries_data, dialect=country_dialect) #csv will use the gotten dialect as separator
#     for row in country_reader:
#         print(row)

# more efficient than the above as reading the entire file 1st to work out the dialect isn't smart, using the 1st 3 lines
with open(input_filename, encoding='utf-8', newline='') as countries_data:
    sample = ""
    for line in range(3): # getting the 1st 3 lines from the file
        sample += countries_data.readline()
    country_dialect = csv.Sniffer().sniff(sample) # sniffing the 3 lines gotten from above
    country_dialect.skipinitialspace = True # would remove the 1st blank space in " Harare"
    countries_data.seek(0) # Go back to the start of the line as above .read() has read the entire file
    country_reader = csv.reader(countries_data, dialect=country_dialect) #csv will use the gotten dialect as separator
    for row in country_reader:
        print(row)

print('*' * 80)
# dialect underlying concept to know
attributes = ['delimiter',
              'doublequote',
              'escapechar',
              'lineterminator',
              'quotechar',
              'quoting',
              'skipinitialspace',
              ]
for attribute in attributes:
    print(f'{attribute}: {repr(getattr(country_dialect, attribute))}') # repr also prints out the line terminator
