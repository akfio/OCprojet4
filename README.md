Programme pour un tournoi d’echec
----------------------------------------------------------------------------------------------

## Installation

Tout d'abord, créez un dossier via la commande mkdir (ici projet4) dans lequel se trouvera l'environnement virtuel et l'ensemble des données extraites. Puis y accéder via la commande cd.

```python
mkdir projet2
cd projet2
```

Déplacez models.py, view,py, controller,py, setup,cfg et requierements.txt dans le dossier. Ensuite, créez un environnement virtuel dans le dossier (ici nommé env):

```python
python3 -m venv env
```

Puis activez le via :

```python
source env/bin/activate #MacOS ou Unix
ou
env/Scripts/activate.bat #Sur Windows
```
Importer les packages nécessaire avec la commande :

```python 
pip install -r requirements.txt
``` 

## Résultat

Vous pouvez désormais lancer le programme via la commande suivante: 

```python
python3 controller.py
```

Pour générer un rapport flack8-htlm, veillez a bien avoir importer le fichier setup,cfg puis lancer la commande :

```python 
flake8 --format=html --htmldir=flake8-report
```
Un dossier flack8-report sera généré.

## Utilisation

Tout d’abord, commencer par créer les joueurs qui seront sauvegardé par le programme via un fichier «Tournoi.json»
Ensuite créer le tournoi avec les différentes informations :
Nom / Lieu / Date / Nombre de tours / Participants / Type de tournoi / Description
Puis charger le tournoi grâce à son nom, le programme lance le tournoi. 
