t = int(input())

def match():
    h, w, n = map(int, input().split())

    if n % h != 0:
        number = n // h + 1
        floor = n % h
    else:
        number = n // h
        floor = h

    if number >= 10:
        new_number = str(number)
    else:
        new_number = "0" + str(number)

    print(str(floor) + new_number)

for i in range(t):
    match()