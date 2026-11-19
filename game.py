from pymongo import MongoClient
import random


# Créer l'équipe
def creer_equipe():
    # se connecter à la base
    client = MongoClient("mongodb://localhost:27017")
    base = client["jeu_combat"]

    # récupérer la liste des personnages
    personnages = list(base["personnages"].find())

    # équipe vide
    equipe = []

    # tant que l'équipe n'a pas 3 personnages
    while len(equipe) < 3:
        # afficher l'équipe actuelle
        print("\nÉquipe actuelle :")
        if len(equipe) == 0:
            print("Aucun personnage")
        for i, perso in enumerate(equipe, start=1):
            print(i, ".", perso["nom"], "- ATK", perso["attaque"], "- DEF", perso["defense"], "- PV", perso["pv"])

        # afficher la liste des personnages avec leurs stats
        print("\nPersonnages disponibles :")
        for i, perso in enumerate(personnages, start=1):
            print(i, ".", perso["nom"], "- ATK", perso["attaque"], "- DEF", perso["defense"], "- PV", perso["pv"])

        # demander un personnage à l'utilisateur
        choix = input("Choisissez un personnage (numéro) : ")

        # si ce n'est pas un nombre
        if not choix.isdigit():
            # afficher un message d'erreur
            print("Choix invalide : tapez un numéro")
        # sinon, si le numéro n'existe pas
        elif int(choix) < 1 or int(choix) > len(personnages):
            # afficher un message d'erreur
            print("Ce numéro n'existe pas")
        else:
            perso = personnages[int(choix) - 1]
            # si le personnage est déjà dans l'équipe
            deja_pris = False
            for membre in equipe:
                if membre["nom"] == perso["nom"]:
                    deja_pris = True
            if deja_pris:
                # afficher un message d'erreur
                print("Ce personnage est déjà dans l'équipe")
            else:
                # ajouter le personnage à l'équipe (une copie)
                equipe.append(perso.copy())

    # retourner l'équipe
    return equipe

# Jouer le combat
#     se connecter à la base
#     récupérer la liste des monstres
#     vagues = 0
#     tant que infini
#         tirer un monstre au hasard
#         afficher les stats du monstre
#         tant que le monstre a des PV
#             pour chaque personnage vivant
#                 le personnage attaque le monstre
#             si le monstre a encore des PV
#                 le monstre attaque un personnage vivant
#                 si tous les personnages ont 0 PV
#                     retourner vagues
#         vagues = vagues + 1