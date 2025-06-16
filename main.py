from stats import count_words, count_characters

def get_book_text(book_path):                           # Fonction qui prend un chemin de fichier en paramètre
    with open(book_path, 'r', encoding="utf-8") as f:   # la methode pour ouvrir et lire un fichier -> Reading and Writing Files : f = open('workfile', 'r', encoding="utf-8") r= reading, w= writing, etc --> Ouvre le fichier en mode lecture avec l'encodage UTF-8
       # file_contents = f.read()
        return f.read()                                 # la fonction Retourne le contenu du fichier sous forme de chaîne


def main():                                             # Fonction principale qui appelle get_book_text avec un chemin relatif vers le document a lire
    contents = get_book_text("books/frankenstein.txt")  # Lit le contenu du livre Frankenstein et le stocke dans 'contents'
    count_result = count_characters(contents)           # Compte chaque caractère (lettres, espaces, symboles, etc.) dans le contenu
    num_words = count_words(contents)                   # Compte les mots dans le contenu du livre
    print(f'{num_words} words found in the document')   # Affiche le nombre de mots trouvés dans le document
    print(count_result)                                 # Affiche le dictionnaire des fréquences des caractères
main()                                                  # Appelle la fonction principale pour exécuter le programme

