N = int(input())

if N == 1:
    print("1 1")

else:
    plan = list(map(str, input().split()))

    pos = [1, 1]

    for i in plan:
        if i == 'R' and pos[1] != N:
            pos[1] += 1

        elif i == 'L' and pos[1] != 1:
            pos[1] -= 1

        elif i == 'U' and pos[0] != 1:
            pos[0] -= 1

        elif i == 'D' and pos[0] != N:
            pos[0] += 1

        else:
            continue

    print(pos[0], pos[1], end=" ")
