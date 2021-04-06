from models import Tournoi
from models import Participants
from models import Rounds
from models import Matches
from view import View
from tinydb import TinyDB, Query, where


class Controller:
    def __init__(self):
        self.view = View()
        self.tournoi = None
        self.particpants = []
        self.matches = None
        self.hist = []
        self.db = TinyDB('Tournoi.json')

    def create_tournament(self):
        name = self.view.get_name()
        place = self.view.get_place()
        date = self.view.get_date()
        turn = self.view.get_turn()
        # round
        player = self.view.get_player()
        type = self.view.get_type()
        description = self.view.get_description()
        table_tournoi = self.db.table("Tournament")
        table_tournoi.insert({'Name': name, 'Place': place, 'Date': date, 'Players': player, 'Type': type, 'Description': description})
        self.tournoi = Tournoi(name, place, date, turn, None, player, type, description)
        self.hist = self.tournoi.hist

    def create_player(self):
        nom = self.view.get_p_name()
        prenom = self.view.get_pname()
        birth = self.view.get_birth_date()
        sexe = self.view.get_sexe()
        classement = self.view.get_classement()
        self.particpants.append(Participants(nom, prenom, birth, sexe, classement))
        table_players = self.db.table("Players")
        table_players.insert({'Name': nom, 'First_name': prenom, 'Birth_date': birth, 'Sexe': sexe, 'Rank': classement})

    def choose_action(self):
        while 1:
            action = self.view.choose_menu()
            if int(action) == 1:
                return self.create_tournament()
            if int(action) == 2:
                return self.create_player()
            else:
                return self.view.choose_menu()

    def get_round():
        b = sorted(player, key=lambda a: a.classement)
        c = len(b) // 2
        first_half = b[:c]
        second_half = b[c:]
        first_round = [
            Matches(first_half[0].nom, first_half[0].id, second_half[0].nom, second_half[0].id, None),
            Matches(first_half[1].nom, first_half[1].id, second_half[1].nom, second_half[1].id, None),
            Matches(first_half[2].nom, first_half[2].id, second_half[2].nom, second_half[2].id, None),
            Matches(first_half[3].nom, first_half[3].id, second_half[3].nom, second_half[3].id, None)
        ]
        hist.append(first_round)
        return first_round

    def get_results(lst_match):
        tot = len(lst_match)
        for i in range(tot):
            result = View.get_result()
            if int(result) == 1:
                lst_match[i].result = "Victoire blanc"
            elif int(result) == 2:
                lst_match[i].result = "Victoire noir"
            elif int(result) == 0:
                lst_match[i].result = "Match nul"
        return lst_match

    def rst_pts():
        a = get_results(hist)
        b = len(a)
        for j in range(b):
            rs = None
            if a[j].result == "Victoire blanc" + a[j].nom_blanc:
                rs = a[j].id_blanc
            elif a[j].result == "Victoire noir":
                rs = a[j].id_noir
            all = len(player)
            for i in range(all):
                if player[i].id == rs:
                    player[i].pts += 1
            if a[j].result == "Match nul":
                player[a[j].id_blanc].pts += 0.5
                player[a[j].id_noir].pts += 0.5
        return player[0].pts, player[1].pts, player[2].pts, player[3].pts, player[4].pts, player[5].pts, player[6].pts, \
               player[7].pts

    def new_round():
        b = sorted(player, key=lambda a: (a.pts, a.classement))
        round = [
            Matches(b[0].nom, b[0].id, b[1].nom, b[1].id, None),
            Matches(b[2].nom, b[2].id, b[3].nom, b[3].id, None),
            Matches(b[4].nom, b[4].id, b[5].nom, b[5].id, None),
            Matches(b[6].nom, b[6].id, b[7].nom, b[7].id, None)
        ]
        hist.append(round)
        for match in hist:
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

