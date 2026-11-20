from pymongo import MongoClient


# Sauvegarder le score
def sauvegarder_score(nom, vagues):
    # se connecter à la base
    client = MongoClient("mongodb://localhost:27017")
    base = client["jeu_combat"]

    # enregistrer le nom du joueur et le nombre de vagues
    base["scores"].insert_one({"nom": nom, "vagues": vagues})


# Afficher le classement
def afficher_classement():
    # se connecter à la base
    client = MongoClient("mongodb://localhost:27017")
    base = client["jeu_combat"]

    # récupérer les 3 meilleurs scores
    scores = list(base["scores"].find().sort("vagues", -1).limit(3))

    print("\nClassement :")
    if len(scores) == 0:
        print("Aucun score pour le moment")

    # pour chaque score
    rang = 1
    for score in scores:
        # afficher le nom et le nombre de vagues
        print(rang, ".", score["nom"], "-", score["vagues"], "vagues")
        rang = rang + 1
