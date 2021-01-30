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

