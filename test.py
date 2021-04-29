from view import View
from models import Matches, Participants, Tournoi, Rounds
from tinydb import TinyDB, Query, where
from tinydb.operations import add, set
from datetime import datetime

db = TinyDB('test.json')

players = []
hist = []
lst_round = []
t_name = []


def create_tournament():
    view = View()
    name = view.get_name()
    t_name.append(name)
    place = view.get_place()
    date = str(datetime.now().date())
    turn = view.get_turn()
    player = add_player()
    type = view.get_type()
    description = view.get_description()
    table_tournoi = db.table("Tournament")
    table_tournoi.insert(
        {'Name': name, 'Place': place, 'Date': date, 'Players': player, 'Type': type, 'Turn': turn,
         'Description': description})
    tournoi = Tournoi(name, place, date, turn, player, type, description)
    return tournoi


def add_player():
    player_serialized = dict()
    for pyr in range(8):
        name = input('Nom du joueur? : ').capitalize()
        r = db.table("Players")
        player = Query()
        a = r.get(player.Name == name)
        if a is None:
            print('Joueur non disponible dans la base de donnée')
            return add_player()
        else:
            p = Participants(a["Name"], a["First_name"], a["Birth_date"], a["Sexe"], a["Rank"])
            players.append(p)
            in_add = dict()
            in_add["Name"] = p.nom
            in_add["First_name"] = p.prenom
            in_add["Birth_date"] = p.age
            in_add["Sexe"] = p.sexe
            in_add["Rank"] = p.classement
            player_serialized[str(len(player_serialized))] = in_add
    return player_serialized


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


def games(lst_round):
    round_serialized = dict()
    for r in lst_round:
        for round in r:
            for match in round:
                to_add = dict()
                to_add["blanc"] = match.nom_blanc
                to_add["blanc_id"] = match.id_blanc
                to_add["noir"] = match.nom_noir
                to_add["noir_id"] = match.id_noir
                to_add["result"] = match.result
                round_serialized[str(len(round_serialized))] = to_add  # round_serialized[0]["blanc"] -> nom1
    return round_serialized


def set_pts():
    result = get_results(hist)
    lst_round.clear()
    lst_round.append(result)
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
    rst_pts()
    return players[0].pts, players[1].pts, players[2].pts, players[3].pts, players[4].pts, players[5].pts, players[
        6].pts, \
           players[7].pts

def charge_pts():
    result = get_results(hist)
    lst_round.clear()
    lst_round.append(result)
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


def rst_pts():
    b = Rounds()
    table_rounds = db.table("Rounds")
    table_rounds.insert({"Tournoi_id": get_id(), "Name": "Round" + " " + str(b.round_nbr),
                         "Games": games(lst_round), "End": str(datetime.now())})


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


def get_id():
    table_tournoi = db.table("Tournament")
    name = t_name[0]
    data = table_tournoi.all()
    i = 0
    while i < len(data):
        if data[i]["Name"] == name:
            break
        i += 1
    return i + 1


def charger():
    # Chercher le nom d'un tournoi
    a = input("Nom du Tournoi? ").capitalize()
    t_name.append(a)
    # Trouver le tournoi correspondant
    b = Query()
    table_tournoi = db.table("Tournament")
    c = table_tournoi.get(b.Name == a)
    # Ajouter les joueurs à la list players
    d = c["Players"]
    for i in d:
        p = Participants(d[i]["Name"], d[i]["First_name"], d[i]["Birth_date"], d[i]["Sexe"], d[i]["Rank"])
        players.append(p)
    # Regrouper le doc ID avec le Tournoi ID des rounds
    id = c.doc_id
    table_round = db.table("Rounds")
    e = table_round.count(b.Tournoi_id == id)
    # Ajouter les matchs dans list de round
    f = 0
    for doc in range(e):
        f += 1
        i = table_round.get((b.Tournoi_id == id) & (b.Name == "Round " + str(f)))
        j = i["Games"]
        for k in j:
            l = Matches(j[k]["blanc"], j[k]["blanc_id"], j[k]["noir"], j[k]["noir_id"], j[k]["result"])
            lst_round.append(l)
    # Recalculer le nombre de points
    for match in lst_round:
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
    # Continuer le tournoi
    z = c["Turn"]
    if e == 0:
        e += 1
        get_round()
        set_pts()
        for g in range(z - e):
            new_round()
            set_pts()
    else:
        for g in range(z - e):
            new_round()
            charge_pts()
            b = Rounds()
            e = table_round.count(Query().Tournoi_id == id)
            c = e + 1
            b.round_nbr = c
            table_rounds = db.table("Rounds")
            table_rounds.insert({"Tournoi_id": get_id(), "Name": "Round" + " " + str(b.round_nbr),
                                 "Games": games(lst_round), "End": str(datetime.now())})

def end_tournoi():
    sort = sorted(players, key=lambda a: a.pts)
    print(players[0].nom.pts)
    return

def fonctionnement():
    #db.drop_table("Tournament")
    db.drop_table("Rounds")
    #create_tournament()
    charger()
    end_tournoi()
    #get_round()
    #set_pts()
    #new_round()
    #set_pts()
    #db.drop_table("Players")
    #for i in range(8):
        #create_player()

fonctionnement()
def rapport_acteurs():
    table_players = db.table("Players")
    a = input("""
                Rapport des acteurs par ordre:
                
              1 : Alphabetique 
              2 : Classement
              
                """)
    if int(a) == 2:
        return sorted(table_players, key=lambda a: a['Rank'])
    elif int(a) == 1:
        return sorted(table_players, key=lambda a: a['Name'])
    else:
        print("Veuillez saisir 1 ou 2")
        return rapport_acteurs()


def pyrs_in_tnmt():
    table_tournoi = db.table("Tournament")
    a = Query()
    b = input("nom du tournoi? ").capitalize()
    c = table_tournoi.get(a.Name == b)
    d = c["Players"]
    lst = []
    for i in d:
        p = Participants(d[i]["Name"], d[i]["First_name"], d[i]["Birth_date"], d[i]["Sexe"], d[i]["Rank"])
        lst.append(p)
    e = input("""
                    Rapport des joueurs par ordre:

                  1 : Alphabetique 
                  2 : Classement

                    """)
    if int(e) == 2:
        return sorted(lst, key=lambda a: a.classement)
    elif int(e) == 1:
        return sorted(lst, key=lambda a: a.nom)
    else:
        print("Veuillez saisir 1 ou 2")
        return pyrs_in_tnmt()


def all_tnmt():
    table_tournoi = db.table("Tournament")
    return table_tournoi.all()


def all_turn_tnmt():
    table_round = db.table("Rounds")
    table_tournoi = db.table("Tournament")
    a = input("Nom du tournoi? ")
    b = Query()
    c = table_tournoi.get(b.Name == a)
    d = c.doc_id
    e = table_round.count(b.Tournoi_id == d)
    f = 0
    lst_rnd = []
    for doc in range(e):
        f += 1
        i = table_round.get((b.Tournoi_id == d) & (b.Name == "Round" + " " + str(f)))
        lst_rnd.append(i)
    return lst_rnd


def all_games_tnmt():
    a = input("Nom du Tournoi? ").capitalize()
    b = Query()
    table_tournoi = db.table("Tournament")
    c = table_tournoi.get(b.Name == a)
    id = c.doc_id
    table_round = db.table("Rounds")
    e = table_round.count(b.Tournoi_id == id)
    f = 0
    lst = []
    for doc in range(e):
        f += 1
        i = table_round.get((b.Tournoi_id == id) & (b.Name == "Round " + str(f)))
        lst.append(i["Games"])
    return lst


def find_pyr():
    table_players = db.table("Players")
    a = Query()
    b = input("nom du joueur? ").capitalize()
    c = table_players.get(a.Name == b)
    return c


def change_name():
    table_players = db.table("Players")
    player = Query()
    a = table_players.get(player.Name == input("nom? "))
    b = str(input("new name: "))
    table_players.update({"Name": b}, Query().Name == a["Name"])


def change_rank():
    view = View()
    name = input('Nom du joueur? : ').capitalize()
    table_players = db.table("Players")
    player = Query()
    a = table_players.get(player.Name == name)
    if a is None:
        print("Joueur non présent dans la base de donnée")
        return change_rank()
    elif table_players.count(player.Name == name) > 1:
        first_name = input('Prénom du joueur? : ').capitalize()
        b = table_players.get((player.Name == name) & (player.First_name == first_name))
        if b is None:
            print("Prénom non présent dans la base de donnée")
            return change_rank()
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



"""
class Static:
    variable = 4
    
    
a = Static()
# print(a.variable) 4
a.variable = 5
# print(a.variable) 5
# print(Static.variable) 4
"""
