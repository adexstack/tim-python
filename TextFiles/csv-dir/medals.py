import csv

csv_filename = "OlympicMedals_2020.csv"
with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    headers = csv_file.readline().strip('\n').split(',')
    print(f'Column headers: {headers}')
    # issue here is that the country is not stringed "" in the .csv file
    reader = csv.reader(csv_file) # Easiest would be adding quoting=csv.QUOTE_NONNUMERIC but would ValueError here
    for row in reader:
        #print(row)  # Mitigating the above issue by unpacking and converting to int
        # unpacking as printed rows has the numbers printed as string, hence converting them back to int
        rank, country, gold, silver, bronze, total = row
        print(int(rank), country, int(gold), int(silver), int(bronze), int(total))
