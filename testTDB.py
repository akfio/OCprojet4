from tinydb import TinyDB, Query
from controller import Controller
from view import View

db = TinyDB('participants.json')

c = View.get_pname()
db.insert(c)
print(db.all())

"""
insert() = ajouter dans le json 
all() = voir le json
Avec Query()
info = Query()
search() =  permet de chercher une donnée : db.search(info.X == "aaa")
update() = db.update({"Y" : "bbb", info.X == "aaa"})
remove () = db.remove(info.X == "aaa")
"""