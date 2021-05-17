class Tournoi:

    def __init__(self, name, place, date, turn, player, type, description):
        self.nom = name
        self.lieu = place
        self.date = date
        self.tour = turn
        self.player = player
        self.type = type
        self.description = description
        self.hist = []


class Participants:
    def __str__(self) -> str:
        return self.nom + self.prenom + self.age + self.sexe + str(self.classement)

    def __repr__(self):
        return '{} {} : {} : {} ({})'.format(self.nom, self.prenom, self.age, self.sexe, self.classement)

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
    round_nbr = 1

    def __init__(self):
        self.round_nbr = Rounds.round_nbr
        Rounds.round_nbr += 1


class Matches:

    def __init__(self, nom_blanc, id_blanc, nom_noir, id_noir, result):
        self.nom_blanc = nom_blanc
        self.id_blanc = id_blanc
        self.nom_noir = nom_noir
        self.id_noir = id_noir
        self.result = result

    def __repr__(self):
        return '{} ({}) VS {} ({}) : {}'.format(self.nom_blanc, self.id_blanc, self.nom_noir, self.id_noir,
                                                self.result)










