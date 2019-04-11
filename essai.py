from random import*
n= randint(0,9)
cpt = 3
while cpt > 0:
	x = int(input("devinez le nombre"))
	if x == n:
		print ("bravo, le nombre choisi est bon")
	elif x != n:
		print("mauvaise choix veillez réessayer")
	cpt -= 1
else:
        print("désoler le jeu est terminé")
