N = int(input())

result = 0

for i in range(N + 1):
    case = 0
    if i % 10 == 3:
    # 0~23시 중 3이 들어간 시
        case = 3600


    else:
        for min in range(60):
            if min % 10 == 3 or min // 10 == 3:
            # 3이 들어간 분
                case += 60

            else:
                for sec in range(60):
                    if sec % 10 == 3 or sec // 10 == 3:
                    # 3이 들어간 초
                        case += 1

    result += case

print(result)