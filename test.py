from view import View
from models import Matches, Participants, Tournoi, Rounds
from tinydb import TinyDB, Query, where
from tinydb.operations import add
from datetime import datetime

db = TinyDB('test.json')


def create_tournament():
    view = View()
    name = view.get_name()
    place = view.get_place()
    date = str(datetime.now().date())
    turn = view.get_turn()
    round = None
    player = add_player()
    type = view.get_type()
    description = view.get_description()
    table_tournoi = db.table("Tournament")
    table_tournoi.insert(
        {'Name': name, 'Place': place, 'Date': date, 'Players': player, 'Round': round, 'Type': type, 'Description': description})
    tournoi = Tournoi(name, place, date, turn, round, player, type, description)
    return tournoi


players = []

hist = []


def add_player():
    for pyr in range(8):
        name = input('Nom du joueur? : ')
        r = db.table("Players")
        player = Query()
        a = r.get(player.Name == name)
        if a is None:
            print('Joueur non disponible dans la base de donnée')
            return add_player()
        else:
            p = Participants(a["Name"], a["First_name"], a["Birth_date"], a["Sexe"], a["Rank"])
            players.append(p)
    return str(players)


def create_player():
    view = View()
    nom = view.get_pyr_name()
    prenom = view.get_frt_name()
    birth = view.get_birth_date()
    sexe = view.get_sexe()
    classement = view.get_rank()
    table_players = db.table("Players")
    table_players.insert({'Name': nom, 'First_name': prenom, 'Birth_date': birth, 'Sexe': sexe, 'Rank': classement})


def get_round():
    b = sorted(players, key=lambda a: a.classement)
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
    table_tournoi = db.table("Tournament")
    round = Rounds()
    table_tournoi.update({"Round": {"Name": "Round" + str(round.round_nbr), "Start": str(datetime.now())}})
    return first_round


def get_results(lst_match):
    view = View()
    for lst in lst_match:
        for match in lst:
            print("")
            print(match)
            result = view.get_result()
            if int(result) == 1:
                match.result = "Victoire" + " " + match.nom_blanc
            elif int(result) == 2:
                match.result = "Victoire" + " " + match.nom_noir
            elif int(result) == 0:
                match.result = "Match nul"
            print(match)
    return lst_match


def rst_pts():
    result = get_results(hist)
    round = Query()
    table_tournoi = db.table("Tournament")
    table_tournoi.update({"Round": {"Games": str(result), "End": str(datetime.now())}})
    for lst in result:
        for match in lst:
            rs = None
            if match.result == "Victoire" + " " + match.nom_blanc:
                rs = match.id_blanc
            elif match.result == "Victoire" + " " + match.nom_noir:
                rs = match.id_noir
            all = len(players)
            for i in range(all):
                if players[i].id == rs:
                    players[i].pts += 1
            if match.result == "Match nul":
                players[match.id_blanc].pts += 0.5
                players[match.id_noir].pts += 0.5
    return players[0].pts, players[1].pts, players[2].pts, players[3].pts, players[4].pts, players[5].pts, players[
        6].pts, \
           players[7].pts


def new_round():
    b = sorted(players, key=lambda a: (a.pts, a.classement))
    round = [
        Matches(b[0].nom, b[0].id, b[1].nom, b[1].id, None),
        Matches(b[2].nom, b[2].id, b[3].nom, b[3].id, None),
        Matches(b[4].nom, b[4].id, b[5].nom, b[5].id, None),
        Matches(b[6].nom, b[6].id, b[7].nom, b[7].id, None)
    ]
    hist.clear()
    hist.append(round)
    for match in hist:
        for m in match:
            if int(m.id_blanc) == b[0].id and int(m.id_noir) == b[1].id:
                tmp_id = round[1].id_noir
                tmp_nom = round[1].nom_noir
                round[1].id_noir = round[2].id_blanc
                round[1].nom_noir = round[2].nom_blanc
                round[2].id_blanc = tmp_id
                round[2].nom_blanc = tmp_nom
            else:
                return round
    return round


#def lst():
    #Rounds(1, lst de match avec resultat, debut, fin)

def update_rounds():
    round = Query()
    table_tournoi = db.table("Tournament")
    table_tournoi.update(add("Round", round.round ==)
    #table_tournoi.update("Name": "Round 1", "Age": 19}})

update_rounds()



def fonctionnement():
    db.drop_table("Tournament")
    create_tournament()
    get_round()
    rst_pts()
    new_round()
    rst_pts()



"""
joueur introuvable
save en db les rounds



def add_point(match):
    rs = None
    if match.result == "Victoire blanc":
        rs = match.id_blanc
    elif match.result == "Victoire noir":
        rs = match.id_noir
    all = len(player)
    for i in range(all):
        if player[i].id == rs:
            player[i].pts += 1
    if match.result == "Match nul":
        player[match.id_blanc].pts += 0.5
        player[match.id_noir].pts += 0.5
    return player[match.id_blanc].pts, player[match.id_noir].pts


b = view.get_result()
if b == 1:
    n.pts += 1
elif b == 2:
    n.pts += 1
elif b == 0:
    n.pts += 0.5
    n.pts += 0.5
return b



def get_round(self):
    a = itemgetter(4)
    b = sorted(player, key=a)
    c = len(b) // 2
    first_half = b[:c]
    second_half = b[c:]
    first_round = [
        
    ]
    self.first = first_round


def get_ze_result(self):
    if view.get_result() == 1:

        
        for _ in first_round:
            result = view.get_result()
            match.append(result)
        return
def add_points():
# Ajouter resultat 1 à Joueur 1
# Ajouter resultat 2 à joueur 2


def get_new_round():
    sorted()
    return
    
    match1 = (first_half[0][5], second_half[0][5], view.get_result())
    lst.append(match1)
    match2 = (first_half[1][5], second_half[1][5], view.get_result())
    lst.append(match2)
    match3 = (first_half[2][5], second_half[2][5], view.get_result())
    lst.append(match3)
    match4 = (first_half[3][5], second_half[3][5], view.get_result())
    lst.append(match4)
    return lst
    
    
def ze_result():
    lst = []
    match1 = (get_round_result()[0][0], get_round_result()[0][1], add_points())
    lst.append(match1)
    match2 = (get_round_result()[1][0], get_round_result()[1][1], add_points())
    lst.append(match2)
    match3 = (get_round_result()[2][0], get_round_result()[2][1], add_points())
    lst.append(match3)
    match4 = (get_round_result()[3][0], get_round_result()[3][1], add_points())
    lst.append(match4)
    return lst   
    
    
    Participants("Brady", "Tom", "03/06/1960", "H", 2),
    Participants("James", "LeBron", "03/06/1960", "H", 4),
    Participants("Westbrook", "Russell", "03/06/1960", "H", 7),
    Participants("Federer", "Roger", "03/06/1960", "H", 8),
    Participants("Nadal", "Rapha", "03/06/1960", "H", 5),
    Participants("Henry", "Titi", "03/06/1960", "H", 1),
    Participants("Gignac", "André", "03/06/1960", "H", 6),
    Participants("Obama", "Presi", "03/06/1960", "H", 3) 
"""


class Static:
    variable = 4


a = Static()
# print(a.variable) 4
a.variable = 5
# print(a.variable) 5
# print(Static.variable) 4
