from pymongo import MongoClient

# se connecter à MongoDB
client = MongoClient("mongodb://localhost:27017")

# choisir la base du jeu
base = client["jeu_combat"]

# vider les collections (pas de doublons si on relance le fichier)
base["personnages"].delete_many({})
base["monstres"].delete_many({})

# préparer la liste des 10 personnages
personnages = [
    {"nom": "Guerrier", "attaque": 20, "defense": 8, "pv": 100},
    {"nom": "Mage", "attaque": 25, "defense": 3, "pv": 70},
    {"nom": "Archer", "attaque": 22, "defense": 4, "pv": 75},
    {"nom": "Voleur", "attaque": 18, "defense": 5, "pv": 80},
    {"nom": "Paladin", "attaque": 15, "defense": 10, "pv": 120},
    {"nom": "Moine", "attaque": 17, "defense": 7, "pv": 90},
    {"nom": "Barbare", "attaque": 24, "defense": 4, "pv": 95},
    {"nom": "Clerc", "attaque": 12, "defense": 8, "pv": 110},
    {"nom": "Assassin", "attaque": 23, "defense": 2, "pv": 65},
    {"nom": "Chevalier", "attaque": 16, "defense": 9, "pv": 105},
]

# préparer la liste des monstres
monstres = [
    {"nom": "Gobelin", "attaque": 12, "defense": 3, "pv": 60},
    {"nom": "Loup", "attaque": 15, "defense": 4, "pv": 80},
    {"nom": "Orc", "attaque": 18, "defense": 6, "pv": 120},
    {"nom": "Troll", "attaque": 22, "defense": 8, "pv": 160},
    {"nom": "Dragon", "attaque": 28, "defense": 10, "pv": 220},
]

# insérer les personnages et les monstres
base["personnages"].insert_many(personnages)
base["monstres"].insert_many(monstres)

print("base initialisée")