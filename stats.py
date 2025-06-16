def count_words(book_content):                          # Fonction qui compte les mots dans le texte donné
    words = book_content.split()                        # Divise le texte en une liste de mots (sépare par les espaces)
    num_words = len(words)                              # Calcule le nombre de mots en obtenant la longueur de la liste
    return num_words                                    # Retourne le nombre total de mots
