import sys

m = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())

result = set()

if m == 1:
    m = 2

for i in range(m, n + 1):
    
    flag = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            flag = False
            break
    if flag == True:
        result.add(i)
if result == set():
    print(-1)
    quit()
print(sum(result))
print(min(result))