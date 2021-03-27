import sys

N = map(int, sys.stdin.readline().rstrip())

order = list(N)

length = len(order)

if sum(order[:length//2]) == sum(order[length//2:length]):
    print("LUCKY")
else:
    print("READY")