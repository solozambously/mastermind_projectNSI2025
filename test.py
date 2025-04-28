from functions_metiers import *


random_color_sequence = generate_random_color_sequence()
correct_colors_in_correct_position = correct_colors_in_correct_position(random_color_sequence, ["R", "G", "B", "Y"])
correct_colors_wrong_position = correct_colors_wrong_position(random_color_sequence, ["R", "G", "B", "Y"])
print("La combinaison secrète est :", random_color_sequence)
print("Votre tentative :            ['R', 'G', 'B', 'Y']")
print(define_numbers_pions(correct_colors_wrong_position, correct_colors_in_correct_position))