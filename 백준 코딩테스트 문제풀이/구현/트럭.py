n, w, L = map(int, input().split())

truck = list(map(int, input().split()))

time = 0    #걸리는 시간

count = 0   #다리에 올라있는 트럭의 수
total_weight = 0    #다리에 올라간 트럭 무게 총합
truck_list = []     #다리에 올라간 트럭 무게 목록
if n == 1:
    print(w + 1)
else:
    for i in range(n):
        if count == w:
        #다리에 오를 트럭 수가 다 찬 경우
            total_weight -= truck_list[0]
            truck_list.pop(0)
            count -= 1
            #time += 1
            #print(truck_list)
        if count < w:
        #다리에 트럭이 더 오를 공간이 있는 경우
            if total_weight + truck[i] > L:
            #트럭 추가했을 시 무게 넘칠 경우
                time += (w - 1)
                total_weight -= truck_list[0]
                count -= 1
                truck_list.pop(0)
                #print(truck_list*(w-1))

            #트럭 무게가 최대하중 이하일 경우 트럭 추가
            truck_list.append(truck[i])
            total_weight += truck[i]
            count += 1
            #time += 1
            #print(truck_list)
        time += 1
    time += w

    print(time)