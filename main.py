from functions import *

random_color_sequence = generate_random_color_sequence()
# Test permettant de voir les couleurs pour tester le programmme
# print(random_color_sequence)

couleurs = ["R", "G", "B", "Y", "P", "O"]


tentatives = 0
max_tentatives = 12

print("Bienvenue dans le jeu Mastermind !")
while tentatives < max_tentatives: 
    combinaison = input("Entrez une combinaison de 4 couleurs parmi R, G, B, Y, P, O : ").upper()
    tentatives += 1
    
    if len(combinaison) != 4:
        print("Votre combinaison est invalide, Elle contient soit trop soit pas assez de couleurs")
        continue
    
    if  all(c in couleurs for c in combinaison):
        print('Votre essai : ', combinaison)
        count_correct_position = correct_colors_in_correct_position(random_color_sequence, combinaison)
        counter_wrong_position = correct_colors_wrong_position(random_color_sequence, combinaison)
        counter_wrong_position, count_correct_position, finish_game = define_numbers_pions(counter_wrong_position, count_correct_position)
        print("Vous avez : ", counter_wrong_position, "et", count_correct_position)
        if finish_game:
            print("Vous avez gagné !")
            break
    else:
        print("Combinaison invalide. Essayez à nouveau.")
    print("tentaive restantes : ", max_tentatives - tentatives)
    
print("Fin du jeu ! La combinaison était : ", random_color_sequence)
print("Crédits : Solal Bouzanquet & Antoines Bourgues - Eleve en NSI1G3 | Projet Mastermind")
print("Merci d'avoir joué !")