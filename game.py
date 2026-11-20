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
        for perso in equipe:
            print("-", perso["nom"], "- ATK", perso["attaque"], "- DEF", perso["defense"], "- PV", perso["pv"])

        # afficher la liste des personnages avec leurs stats
        print("\nPersonnages disponibles :")
        numero = 1
        for perso in personnages:
            print(numero, ".", perso["nom"], "- ATK", perso["attaque"], "- DEF", perso["defense"], "- PV", perso["pv"])
            numero = numero + 1

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
            if perso in equipe:
                # afficher un message d'erreur
                print("Ce personnage est déjà dans l'équipe")
            else:
                # ajouter le personnage à l'équipe
                equipe.append(perso)

    # retourner l'équipe
    return equipe


# Jouer le combat
def jouer_combat(equipe):
    # se connecter à la base
    client = MongoClient("mongodb://localhost:27017")
    base = client["jeu_combat"]

    # récupérer la liste des monstres
    monstres = list(base["monstres"].find())

    # vagues = 0
    vagues = 0

    # tant que infini
    while True:
        # tirer un monstre au hasard
        monstre = random.choice(monstres)
        pv_monstre = monstre["pv"]

        # afficher les stats du monstre
        print("\n--- Vague", vagues + 1, "---")
        print("Monstre :", monstre["nom"], "- ATK", monstre["attaque"], "- DEF", monstre["defense"], "- PV", pv_monstre)

        # tant que le monstre a des PV
        while pv_monstre > 0:
            # pour chaque personnage vivant
            for perso in equipe:
                if perso["pv"] > 0 and pv_monstre > 0:
                    # le personnage attaque le monstre
                    degats = perso["attaque"] - monstre["defense"]
                    if degats < 0:
                        degats = 0
                    pv_monstre = pv_monstre - degats
                    if pv_monstre < 0:
                        pv_monstre = 0
                    print(perso["nom"], "attaque :", degats, "dégâts (monstre :", pv_monstre, "PV)")

            # si le monstre a encore des PV
            if pv_monstre > 0:
                # le monstre attaque un personnage vivant
                cible = random.choice(equipe)
                while cible["pv"] <= 0:
                    cible = random.choice(equipe)
                degats = monstre["attaque"] - cible["defense"]
                if degats < 0:
                    degats = 0
                cible["pv"] = cible["pv"] - degats
                if cible["pv"] < 0:
                    cible["pv"] = 0
                print(monstre["nom"], "attaque", cible["nom"], ":", degats, "dégâts (", cible["pv"], "PV)")

                # si tous les personnages ont 0 PV
                if equipe[0]["pv"] == 0 and equipe[1]["pv"] == 0 and equipe[2]["pv"] == 0:
                    # retourner vagues
                    print("L'équipe est vaincue !")
                    return vagues

        # vagues = vagues + 1
        print("Monstre vaincu !")
        vagues = vagues + 1