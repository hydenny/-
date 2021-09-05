x = []
y = []

for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

result = []

for i in x:
    if x.count(i) == 1:
        result.append(i)

for i in y:
    if y.count(i) == 1:
        result.append(i)

print(str(result[0]) + " " + str(result[1]))