from models import Tournoi
from models import Participants
from models import Rounds
from models import Matches
from view import View
from tinydb import TinyDB, Query
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
        self.t_name = []
        self.db = TinyDB('Tournoi.json')

    def create_tournament(self):
        name = self.view.get_name()
        self.t_name.append(name)
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
            name = self.view.name_player()
            table_players = self.db.table("Players")
            player = Query()
            a = table_players.get(player.Name == name)
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

    def get_round(self):
        sort = sorted(self.participants, key=lambda a: a.classement)
        split = len(sort) // 2
        first_half = sort[:split]
        second_half = sort[split:]
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

    def get_id(self):
        table_tournoi = self.db.table("Tournament")
        name = self.t_name[0]
        data = table_tournoi.all()
        i = 0
        while i < len(data):
            if data[i]["Name"] == name:
                break
            i += 1
        return i + 1

    def round_db(self):
        table_rounds = self.db.table("Rounds")
        table_rounds.insert({"Tournoi_id": self.get_id(), "Name": "Round" + " " + str(self.round.round_nbr),
                             "Games": self.games(), "End": str(datetime.now())})
        return

    def set_pts(self):
        result = self.get_results()
        self.lst_round.clear()
        self.lst_round.append(result)
        for lst in result:
            for match in lst:
                winner = None
                if match.result == "Victoire" + " " + match.nom_blanc:
                    winner = match.id_blanc
                elif match.result == "Victoire" + " " + match.nom_noir:
                    winner = match.id_noir
                all_players = len(self.participants)
                for i in range(all_players):
                    if self.participants[i].id == winner:
                        self.participants[i].pts += 1
                if match.result == "Match nul":
                    self.participants[match.id_blanc].pts += 0.5
                    self.participants[match.id_noir].pts += 0.5
        self.round_db()
        return self.participants[0].pts, self.participants[1].pts, self.participants[2].pts, self.participants[3].pts, \
               self.participants[4].pts, self.participants[5].pts, self.participants[6].pts, self.participants[7].pts

    def charge_pts(self):
        result = self.get_results()
        self.lst_round.clear()
        self.lst_round.append(result)
        for lst in result:
            for match in lst:
                winner = None
                if match.result == "Victoire" + " " + match.nom_blanc:
                    winner = match.id_blanc
                elif match.result == "Victoire" + " " + match.nom_noir:
                    winner = match.id_noir
                all_players = len(self.participants)
                for i in range(all_players):
                    if self.participants[i].id == winner:
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

    def charger(self):
        # Chercher le nom d'un tournoi
        name = self.view.name_tournoi()
        self.t_name.append(name)
        # Trouver le tournoi correspondant
        b = Query()
        table_tournoi = self.db.table("Tournament")
        get_tournoi = table_tournoi.get(b.Name == name)
        # Ajouter les joueurs à la list players
        d = get_tournoi["Players"]
        for i in d:
            player = Participants(d[i]["Name"], d[i]["First_name"], d[i]["Birth_date"], d[i]["Sexe"], d[i]["Rank"])
            self.participants.append(player)
        # Retrouver les rounds avec l'ID du tournoi
        id = get_tournoi.doc_id
        table_round = self.db.table("Rounds")
        count = table_round.count(b.Tournoi_id == id)
        # Ajouter les matchs dans list de round
        f = 0
        for doc in range(count):
            f += 1
            i = table_round.get((b.Tournoi_id == id) & (b.Name == "Round " + str(f)))
            j = i["Games"]
            for k in j:
                l = Matches(j[k]["blanc"], j[k]["blanc_id"], j[k]["noir"], j[k]["noir_id"], j[k]["result"])
                self.lst_round.append(l)
        # Recalculer le nombre de points
        for match in self.lst_round:
            winner = None
            if match.result == "Victoire" + " " + match.nom_blanc:
                winner = match.id_blanc
            elif match.result == "Victoire" + " " + match.nom_noir:
                winner = match.id_noir
            all_players = len(self.participants)
            for i in range(all_players):
                if self.participants[i].id == winner:
                    self.participants[i].pts += 1
            if match.result == "Match nul":
                self.participants[match.id_blanc].pts += 0.5
                self.participants[match.id_noir].pts += 0.5
        # Continuer le tournoi
        z = get_tournoi["Turn"]
        if count == 0:
            count += 1
            self.get_round()
            self.set_pts()
            for g in range(z - count):
                self.new_round()
                self.set_pts()
        else:
            for g in range(z - count):
                self.new_round()
                self.charge_pts()
                b = Rounds()
                count = table_round.count(Query().Tournoi_id == id)
                total = count + 1
                b.round_nbr = total
                table_rounds = self.db.table("Rounds")
                table_rounds.insert({"Tournoi_id": self.get_id(), "Name": "Round" + " " + str(b.round_nbr),
                                     "Games": self.games(), "End": str(datetime.now())})

    def end_tournoi(self):
        sort = sorted(self.participants, key=lambda a: a.pts)
        print(sort)
        return

    def new_rank(self):
        view = View()
        name = input('Nom du joueur? : ').capitalize()
        table_players = self.db.table("Players")
        player = Query()
        a = table_players.get(player.Name == name)
        if a is None:
            print("Joueur non présent dans la base de donnée")
            return self.new_rank()
        elif table_players.count(player.Name == name) > 1:
            first_name = input('Prénom du joueur? : ').capitalize()
            b = table_players.get((player.Name == name) & (player.First_name == first_name))
            if b is None:
                print("Prénom non présent dans la base de donnée")
                return self.new_rank()
            print("Classement actuel: ")
            print(b['Rank'])
            new_rank = view.get_rank()
            table_players.update({"Rank": new_rank}, Query().Rank == b['Rank'])
            return b['Rank']
        else:
            print("Classement actuel: ")
            print(a['Rank'])
            new_rank = view.get_rank()
            table_players.update({"Rank": new_rank}, Query().Rank == a['Rank'])
            return a['Rank']

    def rapport_acteurs(self):
        table_players = self.db.table("Players")
        name = self.view.input_acteurs()
        if int(name) == 2:
            return sorted(table_players, key=lambda a: a['Rank'])
        elif int(name) == 1:
            return sorted(table_players, key=lambda a: a['Name'])
        else:
            print("Veuillez saisir 1 ou 2")
            return self.rapport_acteurs()

    def pyrs_in_tnmt(self):
        table_tournoi = self.db.table("Tournament")
        a = Query()
        name = self.view.name_player()
        get = table_tournoi.get(a.Name == name)
        d = get["Players"]
        lst = []
        for i in d:
            p = Participants(d[i]["Name"], d[i]["First_name"], d[i]["Birth_date"], d[i]["Sexe"], d[i]["Rank"])
            lst.append(p)
        menu = self.view.input_pyrs()
        if int(menu) == 2:
            return sorted(lst, key=lambda a: a.classement)
        elif int(menu) == 1:
            return sorted(lst, key=lambda a: a.nom)
        else:
            print("Veuillez saisir 1 ou 2")
            return self.pyrs_in_tnmt()

    def all_tnmt(self):
        table_tournoi = self.db.table("Tournament")
        return table_tournoi.all()

    def all_turn_tnmt(self):
        table_round = self.db.table("Rounds")
        table_tournoi = self.db.table("Tournament")
        name = self.view.name_tournoi()
        b = Query()
        get = table_tournoi.get(b.Name == name)
        d = get.doc_id
        count = table_round.count(b.Tournoi_id == d)
        round = 0
        lst_rnd = []
        for doc in range(count):
            round += 1
            i = table_round.get((b.Tournoi_id == d) & (b.Name == "Round" + " " + str(round)))
            lst_rnd.append(i)
        return lst_rnd

    def all_games_tnmt(self):
        name = self.view.name_tournoi()
        b = Query()
        table_tournoi = self.db.table("Tournament")
        get = table_tournoi.get(b.Name == name)
        id = get.doc_id
        table_round = self.db.table("Rounds")
        count = table_round.count(b.Tournoi_id == id)
        round = 0
        lst = []
        for doc in range(count):
            round += 1
            i = table_round.get((b.Tournoi_id == id) & (b.Name == "Round " + str(round)))
            lst.append(i["Games"])
        return lst

    def all_rapports(self):
        while 1:
            menu = self.view.input_rapports()
            if int(menu) == 1:
                return self.rapport_acteurs()
            if int(menu) == 2:
                return self.pyrs_in_tnmt()
            if int(menu) == 3:
                return self.all_tnmt()
            if int(menu) == 4:
                return self.all_turn_tnmt()
            if int(menu) == 5:
                return self.all_games_tnmt()
            else:
                print("Commande indisponible")
                return self.all_rapports()


    def choose_action(self):
        while 1:
            action = self.view.choose_menu()
            if int(action) == 1:
                return self.create_tournament()
            if int(action) == 2:
                return self.charger()
            if int(action) == 3:
                return self.create_player()
            if int(action) == 4:
                return self.new_rank()
            if int(action) == 5:
                return self.all_rapports()
            else:
                print("Commande indisponible")
                return self.view.choose_menu()

a = Controller()
a.choose_action()

