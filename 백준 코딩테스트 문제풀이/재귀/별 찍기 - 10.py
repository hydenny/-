global Map

def star(n):
    if n == 3:
        Map[0][:3] = Map[2][:3] = ["*"] * 3
        Map[1][:3] = ["*", "" , "*"]

    

n = int(input())

Map = [["" for i in range(n)] for i in range(n)]

print(Map)