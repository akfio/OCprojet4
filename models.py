
class Tournoi:
    def __init__(self, name, place, date, turn, round, player, type, description):
        self.nom = name
        self.lieu = place
        self.date = date
        self.tour = turn
        self.round = round
        self.player = player
        self.type = type
        self.description = description


class Participants:
    def __init__(self, nom, prenom, age, sexe, classement):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.sexe = sexe
        self.classement = classement


class Rounds:
    def __init__(self):
        self.lst_match = []

    def add_match(self, lst_matchs):
        self.lst_match.append(lst_matchs)


class Matches:
    def __init__(self, id_blanc, id_noir, result):
        self.P_blanc = id_blanc
        self.p_noir = id_noir
        self.resultat = result