import sys

N = int(sys.stdin.readline().rstrip())

student = []

for i in range(N):
    name, score = sys.stdin.readline().rstrip().split()
    student.append((name, score))

student = sorted(student, key=lambda x: x[1])

for i in student:
    print(i[0], end=' ')