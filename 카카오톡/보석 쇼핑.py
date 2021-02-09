def solution(gems):
    answer = []

    name = []  # gems의 요소 종류 개수를 알기 위한 list

    plan = []  # dist를 매기는 case들에 대한 리스트

    for i in gems:
        if i not in name:
            name.append(i)

    count = len(name)

    if count == 1:
        answer = [1, 1]
        return answer

    else:
        for n in range(len(gems) - len(name) + 1):  # 마지막 case에 대해서, 한번에 이어서 모든 종류가 나올 수 있을 경우까지만 고려
            dist = 0
            start = 0
            end = 0
            name_check = 0  # name의 요소를 gems에서 처음 확인할때 1을 더해 업데이트해줌
            check = []

            for i in range(1, len(gems) + 1):
                if name_check != count:
                    if gems[i - 1] in name and gems[i - 1] not in check:
                        check.append(gems[i - 1])
                        if name_check == 0:
                            start = i

                        elif name_check == count - 1:
                            end = i

                        name_check += 1

                    if start != 0:
                        dist += 1

            if name_check != count:
                continue

            plan.append([dist, [start, end]])  # 1 case 생성
            gems[n] = 0  # gems의 확인한 case의 start 요소를 name에 속하지 않을 0으로 바꿔줌

        plan.sort()
        print(plan)
        answer = plan[0][1]

    return answer