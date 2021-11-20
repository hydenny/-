import sys

input = sys.stdin.readline

N = int(input())

stages = list(map(int, input().split()))

stage_count = {}

for i in range(N + 1):
    stage_count[i] = 0
    
for i in stages:
    if i == N + 1:
        for j in range(1, N + 1):
            stage_count[j] += 1
    else:
        stage_count[i] += 1
    
fail_rate = []

for i in stage_count:
    if 