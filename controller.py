from models import Tournoi
from models import Participants
from models import Rounds
from models import Matches
from view import View


class Controller:
    def __init__(self):
        self.view = View()
        self.tournoi = None
        self.particpants = []

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
