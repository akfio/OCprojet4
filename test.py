from operator import itemgetter
import view
from models import Matches, Participants, Tournoi
from controller import Controller
from tinydb import TinyDB, Query

db = TinyDB('db.json')

player = [
    Participants("Brady", "Tom", "03/06/1960", "H", 2),
    Participants("James", "LeBron", "03/06/1960", "H", 4),
    Participants("Westbrook", "Russell", "03/06/1960", "H", 7),
    Participants("Federer", "Roger", "03/06/1960", "H", 8),
    Participants("Nadal", "Rapha", "03/06/1960", "H", 5),
    Participants("Henry", "Titi", "03/06/1960", "H", 1),
    Participants("Gignac", "André", "03/06/1960", "H", 6),
    Participants("Obama", "Presi", "03/06/1960", "H", 3)
]

hist = []


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
        print(lst_match[i])
        result = view.get_result()
        if int(result) == 1:
            lst_match[i].result = "Victoire" + " " + lst_match[i].nom_blanc
        elif int(result) == 2:
            lst_match[i].result = "Victoire" + " " + lst_match[i].nom_noir
        elif int(result) == 0:
            lst_match[i].result = "Match nul"
        print(lst_match[i])
    return lst_match


def rst_pts():
    a = get_results(hist)
    b = len(a)
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

print(rst_pts())

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


def fonctionnement():
    get_round()
    rst_pts()
    new_round()
    rst_pts()


"""
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
"""


class Static:
    variable = 4


a = Static()
# print(a.variable) 4
a.variable = 5
# print(a.variable) 5
# print(Static.variable) 4
