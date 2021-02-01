from main import Tournoi



def get_name():
    try:
        name = input('Nom du Tournoi? ')
        if len(name) > 20:
            print('Nom du tournoi trop long')
            return get_name()
        return name
    except ValueError:
        return get_name()


def get_place():
    try:
        place = input('Lieu du tournoi? ')
        if len(place) > 20:
            return get_place()
        return place
    except ValueError:
        return get_place()


def get_date():
    try:
        date1 = input('Début du tournoi: ' 'JJ/MM/AAAA: ')
        if len(date1) != 10:
            return get_date()
        date2 = input('fin du tournoi: ' 'JJ/MM/AAAA: ')
        if len(date2) != 10:
            return get_date()
        return print(date1 + ' au ' + date2)
    except ValueError:
        return get_date()



def get_turn():
    turn = 4
    print('nombre de tours par défault: 4 ')
    more = input('Entrer une nouvelle valeur ou appuyer sur "ENTREE" ')
    if len(more) > 0:
        turn = more
    print('nombre de tours = ' + str(turn))
    return turn


def get_round():
    return


def get_player():
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


def get_description(self):
    description = input('description du tournoi: ')
    if len(description) > 20:
        return self.get_description
    return description


# Participants
def get_p_name(self):
    try:
        name = input('Nom du joueur? ')
        if len(name) > 20:
            print('Nom du tournoi trop long')
            return self.get_p_name()
        return name
    except ValueError:
        return get_p_name()
    



def get_pname():
    try:
        pname = input('Prenom du joueur?' )
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
        sexe = input('sexe du joueur: ''H/F')
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
        return get_classement()
