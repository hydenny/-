A, B = map(int, input().split())

count = 1

while B != A and B > A:
    if B % 2 == 0:
        B = B//2
        count += 1

    elif B % 10 == 1:
        B -= 1
        B = B//10
        count += 1

    else:
        break

if A == B:
    print(count)
else:
    print(-1)
