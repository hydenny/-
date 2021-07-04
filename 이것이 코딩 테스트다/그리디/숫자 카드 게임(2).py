n, m = map(int, input().split())

minimum = []

for i in range(n):
    cards = list(map(int, input().split()))
    minimum.append(min(cards))

print(max(minimum))