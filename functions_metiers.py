import random

def generate_random_color_sequence():
    """
    Génère une séquence aléatoire de 4 couleurs parmi les suivantes :
    Rouge (R), Vert (G), Bleu (B), Jaune (Y), Violet (P), Orange (O).
    Entrées:
        Aucune.
    Sorties:
        list: Une liste de 4 caractères représentant les couleurs choisies aléatoirement.
    """
    colors = ["R", "G", "B", "Y", "P", "O"]
    random_color_sequence = []
    for i in range(4):
        numbers = random.randint(1, 6)
        random_color_sequence.append(colors[numbers])

    return random_color_sequence

def correct_colors_in_correct_position(random_color_sequence, guess):
    """
    Compte le nombre de couleurs correctes à la position correcte.
    Entrées :
        random_color_sequence (list) : Une liste de 4 couleurs représentant la séquence aléatoire générée.
        guess (list) : Une liste de 4 couleurs représentant la tentative de l'utilisateur.
    Sorties :
        int : Le nombre de couleurs correctes qui sont également à la position correcte.
    """
    
    counter_correct_position = 0
    for i in range(4):
        if guess[i] == random_color_sequence[i]:
            counter_correct_position += 1
        
    return counter_correct_position

def correct_colors_wrong_position(random_color_sequence, guess):
    """
    Compte le nombre de couleurs correctes mais mal placées.
    Entrées :
        random_color_sequence (list) : Une liste de 4 couleurs représentant la séquence aléatoire générée.
        guess (list) : Une liste de 4 couleurs représentant la tentative de l'utilisateur.
    Sorties :
        int : Le nombre de couleurs correctes mais mal placées.
    """

    # On fait des copies pour ne pas modifier les originaux
    sequence_copy = random_color_sequence[:]
    guess_copy = guess[:]
    

    # chercher les bonnes couleurs mal placées
    counter_wrong_position = 0
    for i in range(4):
        if guess_copy[i] is not None and guess_copy[i] in sequence_copy:
            counter_wrong_position += 1
            # Supprimer cette couleur pour ne pas la recompter
            sequence_copy[sequence_copy.index(guess_copy[i])] = None

    return counter_wrong_position


def define_numbers_pions(counter_wrong_position, counter_correct_position):
    """
    Définit le nombre de pions noirs et blancs en fonction des couleurs correctes.
    Entrées :
        counter_wrong_position (int) : Le nombre de couleurs correctes mais mal placées.
        counter_correct_position (int) : Le nombre de couleurs correctes à la position correcte.
    Sorties :
        tuple : Une chaîne décrivant les pions noirs, une chaîne décrivant les pions blancs, 
                et un booléen indiquant si le jeu est terminé.
    """
    
    finish_game = False
    
    if counter_wrong_position != 0:
        counter_wrong_position = counter_wrong_position - counter_correct_position 
    
    pion_blanc = ["aucun pion blanc", "un pion blanc", "deux pions blancs", "trois pions blancs", "quatre pions blancs"][counter_wrong_position]
    pion_noir = ["aucun pion noir", "un pion noir", "deux pions noirs", "trois pions noirs", "quatre pions noirs"][counter_correct_position]

    if counter_correct_position == 4:
        finish_game = True

    return pion_noir, pion_blanc, finish_game