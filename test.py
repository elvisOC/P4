import json
import os
import pathlib
from operator import itemgetter
from tabulate import tabulate


directory = os.path.expandvars(fr'C:\Users\%username%\Desktop\openclassrooms\P4\data\player')
file_path = os.path.join(directory, 'players.json')

print (pathlib.Path(__file__).parent.resolve())



def verifie_file(file_path):
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open (file_path, 'r', encoding='utf-8') as file:
            try: 
                data = json.load(file)
                data_list = [v for v in data.values()]
                sorted_data = sorted(data_list, key=itemgetter('name'))
                return tabulate(sorted_data, headers="keys", tablefmt="grid")
            except json.JSONDecodeError:
                return True
    else:
        return False
        
result = verifie_file(file_path)
print (result)