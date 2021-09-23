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
