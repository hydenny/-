import sys
from collections import deque

input = sys.stdin.readline


def clean_top(top):
    route = deque([])
    for x in room[top][1:]:
        route.append(x)
    for y in range(top - 1,0,-1):
        route.append(room[y][c - 1])
    for x in range(c - 1,0,-1):
        route.append(room[0][x])
    for y in range(0,top):
        route.append(room[y][0])

    x = route.pop()
    route = route.appendleft(x)
    print(route)
    room[top][1] = 0
    
    
    return


def clean_room(top, bottom):
    clean_top(top)
    return


def get_aircleaner_pos(r):
    for i in range(r):
        if room[i][0] == -1:
            return i, i + 1


def solution(r, c, t):
    top, bottom = get_aircleaner_pos(r)
    print(top, bottom)
    clean_top(top)


r, c, t = map(int, input().split())
room = []
for _ in range(r):
    room.append(list(map(int, input().split())))
print(solution(r, c, t))