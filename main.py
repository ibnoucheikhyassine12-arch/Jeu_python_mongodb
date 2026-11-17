#  Afficher menu principal
#  afficher les options numérotées
#  1. Démarrer le jeu
#  2. Afficher le classement
#  3. Quitter


# Récupérer un choix valide dans le menu principal
# tant que infini
# afficher menu principal
# demander un choix à l'utilisateur
# si le choix est 1, 2 ou 3
# retourner le choix valide
# afficher un message d'erreur


# Demander le nom du joueur
# demander un nom à l'utilisateur
# retourner le nom


# Créer l'équipe
# équipe vide
# tant que l'équipe n'a pas 3 personnages
#  afficher l'équipe actuelle
#  afficher la liste des personnages disponibles avec leurs stats
#  demander un personnage à l'utilisateur
#  si le personnage est déjà dans l'équipe
# afficher un message d'erreur
# sinon, si le choix existe
# ajouter le personnage à l'équipe
# afficher un message d'erreur
# retourner l'équipe

# Jouer le combat
# vagues = 0
# tant que infini
# tirer un monstre au hasard
# afficher les stats du monstre
# si tous les personnages ont 0 PV
# retourner vagues
# vagues = vagues + 1


# Sauvegarder le score
# enregistrer le nom du joueur et le nombre de vagues
# Afficher le classement
# récupérer les 3 meilleurs scores
# pour chaque score
# afficher le nom et le nombre de vagues

# Programme principal
# tant que infini
# choix = récupérer un choix valide dans le menu principal
#  si le choix est 1
#  nom = demander le nom du joueur
#  équipe = créer l'équipe
#   vagues = jouer le combat avec l'équipe
#   sauvegarder le score avec le nom et les vagues
#   afficher le score
#   afficher le classement
#   si le choix est 2
#   afficher le classement
#   si le choix est 3
#   afficher "Au revoir"
#   arrêter la boucle

def afficher_menu_principal() :
    print(" Démarrer le jeu")
    print("Afficher le classement")
    print(" Quitter")

def choix_est_valide(choix) :
    return choix in ("1", "2", "3")



