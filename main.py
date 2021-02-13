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

    def Add_Match(self, lst_matchs):
        self.lst_match.append(lst_matchs)


class Matches:
    def __init__(self, IDBlanc, IDNoir, Result):
        self.P_blanc = ID_Blanc
        self.p_noir = ID_Noir
        self.resultat = Result
