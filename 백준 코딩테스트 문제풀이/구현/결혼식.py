n = int(input())
m = int(input())

direct = []
invited = []
friend = []

for i in range(m):
    buddy = list(map(int, input().split()))
    #친구 목록 리스트에 들어갈 비교 한 쌍
    friend.append(buddy)

friend_list = sorted(friend, key=lambda x: x[0])
#친구 목록을 한 쌍의 첫 사람에 대해 오름차순 정렬
#의문점: x[1]에 대해서도 같이 해줘야 하지 않나?
for i in range(m):
    if friend_list[i][0] == 1:
        invited.append(friend_list[i][1])
        direct.append(friend_list[i][1])
    #상근이가 포함된 경우 direct 직속 친구에 추가
    else:
        if friend_list[i][0] in direct:
            invited.append(friend_list[i][1])

        elif friend_list[i][1] in direct:
            invited.append(friend_list[i][0])

invited = set(invited)
#중복 제거

if 1 in invited:
    invited.remove(1)
#상근이가 포함될 경우 방지

print(len(invited))
