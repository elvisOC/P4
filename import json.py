import json
import os

directory = os.path.expandvars(fr'C:\Users\%username%\Desktop\openclassrooms\P4\data\player')
file_path = os.path.join(directory, 'players.json')




class Player:
    def __init__(self, name, surname, birthdate, file_path):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.file_path = file_path
        
    def verifie_file(self):
        if os.path.exists(self.file_path) and os.path.getsize(self.file_path) > 0:
            with open (self.file_path, 'r', encoding='utf-8') as file:
                try: 
                    return json.load(file)
                except json.JSONDecodeError:
                    return {}
        else:
            return {}
        
    def verifie_doublon(self):
        data = self.verifie_file()
        for player in data.values():
            if (
                player.get('name') == self.name and
                player.get('surname') == self.surname and
                player.get('birthdate') == self.birthdate
            ):
                return True
            return False
        
    def addplayer(self):
        data = self.verifie_file()
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
            
new_player = Player(name='test', surname='test', birthdate='31-07-1994', file_path=file_path)
result = new_player.addplayer()
print(result)