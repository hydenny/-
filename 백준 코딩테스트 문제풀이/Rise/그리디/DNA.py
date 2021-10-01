n, m = map(int, input().split())

count = {'A':0, 'T':0, 'G':0, 'C':0}
words = []

for i in range(n):
    words.append(str(input()))

for i in range(n):
    count[words[i][0]] += 1