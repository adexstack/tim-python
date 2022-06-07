from typing import Dict

vehicles: dict[str, str] = {'dream': 'Honda 250T', 'roadster': 'BMW R1100', 'er5': 'Kawasaki ER5', 'can-am': 'Bombardier Can-Am 250',
            'virago': 'Yamaha XV250', 'tenere': 'Yamaha XT650', 'jimny': 'Suzuki Jimny 1.5',
            'fiesta': 'Ford Fiesta Ghia 1.4'}

vehicles["toy"] = "glider"
vehicles["roadster"] = "New Roadster"

deleted_item = vehicles.pop("Tan", "This key doesn't exist") # return default None or passed string in not exist
print(deleted_item)

# del vehicles["Tenere"] # Keyerror as the key doesn't exist

del vehicles["tenere"]

vehicles.pop("fiesta")

# for key in vehicles:
#     print(key, vehicles[key], sep=", ")
for key, value in vehicles.items():
    print(key, value, sep=", ")
