N, K = map(int, input().split())

queue = []
answer = 0

for i in range(N):
    number = int(input())
    queue.append(number)

for i in range(len(queue)):
    x = queue.pop()
    quotient = K // x
    K = K % x
    answer += quotient

print(answer)