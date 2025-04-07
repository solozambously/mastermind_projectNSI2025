import random

def generate_random_color_sequence():
    """
    Generate a random sequence of colors.
    Red : R
    Green : G
    Blue : B
    Yellow : Y
    Purple : P
    Orange : O
    """
    colors = ["R", "G", "B", "Y", "P", "O"]
    random_color_sequence = [random.choice(colors) for _ in range(4)]
    return random_color_sequence

def correct_colors_in_correct_position(random_color_sequence, guess):
    """
    Count the number of correct colors in the correct position.
    """
    counter_correct_position = 0
    for i in range(4):
        if guess[i] == random_color_sequence[i]:
            counter_correct_position += 1
        
    return counter_correct_position

def correct_colors_wrong_position(random_color_sequence, guess):
    """
    Count the number of correct colors in the guess.
    """
    counter_wrong_position = 0
    for i in range(4):
        for j in range(4):
            if guess[j] == random_color_sequence[i]:
                counter_wrong_position += 1
    
    return counter_wrong_position

def define_numbers_pions(counter_wrong_position, counter_correct_position):
    """
    Define the number of pions.
    """
    if counter_wrong_position != 0:
        counter_wrong_position = counter_wrong_position - counter_correct_position 
    
    pion_blanc = ["aucun pion blanc", "un pion blanc", "deux pions blancs", "trois pions blancs", "quatre pions blancs"][counter_wrong_position]
    pion_noir = ["aucun pion noir", "un pion noir", "deux pions noirs", "trois pions noirs", "quatre pions noirs"][counter_correct_position]

    return pion_noir, pion_blanc
