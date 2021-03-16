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
        self.hist = []


class Participants:
    id = 0

    def __init__(self, nom, prenom, age, sexe, classement):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.sexe = sexe
        self.classement = classement
        self.id = Participants.id
        Participants.id += 1
        self.pts = 0


class Rounds:

    def __init__(self):
        self.lst_match = []

    def add_match(self, lst_matchs):
        self.lst_match.append(lst_matchs)


class Matches:

    def __init__(self, nom_blanc, id_blanc,  nom_noir, id_noir, result):
        self.nom_blanc = nom_blanc
        self.id_blanc = id_blanc
        self.nom_noir = nom_noir
        self.id_noir = id_noir
        self.result = result

    def __repr__(self):
        return '{} ({}) VS {} ({}) : {}'.format(self.nom_blanc, self.id_blanc, self.nom_noir, self.id_noir, self.result)

