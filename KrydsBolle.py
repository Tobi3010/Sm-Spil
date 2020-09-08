print("Kryds og Bolle!\n")

OArray = ["O", "O", "O"]
XArray = ["X", "X", "X"]
PlaceHolder = ["","",""]

def Horizontal(CopyCat, XArray, OArray, PlaceHolder):
    FullRow = False
    for n in range(3):
        if CopyCat[n] == OArray or CopyCat[n] == XArray:
            FullRow = True
    return FullRow

def Vertical(CopyCat, XArray, OArray, PlaceHolder):
    FullRow = False
    for n in range(3):
        for i in range(3):
            PlaceHolder[i] = CopyCat[i][n]
        if PlaceHolder == OArray or PlaceHolder == XArray:
            FullRow = True
    return FullRow

def Oblique(CopyCat, XArray, OArray, PlaceHolder):
    FullRow = False
    for n in range(3):
        PlaceHolder[n] = CopyCat[n][n]
    if PlaceHolder == OArray or PlaceHolder == XArray:
        FullRow = True

    for n in range(3):
        PlaceHolder[n] = CopyCat[n][2-n]
    if PlaceHolder == OArray or PlaceHolder == XArray:
        FullRoad = True
    return FullRow


Map = [["+", "+", "+"], ["+", "+", "+"], ["+", "+", "+"]]
game = True

n = 0
while game == True:
    n += 1
    if n % 2 == 0:
        Letter = "X"
    else:
        Letter = "O"

    txt = input("Where do you wanna play {}? ".format(Letter))

    if Map[int(txt[0])-1][int(txt[1])-1] == "+":
        Map[int(txt[0])-1][int(txt[1])-1] = Letter
        for x in range(3):
            for y in range(3):
                print(Map[x][y], end = " ")
            print("")
    else:
        n += -1

    if Horizontal(Map, XArray, OArray, PlaceHolder) == True or Vertical(Map, XArray, OArray, PlaceHolder) == True or Oblique(Map, XArray, OArray, PlaceHolder) == True:
        game = False

print("GAME OVER! PLAYER {} WON THE GAME".format(Letter))
