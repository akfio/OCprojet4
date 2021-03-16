from models import Tournoi
from models import Participants
from models import Rounds
from models import Matches
from view import View
import random
from operator import itemgetter


class Controller:
    def __init__(self):
        self.view = View()
        self.tournoi = None
        self.particpants = []
        self.matches = None

    def create_tournament(self):
        name = self.view.get_name()
        place = self.view.get_place()
        date = self.view.get_date()
        turn = self.view.get_turn()
        # round
        player = self.view.get_player()
        type = self.view.get_type()
        description = self.view.get_description()
        # Enregistrer en base
        self.tournoi = Tournoi(name, place, date, turn, None, player, type, description)

    def create_player(self):
        nom = self.view.get_p_name()
        prenom = self.view.get_pname()
        birth = self.view.get_birth_date()
        sexe = self.view.get_sexe()
        classement = self.view.get_classement()
        self.particpants.append(Participants(nom, prenom, birth, sexe, classement))

    def choose_action(self):
        while 1:
            action = self.view.choose_menu()
            if int(action) == 1:
                return self.create_tournament()
            if int(action) == 2:
                return self.create_player()
            else:
                return self.view.choose_menu()

    def get_first_round(self):
        a = itemgetter(4)
        b = sorted(self.particpants, key=a)
        c = len(b) // 2
        first_half = b[:c]
        second_half = b[c:]
        first_round = [
            (first_half[0][5], second_half[0][5]),
            (first_half[1][5], second_half[1][5]),
            (first_half[2][5], second_half[2][5]),
            (first_half[3][5], second_half[3][5])
        ]
        return first_round

    def result_games(self):
        id_blanc = 4
        id_noir = 4
        result = self.view.get_result()
        self.matches = Matches(id_blanc, id_noir, result)


    def get_results(lst_match):
        tot = len(lst_match)
        for i in range(tot):
            result = view.get_result()
            if int(result) == 1:
                lst_match[i].result = "Victoire blanc"
            elif int(result) == 2:
                lst_match[i].result = "Victoire noir"
            elif int(result) == 0:
                lst_match[i].result = "Match nul"
        return lst_match


    def rst_pts():
        a = get_results(lst_match)
        b = len(a)
        print(b)
        for j in range(b):
            rs = None
            if a[j].result == "Victoire blanc":
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


""""
    def get_round():
        # return la liste des match
        return

     def add_result():
        return view.get_result()

    def get_next_round():
        # La nouvelle liste de match
        return

    def get_final_rank():
        return


    def get_rapport():
"""
