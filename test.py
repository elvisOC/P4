import json
import os
import pathlib
from operator import itemgetter
from tabulate import tabulate
import re

directory = os.path.expandvars(fr'C:\Users\%username%\Desktop\openclassrooms\P4\data')
file_path = os.path.join(directory, 'players.json')
    
actual_directory = pathlib.Path(__file__).parent.resolve()
   

#print (pathlib.Path(__file__).parent.resolve())


'''
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


    def addplayer():
        if self.verifie_file():
            return "Problème avec le fichier"
        if self.verifie_doublon():
            return f"Le joueur {self.surname} {self.name} existe déjà"
        max_id = max(map(int, data.keys())) if data else 0
        new_player_id = max_id + 1
        data[str(new_player_id)] = {
            'name' : self.name, 
            'surname' : self.surname, 
            'birthdate' : self.birthdate
            }
        with open (file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            return f"Joueur {self.name} {self.surname} ajouté"
        
        
        
    def verifie_doublon(self):
        data = self.verifie_file()
        for player in data.values():
            if player.get('ID') == self.national_id:
                return True
            return False
            
            

        if not os.path.exists(self.file_path):
            return "Fichier inexistant"
        if os.path.getsize(self.file_path) < 0:
            return "Fichier vide"
        with open (self.file_path, 'r', encoding='utf-8') as file:
            try: 
                data = json.load(file)
                data_list = [v for v in data.values()]
                sorted_data = sorted(data_list, key=itemgetter('name'))
                return tabulate(sorted_data, headers="keys", tablefmt="grid")
            except json.JSONDecodeError:
                return "Problème avec le fichier"

print(liste_joueurs(file_path))

'''

identifiant = "A612345"
if re.match(r"[A-Za-z][A-Za-z]\d\d\d\d\d", identifiant):
    print("L'identifiant est au bon format")
else:
    print("Mauvais format")
            
fes<feswfes