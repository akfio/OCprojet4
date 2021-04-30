from datetime import datetime




class View:
    # Tournoi
    def get_name(self):
        try:
            name = input('Nom du Tournoi? ').capitalize()
            if len(name) > 20:
                print('Nom du tournoi trop long')
                return self.get_name()
            return name
        except ValueError:
            return self.get_name()

    def get_place(self):
        try:
            place = input('Lieu du tournoi? ').capitalize()
            if len(place) > 20:
                return self.get_place()
            return place
        except ValueError:
            return self.get_place()

    def get_turn(self):
        turn = 4
        print('nombre de tours par défault: 4 ')
        more = input('Entrer une nouvelle valeur ou appuyer sur "ENTER" ')
        if len(more) > 0:
            turn = more
        print('nombre de tours = ' + str(turn))
        return turn

    def get_type(self):
        try:
            print('Taper 1 pour Bullet')
            print('Taper 2 pour Blitz')
            print('Taper 3 pour Rapide')
            type = int(input('Choix = '))
            if type == 1:
                time = 'Bullet'
                print('Partie Bullet')
                return time
            if type == 2:
                time = 'Biltz'
                print('Partie Blitz')
                return time
            if type == 3:
                time = 'Rapide'
                print('Partie Rapide')
                return time
            if type != [1, 2, 3]:
                return self.get_type()
        except ValueError:
            return self.get_type()

    def get_description(self):
        try:
            description = input('description du tournoi: ').capitalize()
            if len(description) > 20:
                return self.get_description()
            return description
        except ValueError:
            return self.get_description()

    # Participants
    def get_pyr_name(self):
        try:
            name = input('Nom du joueur? ').capitalize()
            if len(name) > 20:
                print('Nom trop long')
                return self.get_pyr_name()
            return name
        except ValueError:
            return self.get_pyr_name()

    def get_frt_name(self):
        try:
            pname = input('Prenom du joueur? ').capitalize()
            if len(pname) > 20:
                print('Prenom trop long')
                return self.get_frt_name()
            return pname
        except ValueError:
            return self.get_frt_name()

    def get_birth_date(self):
        try:
            a = input('année de naissance : ')
            b = input('mois de naissance : ')
            c = input('jour de naissance : ')
            d = a + '-' + b + '-' + c
            e = datetime.strptime(d, '%Y-%m-%d').date()
            return str(e)
        except ValueError:
            print("Format incorrect, dois être AAAA-MM-JJ")
            return self.get_birth_date()

    def get_sexe(self):
        try:
            sexe = input('sexe du joueur: ''H/F ').capitalize()
            if len(sexe) != 1:
                return self.get_sexe()
            return sexe
        except ValueError:
            return self.get_sexe()

    def get_rank(self):
        try:
            rank = int(input('Classement général du joueur: '))
            if rank < 0:
                print('Chiffre négatif')
                return self.get_rank()
            return rank
        except ValueError:
            print('Entrer une valeur numérique')
            return self.get_rank()

    # Matches
    def get_result(self):
        result = input("""
                       Tapez 1 pour une victoire du joueur 1
                       Tapez 0 pour un match nul
                       Tapez 2 pour une victoire du joueur 2

                       """)
        if result > str(2):
            print("Valeur incorrecte")
            return self.get_result()
        elif result < str(0):
            print("Valeur incorrecte")
            return self.get_result()
        return result

    # INPUT

    def name_tournoi(self):
        a = input("Nom du tournoi? ").capitalize()
        return a

    def name_player(self):
        a = input("Nom du joueur? ").capitalize()
        return a

    def input_acteurs(self):
        name = input("""
                    Rapport des acteurs par ordre:

                  1 : Alphabetique 
                  2 : Classement

                    """)
        return name

    def input_pyrs(self):
        menu = input("""
                                Rapport des joueurs par ordre:

                              1 : Alphabetique 
                              2 : Classement

                                """)
        return menu

    def input_rapports(self):
        menu = input("""
                                Choisir le rapport a afficher:

                              1 : Liste de tous les acteurs 
                              2 : Liste de tous les joueurs d'un tournoi
                              3 : Liste de tous les tournoi
                              4 : Liste de tous les tours d'un tournoi
                              5 : Liste de tous les matchs d'un tournoi

                                """)
        return menu

    # MENU

    def print_result(self):
        print("""
        
                CLASSEMENT DE FIN DE TOURNOI:
                
        format : <Nom, Prenom : Pts>
            
            """)

    def print(self):
        print(self)

    def choose_menu(self):
        print("""
            Menu du Tournoi: 
              1 : Création d'un tournoi
              2 : Chargement d'un tournoi
              3 : Création d'un participant
              4 : Modifier le classement d'un participant
              5 : Afficher un rapport 
              """)
        a = input("choisir une action: ")
        return a



