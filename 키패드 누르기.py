def solution(numbers, hand):
    answer = ''

    left_position = ['10']#     * 대신 씀(int형으로 맞춰주기 위함)
    right_position = ['12']#    # 대신 씀
    result = []

    for i in range(len(numbers)):
        if numbers[i] == 0:
            numbers[i] = 11
    #print(numbers)
    #for i in numbers로 해서 계속 틀리게 나왔음.
    #for문에 대한 정확한 쓰임 알아둘 것.

    for i in numbers:   # 1 4 7 10(*)
        if i%3 == 1:
            left_position.pop()
            result.append('L')
            left_position.append(str(i))

        elif i%3 == 0:  # 3 6 9 12(#)
            right_position.pop()
            result.append('R')
            right_position.append(str(i))

        else:   # 2 5 8 11(0)
            if int(left_position[0]) == i:
                left_dist = 0

            elif int(left_position[0])%3 == 2:
                left_dist = abs(int(left_position[0]) - i)//3

            else:
                if abs(int(left_position[0]) + 1 - i)//3 == 0:
                    left_dist = 1

                elif abs(int(left_position[0]) + 1 - i)//3 == 1:
                    left_dist = 2

                elif abs(int(left_position[0]) + 1 - i)//3 == 2:
                    left_dist = 3

                else:
                    left_dist = 4

            if int(right_position[0]) == i:
                right_dist = 0

            elif int(right_position[0])%3 == 2:
                right_dist = abs(int(right_position[0]) - i)//3

            else:
                if abs(int(right_position[0]) - 1 - i)//3 == 0:
                    right_dist = 1

                elif abs(int(right_position[0]) - 1 - i)//3 == 1:
                    right_dist = 2

                elif abs(int(right_position[0]) - 1 - i)//3 == 2:
                    right_dist = 3

                else:
                    right_dist = 4

            if left_dist == right_dist:
                if hand == "right":
                    right_position.pop()
                    result.append('R')
                    right_position.append(str(i))

                else:
                    left_position.pop()
                    result.append('L')
                    left_position.append(str(i))

            elif left_dist > right_dist:
                right_position.pop()
                result.append('R')
                right_position.append(str(i))

            else:
                left_position.pop()
                result.append('L')
                left_position.append(str(i))



    for i in result:
        answer = answer + i

    return answer