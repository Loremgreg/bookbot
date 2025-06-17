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

#from main import main
def sort_characters_by_count(char_counts):                         # Fonction qui trie les caractères par nombre d'occurrences
    conversion_to_dic_list = [{"char": key, "num": value} for key, value in char_counts.items()] # Transforme en liste de dictionnaires
    conversion_to_dic_list.sort(key=lambda item: item["num"], reverse=True) # Trie du plus fréquent au moins fréquent -> “Utilise item["num"] comme critère de tri pour chaque dictionnaire de la liste.”
    return conversion_to_dic_list                       # Retourne la liste triée

                        





