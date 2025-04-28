from functions_metiers import *

def afficher_bienvenue():
    """
    Affiche le message de bienvenue.
    Entrées :
        Aucune.
    Sorties :
        Aucune.
    """
    print("Bienvenue dans le jeu Mastermind !")

def demander_combinaison(couleurs):
    """
    Demande à l'utilisateur d'entrer une combinaison de 4 couleurs.
    Entrées :
        couleurs (list) : Liste des couleurs valides.
    Sorties :
        str : La combinaison entrée par l'utilisateur.
    """
    while True:
        combinaison = input("Entrez une combinaison de 4 couleurs parmi R, G, B, Y, P, O : ").upper()
        if len(combinaison) != 4:
            print("Votre combinaison est invalide, elle contient soit trop soit pas assez de couleurs.")
            continue
        if all(c in couleurs for c in combinaison):
            return combinaison
        else:
            print("Combinaison invalide. Essayez à nouveau.")

def afficher_resultats(counter_wrong_position, count_correct_position):
    """
    Affiche les résultats de l'essai de l'utilisateur.
    Entrées :
        counter_wrong_position (int) : Nombre de couleurs correctes mais mal placées.
        count_correct_position (int) : Nombre de couleurs correctes à la position correcte.
    Sorties :
        Aucune.
    """
    print("Vous avez : ", counter_wrong_position, "et", count_correct_position)

def afficher_fin_jeu(random_color_sequence):
    """
    Affiche le message de fin de jeu avec la combinaison correcte.
    Entrées :
        random_color_sequence (list) : La séquence aléatoire générée.
    Sorties :
        Aucune.
    """
    print("Fin du jeu ! La combinaison était : ", random_color_sequence)
    print("Crédits : Solal Bouzanquet & Antoines Bourgues - Eleve en NSI1G3 | Projet Mastermind")
    print("Merci d'avoir joué !")

def jouer_mastermind():
    """
    Fonction principale pour jouer au jeu Mastermind.
    Entrées :
        Aucune.
    Sorties :
        Aucune.
    """
    random_color_sequence = generate_random_color_sequence()
    couleurs = ["R", "G", "B", "Y", "P", "O"]
    tentatives = 0
    max_tentatives = 12

    afficher_bienvenue()

    while tentatives < max_tentatives:
        combinaison = demander_combinaison(couleurs)
        tentatives += 1

        print('Votre essai : ', combinaison)
        count_correct_position = correct_colors_in_correct_position(random_color_sequence, combinaison)
        counter_wrong_position = correct_colors_wrong_position(random_color_sequence, combinaison)
        counter_wrong_position, count_correct_position, finish_game = define_numbers_pions(counter_wrong_position, count_correct_position)
        
        afficher_resultats(counter_wrong_position, count_correct_position)

        if finish_game:
            print("Vous avez gagné !")
            break

        print("Tentatives restantes : ", max_tentatives - tentatives)

    afficher_fin_jeu(random_color_sequence)