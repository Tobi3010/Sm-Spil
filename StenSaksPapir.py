import random

print("Sten Saks Papir!")




i = ["Saks", "Sten"]
n = ["Sten", "Papir"]
k = ["Papir", "Saks"]
List = [i,n,k]

Enemy = List[random.randint(0, 2)][0]
print(Enemy)

print(List[0][1])
