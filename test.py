from operator import itemgetter
import view
from models import Matches, Participants, Tournoi
from controller import Controller

player = [
    Participants("Brady", "Tom", "03/06/1960", "H", 1),
    Participants("James", "LeBron", "03/06/1960", "H", 1),
    Participants("Westbrook", "Russell", "03/06/1960", "H", 7),
    Participants("Federer", "Roger", "03/06/1960", "H", 8),
    Participants("Nadal", "Rapha", "03/06/1960", "H", 5),
    Participants("Henry", "Titi", "03/06/1960", "H", 2),
    Participants("Gignac", "André", "03/06/1960", "H", 6),
    Participants("Obama", "Presi", "03/06/1960", "H", 2)
]
# for match in hist:
# if match.id_blanc == id.blanc
# and match.id_noir == id.noir
# juste 1 et 2 a chaque tour
hist = []


def get_round():
    b = sorted(player, key=lambda a: (a.classement, a.pts))
    c = len(b) // 2
    first_half = b[:c]
    second_half = b[c:]
    first_round = [
        Matches(first_half[0].nom, first_half[0].id, second_half[0].nom, second_half[0].id, None),
        # Matches(first_half[1].nom(first_half[1].id), second_half[1].nom(second_half[1].id), None),
        # Matches(first_half[2].nom(first_half[2].id), second_half[2].nom(second_half[2].id), None),
        # Matches(first_half[3].nom(first_half[3].id), second_half[3].nom(second_half[3].id), None)
    ]
    return print(first_round)


get_round()


def is_exist(id_blanc, id_noir):
    for match in hist:
        if int(match.id_blanc) == int(id_blanc) and int(match.id_noir) == int(id_noir):
            print("ok")


# lst_match = [
# Matches(player[0].id, player[4].id, None),
# Matches(player[1].id, player[5].id, None),
# Matches(player[2].id, player[6].id, None),
# Matches(player[3].id, player[7].id, None)
# ]


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


# match = Matches(player[5].id, player[6].id, "Victoire noir")


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


"""
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
