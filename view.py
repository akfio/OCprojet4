from datetime import date
from operator import attrgetter, itemgetter

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


    def get_turn():
        turn = 4
        print('nombre de tours par défault: 4 ')
        more = input('Entrer une nouvelle valeur ou appuyer sur "ENTREE" ')
        if len(more) > 0:
            turn = more
        print('nombre de tours = ' + str(turn))
        return turn


    def get_player():
        #aller chercher des joueurs dans une liste
        return


    def get_type():
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
                return get_type()
        except ValueError:
            return get_type()


    def get_description():
        try:
            description = input('description du tournoi: ')
            if len(description) > 20:
                return get_description
            return description
        except ValueError:
            return get_description()


    def get_tournoi():
        all = [get_name(), get_place(), get_date(), get_turn(), get_type(), get_description()]
        return all


    # Participants
    def get_p_name():
        try:
            name = input('Nom du joueur? ')
            if len(name) > 20:
                print('Nom trop long')
                return get_p_name()
            return name
        except ValueError:
            return get_p_name()


    def get_pname():
        try:
            pname = input('Prenom du joueur? ')
            if len(pname) > 20:
                print('Prenom trop long')
                return get_pname()
            return pname
        except ValueError:
            return get_pname()


    def get_birth_date():
        try:
            birth_date = input('Date de naissance: ' 'JJ/MM/AAAA: ')
            if len(birth_date) != 10:
                return get_birth_date()
            return birth_date
        except ValueError:
            return get_birth_date()


    def get_sexe():
        try:
            sexe = input('sexe du joueur: ''H/F ')
            if len(sexe) != 1:
                return get_sexe()
            return sexe
        except ValueError:
            return get_sexe()


    def get_classement():
        try:
            classement = int(input('Classement général du joueur: '))
            if classement < 0:
                print('Chiffre négatif')
                return get_classement()
            return classement
        except ValueError:
            print('Entrer une valeur numérique')
            return get_classement()


    def get_participant():
        p = []
        player = [get_p_name(), get_pname(), get_birth_date(), get_sexe(), get_classement()]
        p.append(player)
        return player

    # Rounds

    def get_lst_match():
        lst = []
        lst.append(get_paire())

    def get_result():
        result = input("joueur blanc: ")
        result2 = input("joueur noir: ")


    def get_nb_pts():
        c = [ (ID joueur, points)]
     #joueur1 = point actuel + result


    # Matches

    def get_paire():
        sorted(player, key=itemgetter(4))
        for player in range(4):


    def get_new_paire():
        sorted(c, key=itemgetter(1), reverse=True)


