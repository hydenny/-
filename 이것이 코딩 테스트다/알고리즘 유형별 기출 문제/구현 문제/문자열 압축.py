def solution(s):
    answer = 0
    length = []

    for i in range(1, len(s) + 1):
        result = ""
        index = 0
        count = 1
        next = ""
        for j in range(len(s) // i):
            pre = s[index: index + i]
            next = s[index + i: index + 2 * i]
            if pre == next:
                count += 1
            else:
                if count == 1:
                    result += pre
                else:
                    result += (str(count) + pre)
                count = 1
            index += i

        if len(s) % i != 0:
            result += s[len(s) - len(s) % i:]
        else:
            result += next

        length.append(len(result))
    answer = min(length)

    return answer