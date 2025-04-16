import random  
# On importe le module random pour pouvoir choisir un mot au hasard.
# Ouvre le fichier "mots_dev.txt" en mode lecture et charge son contenu dans une liste.
# Chaque ligne du fichier sera un mot distinct dans la liste.
with open("mots_dev.txt", "r") as fichier:
    liste_de_mots = fichier.read().splitlines()  # Sépare le fichier en lignes et les met dans une liste.

def mot_à_dev():
    
    # Choisir un mot au hasard dans la liste de mots.
    mot = random.choice(liste_de_mots)
    
    # Convertir le mot choisi en une liste de lettres pour le manipuler plus facilement.
    mot_to_liste = list(mot.lower())
    longueur_du_mot = len(mot)
    l_restante = longueur_du_mot
    essai = longueur_du_mot
    
    # Liste pour afficher les lettres devinées et les lettres non trouvées par des '-'
    calcul = ["-"] * longueur_du_mot
    
    # Un ensemble pour stocker les lettres déjà devinées.
    lettres_devinees = set()

    # Affiche le mot à deviner, au début, sous forme de tirets (lettres non devinées).
    print(f"Le mot à deviner : {''.join(calcul)}")
    print(f"Tu as {essai} essais.")

    # Tant que l'utilisateur a encore des essais et qu'il reste des lettres à deviner :
    while essai > 0 and l_restante > 0:
        
        in_put = input("DEVINE UNE LETTRE : ").lower()

        if len(in_put) != 1 or not in_put.isalpha():
            print("Veuillez entrer une seule lettre valide.")
            continue

        if in_put in lettres_devinees:
            print("Tu as déjà deviné cette lettre. Essaie une autre.")
            continue

        lettres_devinees.add(in_put)

        if in_put in mot_to_liste:
            # Remplace les tirets par la lettre correcte dans la liste calcul.
            for i in range(len(mot)):
                if mot_to_liste[i] == in_put:
                    calcul[i] = in_put
                    l_restante -= 1
            print(f"Bravo ! Lettre trouvée : {''.join(calcul)}")
        else:
            essai -= 1
            print(f"Raté ! Il te reste {essai} essais.")

        print(f"Mot actuel : {''.join(calcul)}")
        print(f"Lettres devinées : {', '.join(sorted(lettres_devinees))}")

    if l_restante == 0:
        print("Félicitations, tu as deviné le mot !")
    else:
        print(f"Dommage, le mot était : {mot}")

mot_à_dev()
