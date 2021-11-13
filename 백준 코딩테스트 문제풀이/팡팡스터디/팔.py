l, r = map(str, input().split())

if l == r or len(l) == 1:
    print(l.count('8'))
    
else:
    idx = 0
    count = 0
    while idx < len(l):
        if l[idx] == 8 or r[idx] == 8:
            if l[idx] != r[idx]:
                print(count)
                exit()
        count += 1
        idx += 1
    print(count)