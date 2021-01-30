from main import Tournoi



def get_name(self):
    name = input('Nom du Tournoi? ')
    return name


def get_place(self):
    place = input('Lieu du tournoi? ')
    return place


def get_date():
    try:
        date = input('jour ')
        return date
    except ValueError:
        return get_date



def get_turn():
    turn = 4
    return


def get_round():
    return


def get_player():
    return


def get_description(self):
    description = input('description du tournoi: ')
    if len(description) > 20:
        return self.get_description
    return description


# Participants
def get_p_name(self):
    name = input('Nom du joueur? ')
    if len(name) > 20:
        print('Nom du tournoi trop long')
        return self.get_p_name()
    return name


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
        return classement
    except ValueError:
        return get_classement()
