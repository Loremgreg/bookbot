import sys
from stats import count_words, count_characters, sort_characters_by_count

def get_book_text(book_path):                           # Fonction qui prend un chemin de fichier en paramètre
    with open(book_path, 'r', encoding="utf-8") as f:   # la methode pour ouvrir et lire un fichier -> Reading and Writing Files : f = open('workfile', 'r', encoding="utf-8") r= reading, w= writing, etc --> Ouvre le fichier en mode lecture avec l'encodage UTF-8
       # file_contents = f.read()
        return f.read()                                 # la fonction Retourne le contenu du fichier sous forme de chaîne


def main():                                             # Fonction principale qui appelle get_book_text avec un chemin relatif vers le document a lire
   #contents = get_book_text("books/frankenstein.txt")  # Lit le contenu du livre Frankenstein et le stocke dans 'contents'
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        contents = get_book_text(sys.argv[1])

    count_result = count_characters(contents)           # Compte chaque caractère (lettres, espaces, symboles, etc.) dans le contenu
    num_words = count_words(contents)                   # Compte les mots dans le contenu du livre
    sorted = sort_characters_by_count(count_result)

    

    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}")
    print(f'----------- Word Count ----------\nFound {num_words} total words')   # Affiche le nombre de mots trouvés dans le document
    print("--------- Character Count -------\n")
    for result in sorted:
        if result["char"].isalpha() == True:
            print(f"{result['char']}: {result['num']}")
    print("============= END ===============")
                                                        # Affiche le dictionnaire des fréquences des caractères
main()                                                  # Appelle la fonction principale pour exécuter le programme

