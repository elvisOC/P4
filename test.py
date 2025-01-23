import json
import os


directory = os.path.expandvars(fr'C:\Users\%username%\Desktop\openclassrooms\P4\data\player')
file_path = os.path.join(directory, 'players.json')
with open(file_path, 'r') as file:
    data = json.load(file)
    
print (data)
key = data.keys()
print (key)