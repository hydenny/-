<<<<<<< HEAD
global Map

def star(n):
    if n == 3:
        Map[0][:3] = Map[2][:3] = ["*"] * 3
        Map[1][:3] = ["*", "" , "*"]

    

n = int(input())

Map = [["" for i in range(n)] for i in range(n)]

print(Map)
=======
def star(n):
    Map = [[''] * 9]

    if n == 3:
        Map[:3] = ['*', '*', '*']
        Map[3:6] = ['*', '', '*']
        Map[6:] = ['*', '*', '*']
    else:
        Map[:3] = [star(n // 3), star(n // 3), star(n // 3)]

    return Map

n = int(input())

for i in range(n // 3):
    for j in range(n // 3):
>>>>>>> 4d57034fcff68a76ee04754ed464331ac7c89623
