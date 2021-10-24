global start, result
start, result = 0, 0

def recur(string):
    global start, result

    value = 0

    if string[start] == '(':
        if string[start + 1] == ')':
            start += 2
            result = 2 + recur(string[start:])
        
        elif string[start + 1] == '(' or '[':
            start += 1
            return 2 * recur(string[start:])

        else:
            print(0)
            exit()

    if string[start] == '[':
        if string[start + 1] == ']':
            start += 2
            return 3 + recur(string[start:])
        
        elif string[start + 1] == '(' or '[':
            start += 1
            return 3 * recur(string[start:])

        else:
            print(0)
            exit()

string = str(input())

if string[start] == (')' or ']'):
    print(0)
    exit()

else:
    print(recur(string))