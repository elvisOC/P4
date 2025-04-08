class View:

    def home_menu():
        print("1.Tournoi")
        print("2.Joueurs")
        print("3.Quitter")
        return input("Choississez un menu : ")

    def menu_tournoi():
        print("1.Créer tournoi")
        print("2.Consulter tournois")
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
        number_of_rounds = int(input("Nombre de tours (4 par defaut) : "))
        description = input("Description : ")
        players_nbr = int(input("Nombre de joueurs : "))
        list_player = View.menu_liste_players(players_nbr)
        return name, location, start_date, end_date, number_of_rounds, description, players_nbr, list_player

    def menu_quitter():
        print("Au revoir !")

    def menu_liste_players(players_nbr):
        list_player = []
        for nbr in range(1, players_nbr + 1):
            player = input(f"Identifiant joueur{nbr} : ")
            list_player.append(player)
        return list_player

    def menu_tournoi_ID():
        return input("Entrez l'ID du tournoi : ")

    def menu_rounds():
        return input("Entrez le numéro du round : ")

    def menu_matchs():
        return input("Selectionner le match : ")

    def resultat():
        return input("Vainqueur ? (1 pour joueur 1, 2 pour joueur 2, 3 pour match nul) : ")
