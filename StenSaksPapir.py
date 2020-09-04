import random

print("Sten Saks Papir!")

i = ["Saks", "Sten"]
n = ["Sten", "Papir"]
k = ["Papir", "Saks"]
List = [i,n,k]

EnemyPoints = 0
PlayerPoints = 0
game = True

while game == True:
    Enemy = List[random.randint(0, 2)][0]
    print(Enemy)
    Player = input("Hvad spiller du? ")

    for x in range(3):
        if Player in List[x] and Enemy in List[x]:
            if List[x][0] == Enemy and Player != Enemy:
                PlayerPoints = PlayerPoints + 1
                print("Player won!")
            elif List[x][0] == Player and Player != Enemy:
                EnemyPoints = EnemyPoints + 1
                print("Enemy won!")
    if EnemyPoints == 3 or PlayerPoints == 3:
        game = False
print("GAME OVER")
