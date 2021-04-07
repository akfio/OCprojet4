from datetime import date
from operator import attrgetter, itemgetter
import random


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

    def get_date(self):
        try:
            a = input("Année : ")
            b = input("Mois : ")
            c = input("Jour : ")
            d = date(int(a), int(b), int(c))
            print(d)
        except ValueError:
            print('Utiliser un nombre compris entre 1 et 12 pour le mois et entre 1 et 31 pour le jour')
            return self.get_date()

    def get_turn(self):
        turn = 4
        print('nombre de tours par défault: 4 ')
        more = input('Entrer une nouvelle valeur ou appuyer sur "ENTER" ')
        if len(more) > 0:
            turn = more
        print('nombre de tours = ' + str(turn))
        return turn

    def get_player(self):
        name = input('Nom du joueur? : ')
        return name


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
    def get_p_name(self):
        try:
            name = input('Nom du joueur? ')
            if len(name) > 20:
                print('Nom trop long')
                return self.get_p_name()
            return name
        except ValueError:
            return self.get_p_name()

    def get_pname(self):
        try:
            pname = input('Prenom du joueur? ')
            if len(pname) > 20:
                print('Prenom trop long')
                return self.get_pname()
            return pname
        except ValueError:
            return self.get_pname()

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

    def get_classement(self):
        try:
            classement = int(input('Classement général du joueur: '))
            if classement < 0:
                print('Chiffre négatif')
                return self.get_classement()
            return classement
        except ValueError:
            print('Entrer une valeur numérique')
            return self.get_classement()

    # Rounds

    def get_lst_match(self):
        return

    # Matches
    def get_result(self):
        result = input("""
                       Tapez 1 pour une victoire du joueur blanc
                       Tapez 0 pour un match nul
                       Tapez 2 pour une victoire du joueur noir

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





def add_results(lst_match):
    tot = len(lst_match)
    for i in range(tot):
        print(lst_match[i])
        result = get_result()
        if int(result) == 1:
            lst_match[i].result = "Victoire" + " " + lst_match[i].nom_blanc
        elif int(result) == 2:
            lst_match[i].result = "Victoire" + " " + lst_match[i].nom_noir
        elif int(result) == 0:
            lst_match[i].result = "Match nul"
        print(lst_match[i])
    return lst_match



