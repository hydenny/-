def solution(id_list, report, k):
    answer = [0] * len(id_list)

    if len(id_list) == 2:
        return [0, 0]

    reported = []

    report = set(report)
    report = list(report)
    print(report)
    for i in range (len(report)):
        reported.append(report[i][1])
    print(reported)
    banned = []

    for i in id_list:
        banned.append(reported.count(i))
    print(banned)
    for i in id_list:
        for j in report:
            if j[0] == i:
                if banned[(id_list.index(j[1]))] >= k:
                    answer[id_list.index(j[1])] += 1
    
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k))