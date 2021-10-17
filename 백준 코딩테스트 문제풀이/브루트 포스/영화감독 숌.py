n = int(input())

result = "666"

if n != 1:
    head = "0"
    tail = "0"

    count = 0

    while count != n:
        if int(head + result) < int(result + tail):
            result = head + result
            head = str(int(head) + 1)
            count += 1

        else:
            result = result + tail
            tail = str(int(tail) + 1)
            count += 1

print(result)