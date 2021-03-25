from tinydb import TinyDB, Query, where
from controller import Controller
from view import View
from models import Participants

db = TinyDB('participants.json')

str = db.search(where('Name') == 'Nom6')
p = Participants(str[0]["Name"], str[0]["First Name"], str[0]["Birthdate"], str[0]["Genre"], str[0]["Ranking"])

table_parcipant = db.table("Participants")
table_parcipant.insert({'Name': 'Alice' , 'Age' : 19})
table_parcipant.insert({'Name': 'Jean' , 'Age' : 19})
table_parcipant.insert({'Name': 'Jacques' , 'Age' : 19})
for data in table_parcipant.all():
    print(data)
"""
def get_p_name():
    try:
        name = input('Nom du joueur? ')
        if len(name) > 20:
            print('Nom trop long')
            return get_p_name()
        return name
    except ValueError:
        return get_p_name()


def get_pname():
    try:
        pname = input('Prenom du joueur? ')
        if len(pname) > 20:
            print('Prenom trop long')
            return get_pname()
        return pname
    except ValueError:
        return get_pname()


def get_birth_date():
    try:
        birth_date = input('Date de naissance: ' 'JJ/MM/AAAA: ')
        if len(birth_date) != 10:
            return get_birth_date()
        return birth_date
    except ValueError:
        return get_birth_date()


def get_sexe():
    try:
        sexe = input('sexe du joueur: ''H/F ')
        if len(sexe) != 1:
            return get_sexe()
        return sexe
    except ValueError:
        return get_sexe()


def get_classement():
    try:
        classement = int(input('Classement général du joueur: '))
        if classement < 0:
            print('Chiffre négatif')
            return get_classement()
        return classement
    except ValueError:
        print('Entrer une valeur numérique')
        return get_classement()


def create_player():
    nom = get_p_name()
    prenom = get_pname()
    birth = get_birth_date()
    sexe = get_sexe()
    classement = get_classement()
    db.insert({"Name": nom, "First Name": prenom, "Birthdate": birth, "Genre": sexe, "Ranking": classement})
    return Participants(nom, prenom, birth, sexe, classement)

print(db.all())
"""




"""
insert() = ajouter dans le json 
all() = voir le json
Avec Query()
info = Query()
search() =  permet de chercher une donnée : db.search(info.X == "aaa")
update() = db.update({"Y" : "bbb", info.X == "aaa"})
remove () = db.remove(info.X == "aaa")



data pour :
- Participant
- round
- Tournoi



??? = Virer le self 
= recupérer depuis db
"""


