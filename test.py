from operator import itemgetter
import view
from models import Matches, Participants
from controller import Controller

player = [
    Participants("Brady", "Tom", "03/06/1960", "H", 1),
    Participants("James", "LeBron", "03/06/1960", "H", 3),
    Participants("Westbrook", "Russell", "03/06/1960", "H", 7),
    Participants("Federer", "Roger", "03/06/1960", "H", 8),
    Participants("Nadal", "Rapha", "03/06/1960", "H", 5),
    Participants("Henry", "Titi", "03/06/1960", "H", 4),
    Participants("Gignac", "André", "03/06/1960", "H", 6),
    Participants("Obama", "Presi", "03/06/1960", "H", 2)
]


def get_round_result():
    a = itemgetter(4)
    b = sorted(player, key=a)
    c = len(b) // 2
    first_half = b[:c]
    second_half = b[c:]
    first_round = [
        (first_half[0].id, second_half[0].id),
        (first_half[1].id, second_half[1].id),
        (first_half[2].id, second_half[2].id),
        (first_half[3].id, second_half[3].id)
    ]
    return first_round


lst_match = [
    Matches(player[0].id, player[4].id, None),
    Matches(player[1].id, player[5].id, None),
    Matches(player[2].id, player[6].id, None),
    Matches(player[3].id, player[7].id, None)
]


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


class Points:
    pts = 0


def add_points():
    n = Points()
    b = view.get_result()
    if b == 1:
        n.pts += 1
    elif b == 2:
        n.pts += 1
    elif b == 0:
        n.pts += 0.5
        n.pts += 0.5
    return b





class Static:
    variable = 4


a = Static()
# print(a.variable) 4
a.variable = 5
# print(a.variable) 5
# print(Static.variable) 4
"""



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
