def count_words(book_content):                          # Fonction qui compte les mots dans le texte donné
    words = book_content.split()                        # Divise le texte en une liste de mots (sépare par les espaces)
    num_words = len(words)                              # Calcule le nombre de mots en obtenant la longueur de la liste
    return num_words                                    # Retourne le nombre total de mots

def count_characters(character):                        # Fonction qui compte chaque caractère (incluant espaces et symboles)
    counts = {}                                         # Initialise un dictionnaire vide pour les fréquences
    contents = character.lower()                        # Convertit tout en minuscule pour la cohérence
    for char in contents:                               # Parcourt chaque caractère
        if char in counts:                              # Si le caractère existe déjà dans le dictionnaire
            counts[char] += 1                           # Incrémente le compteur
        else:
            counts[char] = 1                            # Sinon, initialise à 1
    return counts                                       # Retourne le dictionnaire de fréquences


