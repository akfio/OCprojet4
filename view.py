from datetime import date
from tinydb import TinyDB, Query
from models import Matches, Participants



class View:
    # Tournoi
    def get_name(self):
        try:
            name = input('Nom du Tournoi? ')
            if len(name) > 20:
                print('Nom du tournoi trop long')
                return self.get_name()
            return name
        except ValueError:
            return self.get_name()

    def get_place(self):
        try:
            place = input('Lieu du tournoi? ')
            if len(place) > 20:
                return self.get_place()
            return place
        except ValueError:
            return self.get_place()

    def get_turn(self):
        turn = 4
        print('nombre de tours par défault: 4 ')
        more = input('Entrer une nouvelle valeur ou appuyer sur "ENTER" ')
        if len(more) > 0:
            turn = more
        print('nombre de tours = ' + str(turn))
        return turn

    def add_player(self):
        db = TinyDB('db.json')
        controller = Controller()
        for pyr in range(8):
            name = input('Nom du joueur? : ')
            r = db.table("Players")
            player = Query()
            a = r.get(player.Name == name)
            if a is None:
                print('Joueur non disponible dans la base de donnée')
                return self.add_player()
            else:
                p = Participants(a["Name"], a["First_name"], a["Birth_date"], a["Sexe"], a["Rank"])
                controller.participants.append(p)
        return controller.participants

    def get_type(self):
        try:
            print('Taper 1 pour Bullet')
            print('Taper 2 pour Blitz')
            print('Taper 3 pour Rapide')
            type = int(input('Choix = '))
            if type == 1:
                time = 'Bullet'
                print('Partie Bullet')
                return time
            if type == 2:
                time = 'Biltz'
                print('Partie Blitz')
                return time
            if type == 3:
                time = 'Rapide'
                print('Partie Rapide')
                return time
            if type != [1, 2, 3]:
                return self.get_type()
        except ValueError:
            return self.get_type()

    def get_description(self):
        try:
            description = input('description du tournoi: ')
            if len(description) > 20:
                return self.get_description()
            return description
        except ValueError:
            return self.get_description()

    # Participants
    def get_pyr_name(self):
        try:
            name = input('Nom du joueur? ')
            if len(name) > 20:
                print('Nom trop long')
                return self.get_pyr_name()
            return name
        except ValueError:
            return self.get_pyr_name()

    def get_frt_name(self):
        try:
            pname = input('Prenom du joueur? ')
            if len(pname) > 20:
                print('Prenom trop long')
                return self.get_frt_name()
            return pname
        except ValueError:
            return self.get_frt_name()

    def get_birth_date(self):
        try:
            birth_date = input('Date de naissance: ' 'JJ/MM/AAAA: ')
            if len(birth_date) != 10:
                return self.get_birth_date()
            return birth_date
        except ValueError:
            return self.get_birth_date()

    def get_sexe(self):
        try:
            sexe = input('sexe du joueur: ''H/F ')
            if len(sexe) != 1:
                return self.get_sexe()
            return sexe
        except ValueError:
            return self.get_sexe()

    def get_rank(self):
        try:
            rank = int(input('Classement général du joueur: '))
            if rank < 0:
                print('Chiffre négatif')
                return self.get_rank()
            return rank
        except ValueError:
            print('Entrer une valeur numérique')
            return self.get_rank()

    # Rounds

    def get_lst_match(self):
        return

    # Matches
    def get_result(self):
        result = input("""
                       Tapez 1 pour une victoire du joueur 1
                       Tapez 0 pour un match nul
                       Tapez 2 pour une victoire du joueur 2

                       """)
        if result > str(2):
            print("Valeur incorrecte")
            return self.get_result()
        elif result < str(0):
            print("Valeur incorrecte")
            return self.get_result()
        return result

    # MENU

    def choose_menu(self):
        print("""
            Menu du Tournoi: 
              1 : Création de tournoi
              2 : Création de participants
              """)
        a = input("choisir une action: ")
        return a



