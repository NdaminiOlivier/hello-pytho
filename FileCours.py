from pickle import *

Mon_Fichier = open("Fichier.txt","r")
contenu = Mon_Fichier.read()
#print(contenu)

Mon_Fichier = open("Fichier.txt","w")
contenu2 = Mon_Fichier.write("Je voudrai savoir le monde est si simple et à la fois complexe")
print(contenu2)
Mon_Fichier.close()
Mon_Fichier.closed


score = {
    "joueur 1": 5,
    "joueur 2": 34,
    "joueur 3": 20,
    "joueur 4": 2,
}
with open("AjoutObjet.txt","wb") as FileAjouter:
    mon_pickler = Pickler(FileAjouter)
    mon_pickler.dump(score)