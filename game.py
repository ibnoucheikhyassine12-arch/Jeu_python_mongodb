from pymongo import MongoClient
# Créer l'équipe
def creer_equipe():
    # se connecter à la base
    client = MongoClient ("mongodb://localhost:27017")
    base = client["jeu_combat"]
    # récupérer la liste des personnages
    personnage = list(base["personnages"].find())
    print(personnage)
    # équipe vide
    equipe = []
    # tant que l'équipe n'a pas 3 personnages
    # afficher l'équipe actuelle
    # afficher la liste des personnages avec leurs stats
    # demander un personnage à l'utilisateur
    # si le personnage est déjà dans l'équipe
    # afficher un message d'erreur
    # sinon, si le choix existe
    # ajouter le personnage à l'équipe
    # sinon
    # afficher un message d'erreur
    # retourner l'équipe
    return []


# Jouer le combat
def jouer_combat(equipe):
    # se connecter à la base
    # vagues = 0
    # tant que infini
    # tirer un monstre au hasard
    # afficher les stats du monstre
    # (le tour de combat, à trouver sur papier)
    # si tous les personnages ont 0 PV
    # retourner vagues
    # vagues = vagues + 1
    return 0


     