from random import*

print("\n\n******** Menu ********")            
print("Bienvenue dans le jeu des allumettes!")
print("Instructions: choisissez un nombre d'allumette puis decidez du nombre (entre 1 et 3) a enlever.\n A son tour, l'autre joueur  fera de meme et ainsi de suite jusqu'a ce qu'il n'y ait plus d'allumettes.\n Le perdant est celui qui retirera la derniere allumette.")
print("*************************\n")           

print("Choisissez le mode de jeu: ")
print("(0) Spectateur ") # IA vs IA
print("(1) Solo: 1 joueur ") #humain VS IA
print("(2) 2 joueurs ") #humain VS humain

n_joueurs_humain=3
#protection nb de joueurs
while n_joueurs_humain>2:
    n_joueurs_humain= int(input("Votre choix: "))


#1 joueur humain
def un_joueurs_humain():
    #protection difficulté
    niveau=5
    while niveau>4:
        print("Choisissez le niveau de jeu: ")
        print("(0) Débutant ") #Random
        print("(1) Intermédiaire ") #IA stratégie optimale pour un modulo
        print("(2) Master ") #IA stratégie optimale pour deux modulos
        print("(3) Pro ") #Stratégie optimal pour trois  modulos
        print("(4) Expert ") #Stratégie optimal pour tous les modulos
        niveau=  int(input("Niveau: "))
    l_n=[' Débutant',  'Intermédiaire', 'Master', 'Pro', 'Expert']
    print('Vous avez choisi le niveau'+l_n[niveau])
    n=-1
    while n<=0:
     n=int(input("Choisissez un nombre total d'allumettes: "))
    while n>0:
        j=-1
        while j<1 or j>3 or j>n:
            j= int(input("Combien d'allumettes voulez vous retirez?"))
        n-=j
        if n==0:
            print("Vous avez perdu!")
        else:
            print("Il reste: ", n)
            p=AI_p(niveau, n)
            print("J'en prend ", p)
            n-=p
            print("Il en reste ", n)
            if n==0:
                print("J'ai perdu!")
    return 0

#2 joueurs humains
def deux_joueurs_humain():
    n=-1
    while n<=0:
     n=int(input("Joueur1, choisissez un nombre total d'allumettes: "))
    while n>0:
        j1=-1
        while j1<1 or j1>3 or j1>n:
            j1= int(input("Joueur1, combien d'allumettes voulez vous retirez?"))
        n-=j1
        if n==0:
            print("Joueur1, vous avez perdu!")
        else:
            print("Il reste: ", n)
            j2=-1
            while j2<1 or j2>3 or j2>n:
                j2= int(input("Joueur2, combien d'allumettes voulez vous retirez?"))
            n-=j2
            print("Il en reste ", n)
            if n==0:
                print("Joueur2, vous avez perdu!")
    return 0

#zero joueurs humain
def zero_joueurs_humain():
     #protection difficulté
    niveau1=5
    niveau2=5
    while niveau1>4 or niveau2>4:
        niveau1=  int(input("Quel niveau de dificultés pour ordi1? "))
        niveau2=  int(input("Quel niveau de dificultés pour ordi2? "))
    n=-1
    while n<=0:
     n=int(input("Choisissez un nombre total d'allumettes: "))
    while n>0:
        j=AI_p(niveau1, n)
        print('Ordi1 a choisit de retirer {} allumettes'.format(j))
        n-=j
        if n==0:
            print("Ordi1 a perdu!")
        else:
            print("Il reste: ", n)
            p=AI_p(niveau2, n)
            print("Ordi2 prend ", p)
            n-=p
            print("Il en reste ", n)
            if n==0:
                print("Ordi2 a perdu!")
    return 0

#strategie de jeu pour l'ordi selon le niveau de difficulté 
def AI_p(level, n):
    if level==0:
        p= random.randint(1,3)
    elif level==1:
        if n%4==3:
            p=2
        else:
            p=random.randint(1,3)
    elif level==2:
        if n%4==3:
            p=2
        elif n%4==2:
            p=1
        else:
            p=random.randint(1,3)
    if level==3:
        if n%4==3:
            p=2
        elif n%4==2:
            p=1
        elif n%4==0:
            p=3
        else:
            p=random.randint(1,3)
    else:
        if n%4==3: 
            p=2
        elif n%4==2:
            p=1
        elif n%4==0:
            p=3
        else: 
            p=1
    return p
    
        
        
if n_joueurs_humain==1:
    print("Vous jouez contre l'ordinateur!")
    un_joueurs_humain()
elif n_joueurs_humain==2:
    print("Vous jouez contre un autre joueur humain!")
    deux_joueurs_humain()
else:
    print("Vous etes spectateur!")
    zero_joueurs_humain()
