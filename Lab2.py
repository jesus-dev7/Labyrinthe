import time
import tkinter as tk

lab=[["x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x"],
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
    ["x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x"]]

def TrouverCoos(Ob):
    NbX = -1
    NbY = -1
    for Elem in lab:
        NbX = -1
        NbY +=1
        if Ob in Elem:
            for Truc in Elem:
                NbX += 1
                if Truc == Ob:
                    return([NbX, NbY])
                
ActCoo = TrouverCoos("E")
CoosS = TrouverCoos("S")

def PathFinder():
    
    def CreerPile():
        global Pile
        Pile = []
    CreerPile()
    def AddPile(Chose):
        global Pile
        Pile.append(Chose)
    AddPile(ActCoo.copy())
    print(ActCoo)
    def DelPile():
        global Pile
        Pile.pop(-1)
        
    def CreerPile2():
        global Pile2
        Pile2 = []
    CreerPile2()
    def AddPile2(Chose):
        global Pile2
        Pile2.append(Chose)
    def DelPile2():
        global Pile2
        Pile2.pop(-1)
    def ExPile2(Pile2):
        Pile2[-1]()
        DelPile2()
        
        

    def Tour():
        """Tour de recherche de case vide.
        """
        global ActCoo
        CreerPile2()
        
        def Droite():
            global Val, x, y
            global ActCoo
            x, y = ActCoo[0]+1, ActCoo[1]
            Val = lab[y][x]
        
        def Gauche():
            global Val, x, y
            global ActCoo
            x, y = ActCoo[0]-1, ActCoo[1]
            Val = lab[y][x]
        
        def Bas():
            global Val, x, y
            global ActCoo
            x, y = ActCoo[0], ActCoo[1]+1
            Val = lab[y][x]
        
        def Haut():
            global Val, x, y
            global ActCoo
            x, y = ActCoo[0], ActCoo[1]-1
            Val = lab[y][x]

        AddPile2(Haut)
        AddPile2(Gauche)
        AddPile2(Bas)
        AddPile2(Droite)
        
        global Val
        Val = None
        
        def Test():
            global ActCoo
            if Val == "0" or Val == "S":
                lab[y][x] = "."
                ActCoo = [x, y]
                AddPile(ActCoo.copy())
                print(ActCoo)
                return True
            return False
        
        
        def Cds():
            global ActCoo
            global Pile
            if len(Pile) > 1:
                Prems = Pile[-1][0]
                Deus = Pile[-1][1]
                lab[Deus][Prems] = "C"
                DelPile()
                ActCoo = Pile[-1]
            else:
                return
            
        def Course():
            global ActCoo
            while len(Pile2)>0:
                ExPile2(Pile2)
                if Test() == True:break
            else:
                Cds()
        Course()
        for ligne in lab:
            print(ligne)
        time.sleep(0.01)
        if ActCoo != CoosS:
            print(Tour())
    print(Tour())
        
print(PathFinder())

def Interface():
    
    root = tk.Tk()
    root.geometry('800x600')
    root.title('Canvas Demo - Rectangle')

    canvas = tk.Canvas(root, width=600, height=400, bg='white')
    canvas.grid(column=0, row=0)
    
    class Cubes:
        def __init__(self, k, j, color):
            self.k = int(k)
            self.j = int(j)
            self.color = color
        def Creer(self):
            canvas.create_rectangle(((self.k)*10, (self.j)*10), ((self.k+20)*10, (self.j+20)*10), fill=color)
            
    for j in range(len(lab)):
        for k in range(len(lab[j])):
            if lab[j][k] == "x":
                color = "black"
            elif lab[j][k] == "C":
                color = "yellow"
            elif lab[j][k] == ".":
                color = "red"
            elif lab[j][k] == "E":
                color = "blue"
            else:
                color = "green"
            cubes = Cubes(k, j, color)
            cubes.Creer()

    root.mainloop()

Interface()