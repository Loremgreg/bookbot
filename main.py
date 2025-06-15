def get_book_text(book_path):                           # Fonction qui prend un chemin de fichier en paramètre
    with open(book_path, 'r', encoding="utf-8") as f:   # la methode pour ouvrir et lire un fichier -> Reading and Writing Files : f = open('workfile', 'r', encoding="utf-8") r= reading, w= writing, etc --> Ouvre le fichier en mode lecture avec l'encodage UTF-8
       # file_contents = f.read()
        return f.read()                                 # la fonction Retourne le contenu du fichier sous forme de chaîne

def main():                                             # Fonction principale qui appelle get_book_text avec un chemin relatif vers le document a lire
    contents = get_book_text("books/frankenstein.txt")  
    print(contents) 

main()



