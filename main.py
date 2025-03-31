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

def correct_colors_wrong_position(random_color_sequence, guess):
    """
    Count the number of correct colors in the guess.
    """
    counter = 0
    for i in range(4):
        for j in range(4):
            if guess[j] == random_color_sequence[i]:
                counter_wrong_position += 1
    
    return counter_wrong_position

def correct_colors_in_correct_position(random_color_sequence, guess):
    """
    Count the number of correct colors in the correct position.
    """
    counter = 0
    for i in range(4):
        if guess[i] == random_color_sequence[i]:
            counter_correct_position += 1
    
    return counter_correct_position

random_color_sequence = generate_random_color_sequence()
print("Random Color Sequence:", random_color_sequence)
print('Le nombre de bonnes couleurs sont (mais pas bien placé /!\ bug pout l\'instant):', correct_colors_wrong_position(random_color_sequence, ["R", "G", "B", "Y"]))
print('Le nombre de bonnes couleurs et bien placé:', correct_colors_in_correct_position(random_color_sequence, ["R", "G", "B", "Y"]))