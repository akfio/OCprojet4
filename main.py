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

    def tournoi(self):
        return self.nom, self.lieu, self.date, self.tour, self.round, self.player, self.type, self.description


class Participants:
    def __init__(self, nom, prenom, age, sexe, classement):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.sexe = sexe
        self.classement = classement

    def participants(self):
        return self.nom, self.prenom, self.age, self.sexe, self.classement
