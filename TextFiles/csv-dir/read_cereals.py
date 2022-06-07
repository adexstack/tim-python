import csv

csv_filename = 'cereal_grains.csv'

with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    header = csv_file.readline().strip('\n').split()
    print(f'Column header is {header}')
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC) # to unquote the numerics Note that this converts to float
    for row in reader:
        print(row)