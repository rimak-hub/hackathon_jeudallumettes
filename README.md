# hackathon_group5


******** Menu ********"          
print(Bienvenue dans le jeu des allumettes!")
print("Instructions: choisissez un nombre d'allumette puis decidez du nombre (entre 1 et 3) a enlever.\n A son tour, l'autre joueur  fera de meme et ainsi de suite jusqu'a ce qu'il n'y ait plus d'allumettes.\n Le perdant est celui qui retirera la derniere allumette.")
print("*************************\n")           

print("Choisissez le mode de jeu: ")
print("(0) Spectateur ") # IA vs IA
print("(1) Solo: 1 joueur ") #humain VS IA
print("(2) 2 joueurs ") #humain VS humain

print("Choisissez le niveau de jeu: ")
print("(0) Débutant ") #Random
print("(1) Intermédiaire ") #IA stratégie optimale pour un modulo
print("(2) Master ") #IA stratégie optimale pour deux modulos
print("(3) Pro ") #Stratégie optimal pour trois  modulos
print("(4) Expert ") #Stratégie optimal pour tous les modulos
niveau=  int(input("Niveau: "))
