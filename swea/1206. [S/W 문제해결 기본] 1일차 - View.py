T = 10
for test_case in range(1, T + 1):
    length = int(input())
    sticks = list(map(int, input().split()))
    result = 0
    
    for i in range(2, length - 2):
        flag = True
        pivot = sticks[i]
        while True:
            for j in range(-2, 3):
                if j == 0:
                    continue
                if pivot <= sticks[i + j]:
                    flag = False

            if flag == True:
                result += 1
                pivot -= 1
            else:
                break

    print("#" + str(test_case), result)