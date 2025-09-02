Lab = [
    ["x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x"],
    ["x","S","0","0","x","0","0","0","x","0","0","0","x","0","0","0","0","0","0","x"],
    ["x","x","x","0","x","0","x","0","x","0","x","0","x","0","x","x","x","x","0","x"],
    ["x","0","0","0","0","0","x","0","0","0","x","0","0","0","x","0","0","x","0","x"],
    ["x","0","x","x","x","0","x","x","x","0","x","x","x","0","x","0","x","x","0","x"],
    ["x","0","0","0","x","0","0","0","x","0","0","0","x","0","0","0","x","0","0","x"],
    ["x","x","x","0","x","x","x","0","x","x","x","0","x","x","x","0","x","0","x","x"],
    ["x","0","0","0","x","0","0","0","0","0","0","0","x","0","0","0","x","0","0","x"],
    ["x","0","x","x","x","0","x","x","x","x","x","0","x","x","x","0","x","x","0","x"],
    ["x","0","x","0","0","0","x","0","0","0","x","0","0","0","x","0","0","x","0","x"],
    ["x","0","x","x","x","0","x","x","x","0","x","x","x","0","x","x","0","x","0","x"],
    ["x","0","0","0","x","0","0","0","x","0","0","0","x","0","0","x","0","x","0","x"],
    ["x","x","x","0","x","x","x","0","x","x","x","0","x","x","0","x","0","x","0","x"],
    ["x","0","0","0","0","0","x","0","0","0","x","0","0","0","0","x","0","x","0","x"],
    ["x","0","x","x","x","0","x","x","x","0","x","x","x","x","0","x","0","x","0","x"],
    ["x","0","x","0","0","0","0","0","x","0","0","0","0","x","0","x","0","x","0","x"],
    ["x","0","x","0","x","x","x","0","x","x","x","x","0","x","0","x","0","x","0","x"],
    ["x","0","0","0","x","0","0","0","0","0","0","x","0","x","0","0","0","x","0","x"],
    ["x","x","x","0","x","x","x","x","x","x","0","x","x","x","x","x","0","x","E","x"],
    ["x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x"],
]

def Trouver_Entree():
    for ind in range(len(Lab)):
        Liste = Lab[ind]
        for i in range(len(Liste)):
            if Liste[i] == "E":
                Y = ind
                X = i
                Liste[i] = "."
    print("X:", X)
    print("Y:", Y)
    return([X, Y])

tup = Trouver_Entree()

def Verifier_nature(Coos):
    X = Coos[0]
    Y = Coos[1]
    Cible1 = Lab[Y]
    Point_A_Verifier = Cible1[X]
    return(Point_A_Verifier)
    
print(Verifier_nature(tup))

def Verif_droite(coos):
    X = coos[0]
    Y = coos[1]
    NewCoos = (X + 1, Y)
    return(Verifier_nature(NewCoos))

def Verif_gauche(coos):
    X = coos[0]
    Y = coos[1]
    NewCoos = (X - 1, Y)
    return(Verifier_nature(NewCoos))

def Verif_haut(coos):
    X = coos[0]
    Y = coos[1]
    NewCoos = (X, Y - 1)
    return(Verifier_nature(NewCoos))

def Verif_bas(coos):
    X = coos[0]
    Y = coos[1]
    NewCoos = (X, Y + 1)
    return(Verifier_nature(NewCoos))

liste = []
def ajouter_pile(chose):
    liste.append(chose)
def enlever_pile():
    liste.pop(len(liste) - 1)

def Cul_De_Sac():
    x = liste[len(liste) - 1][0]
    y = liste[len(liste) - 1][1]
    NvCoos = [x, y]
    enlever_pile()
    print(liste)
    val = Verif_droite(NvCoos)
    if val == "x" or val == "." or val == "v":
        val = Verif_gauche(NvCoos)
        if val == "x" or val == "." or val == "v":
            val = Verif_haut(NvCoos)
            if val == "x" or val == "." or val == "v":
                val = Verif_bas(NvCoos)
                if val == "x" or val == "." or val == "v":
                    print("Cul de sac.")
                    Lab[y][x] = "v"
                    Cul_De_Sac()
                else:
                    NvCoos[1] = y + 1
                    print(NvCoos[1])
                    if val != "S":
                        Verif_autour(NvCoos)
                    else:
                        print("Victoire !")
            else:
                NvCoos[1] = y - 1
                print(NvCoos[1])
                if val != "S":
                    Verif_autour(NvCoos)
                else:
                    print("Victoire !")
        else:
            NvCoos[0] = x - 1
            print(NvCoos[0])
            if val != "S":
                Verif_autour(NvCoos)
            else:
                print("Victoire !")
    else:
        NvCoos[0] = x + 1
        print(NvCoos[0])
        if val != "S":
            Verif_autour(NvCoos)
        else:
            print("Victoire !")

def Verif_autour(coos_):
    print(coos_)
    X = coos_[0]
    Y = coos_[1]
    Lab[Y][X] = "."
    ajouter_pile(coos_.copy())
    print(liste)
    val = Verif_droite(coos_)
    if val == "x" or val == ".":
        val = Verif_gauche(coos_)
        if val == "x" or val == ".":
            val = Verif_haut(coos_)
            if val == "x" or val == ".":
                val = Verif_bas(coos_)
                if val == "x" or val == ".":
                    print("Cul de sac.")
                    Cul_De_Sac()
                else:
                    coos_[1] = Y + 1
                    print(coos_[1])
                    if val != "S":
                        Verif_autour(coos_)
                    else:
                        print("Victoire !")
            else:
                coos_[1] = Y - 1
                print(coos_[1])
                if val != "S":
                    Verif_autour(coos_)
                else:
                    print("Victoire !")
        else:
            coos_[0] = X - 1
            print(coos_[0])
            if val != "S":
                Verif_autour(coos_)
            else:
                print("Victoire !")
    else:
        coos_[0] = X + 1
        print(coos_[0])
        if val != "S":
            Verif_autour(coos_)
        else:
            print("Victoire !")
print(Verif_autour(tup))
for n in range(len(Lab)):
    print(Lab[n])