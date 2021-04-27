from models import Tournoi
from models import Participants
from models import Rounds
from models import Matches
from view import View
from tinydb import TinyDB, Query, where
from datetime import datetime


class Controller:
    def __init__(self):
        self.view = View()
        self.round = Rounds()
        self.tournoi = None
        self.participants = []
        self.matches = None
        self.hist = []
        self.lst_round = []
        self.db = TinyDB('Tournoi.json')

    def create_tournament(self):
        name = self.view.get_name()
        place = self.view.get_place()
        date = str(datetime.now().date())
        turn = self.view.get_turn()
        player = self.add_player()
        type = self.view.get_type()
        description = self.view.get_description()
        table_tournoi = self.db.table("Tournament")
        table_tournoi.insert(
            {'Name': name, 'Place': place, 'Date': date, 'Players': player, 'Type': type, 'Turn': turn,
             'Description': description})
        self.tournoi = Tournoi(name, place, date, turn, player, type, description)
        # self.hist = self.tournoi.hist

    def create_player(self):
        nom = self.view.get_pyr_name()
        prenom = self.view.get_frt_name()
        birth = self.view.get_birth_date()
        sexe = self.view.get_sexe()
        classement = self.view.get_rank()
        table_players = self.db.table("Players")
        table_players.insert({'Name': nom, 'First_name': prenom, 'Birth_date': birth, 'Sexe': sexe, 'Rank': classement})

    def add_player(self):
        player_serialized = dict()
        for pyr in range(8):
            name = input('Nom du joueur? : ')
            r = self.db.table("Players")
            player = Query()
            a = r.get(player.Name == name)
            if a is None:
                print('Joueur non disponible dans la base de donnée')
                return self.add_player()
            else:
                p = Participants(a["Name"], a["First_name"], a["Birth_date"], a["Sexe"], a["Rank"])
                self.participants.append(p)
                in_add = dict()
                in_add["Name"] = p.nom
                in_add["First_name"] = p.prenom
                in_add["Birth_date"] = p.age
                in_add["Sexe"] = p.sexe
                in_add["Rank"] = p.classement
                player_serialized[str(len(player_serialized))] = in_add
        return player_serialized

    def choose_action(self):
        while 1:
            action = self.view.choose_menu()
            if int(action) == 1:
                return self.create_tournament()
            if int(action) == 2:
                return self.create_player()
            else:
                return self.view.choose_menu()

    def get_round(self):
        b = sorted(self.participants, key=lambda a: a.classement)
        c = len(b) // 2
        first_half = b[:c]
        second_half = b[c:]
        first_round = [
            Matches(first_half[0].nom, first_half[0].id, second_half[0].nom, second_half[0].id, None),
            Matches(first_half[1].nom, first_half[1].id, second_half[1].nom, second_half[1].id, None),
            Matches(first_half[2].nom, first_half[2].id, second_half[2].nom, second_half[2].id, None),
            Matches(first_half[3].nom, first_half[3].id, second_half[3].nom, second_half[3].id, None)
        ]
        self.hist.append(first_round)
        return first_round

    def get_results(self):
        for lst in self.hist:
            for match in lst:
                print("")
                print(match)
                result = self.view.get_result()
                if int(result) == 1:
                    match.result = "Victoire" + " " + match.nom_blanc
                elif int(result) == 2:
                    match.result = "Victoire" + " " + match.nom_noir
                elif int(result) == 0:
                    match.result = "Match nul"
                print(match)
        return self.hist

    def games(self):
        round_serialized = dict()
        for r in self.lst_round:
            for round in r:
                for match in round:
                    to_add = dict()
                    to_add["blanc"] = match.nom_blanc
                    to_add["blanc_id"] = match.id_blanc
                    to_add["noir"] = match.nom_noir
                    to_add["noir_id"] = match.id_noir
                    to_add["result"] = match.result
                    round_serialized[str(len(round_serialized))] = to_add
        return round_serialized

    def rst_pts(self):
        result = self.get_results()
        self.lst_round.clear()
        self.lst_round.append(result)
        table_tournoi = self.db.table("Tournament")
        table_rounds = self.db.table("Rounds")
        table_rounds.insert({"Tournoi_id": len(table_tournoi), "Name": "Round" + " " + str(self.round.round_nbr),
                             "Games": self.games(), "End": str(datetime.now())})
        for lst in result:
            for match in lst:
                rs = None
                if match.result == "Victoire" + " " + match.nom_blanc:
                    rs = match.id_blanc
                elif match.result == "Victoire" + " " + match.nom_noir:
                    rs = match.id_noir
                all = len(self.participants)
                for i in range(all):
                    if self.participants[i].id == rs:
                        self.participants[i].pts += 1
                if match.result == "Match nul":
                    self.participants[match.id_blanc].pts += 0.5
                    self.participants[match.id_noir].pts += 0.5
        return self.participants[0].pts, self.participants[1].pts, self.participants[2].pts, self.participants[3].pts, \
               self.participants[4].pts, self.participants[5].pts, self.participants[6].pts, self.participants[7].pts

    def new_round(self):
        b = sorted(self.participants, key=lambda a: (a.pts, a.classement))
        round = [
            Matches(b[0].nom, b[0].id, b[1].nom, b[1].id, None),
            Matches(b[2].nom, b[2].id, b[3].nom, b[3].id, None),
            Matches(b[4].nom, b[4].id, b[5].nom, b[5].id, None),
            Matches(b[6].nom, b[6].id, b[7].nom, b[7].id, None)
        ]
        self.hist.clear()
        self.hist.append(round)
        for match in self.hist:
            for m in match:
                if int(m.id_blanc) == b[0].id and int(m.id_noir) == b[1].id:
                    tmp_id = round[0].id_noir
                    tmp_nom = round[0].nom_noir
                    round[0].id_noir = round[1].id_blanc
                    round[0].nom_noir = round[1].nom_blanc
                    round[1].id_blanc = tmp_id
                    round[1].nom_blanc = tmp_nom
                else:
                    return round
        return round




a = Controller()

