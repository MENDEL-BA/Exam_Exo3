import isproduitisnegatif as isn

while True:
        try:
            a=int(input("Entrer le premier nombre : :\t"))
            break
        except:
            print("Veuillez entrer un nombre !")

while True:
        try:
            b=int(input("Entrer le deuxieme nombre :\t"))
            break
        except:
            print("Veuillez entrer un nombre !")


isn.isProduitIsnegatif(a,b)