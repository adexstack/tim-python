import json
import urllib.request # use request instead

json_data_source = 'https://www.ncdc.noaa.gov/cag/time-series/global/globe/land_ocean/ytd/12/1880-2021/data.json'


with urllib.request.urlopen(json_data_source) as data_stream:
    data = data_stream.read().decode('utf=8')
    anomalies = json.loads(data) # loads().... getting json from python object

for year, value in anomalies['data'].items():
    year, value = int(year), float(value)
    print(f"{year}...{value:6.2f}")
print('*' * 80)