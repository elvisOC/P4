class View:

    def home_menu():
        print("1.Tournoi")
        print("2.Joueurs")
        print("3.Rapport")
        print("4.Quitter")
        return input("Choississez un menu : ")
    
    def menu_tournoi():
        print("1.Créer tournoi")
        print("2.Consulter anciens tournois")
        print("3.Revenir au menu principal")
        return input("Choississez un menu : ")
    
    def menu_joueur():
        print("1.Ajouter joueur")
        print("2.Afficher la liste des joueurs")
        print("3.Revenir au menu principal")
        return input("Choississez un menu : ")
    
    def menu_rapport():
        print("1.Afficher rapport")
        print("2.Revenir au menu principal")
        return input("Choississez un menu : ")
    
    def menu_creation_joueur():
        identifiant = input("Identifiant : ").strip()
        surname = input("Nom : ")
        name = input("Prenom : ")
        birthdate = input("Date de naissance (JJ-MM-AAAA) : ")
        return identifiant, surname, name, birthdate
    
    def menu_creation_tournoi():
        name = input("Nom du tournoi : ")
        location = input("Lieu du tournoi : ")
        start_date = input("Date de début (JJ-MM-AAAA) : ")
        end_date = input("Date de fin (JJ-MM-AAAA) : ")
        number_of_rounds = int(input(f"Nombre de tours (4 par defaut) : "))
        current_round = 0
        description = input("Description : ")
        return name, location, start_date, end_date, number_of_rounds, current_round, description
    
    def menu_quitter():
        print("Au revoir !")
        
    def menu_liste_players():
        print("Liste Joueurs : ")