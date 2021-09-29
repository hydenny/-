n, l = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

start = 0
end = start + 1

count = 0
if n == 1:
    print(1)
    exit()
while end != n:    
    d = array[end] - array[start] + 1
    if d > l:
        count += 1
        start = end
        end = start + 1
    else:
        if end == n - 1:
            count += 1
        end += 1
    if start == n - 1:
        count += 1

print(count)