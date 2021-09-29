n, l = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

start = 0
end = start + 1

count = 0

while end != n:    
    #print(start, end, end=(" "))
    d = array[end] - array[start] + 1
    if d > l:
        if start == 0:
            count += 1
            start += 1
            end += 1
        else:
            count += 1
            start = end
            end = start + 1
    else:
        if end == n - 1:
            count += 1
        end += 1

print(count)