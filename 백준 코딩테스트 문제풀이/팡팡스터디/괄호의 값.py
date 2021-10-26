global idx, result
start, result = 0, 0

def recur(idx):
    global result, start

    if string[idx] == '(':
        if string[idx + 1] == ')':
            idx += 2
            result += (2 + recur(idx))

        elif string[idx + 1] == '(' or '[':
            idx += 1
            result += 2 * recur(idx)

        else:
            print(0)
            exit()

    elif string[idx] == '[':
        if string[idx + 1] == ']':
            idx += 2
            result += (3 + recur(idx))

        elif string[idx + 1] == '(' or '[':
            idx += 1
            result += 3 * recur(idx)

        else:
            print(0)
            exit()

    return result


string = str(input())

if string[start] == (')' or ']'):
    print(0)
    exit()

else:
    answer = 0

    

    print(recur(start))