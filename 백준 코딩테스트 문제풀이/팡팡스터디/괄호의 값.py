global start, result
start, result = 0, 0

def recur(string):
    global start, result

    value = 0

    if string[start] == '(':
        if string[start + 1] == ')':
            return 2 + recur(string[start + 2:])
        
        elif string[start + 1] == '(' or '[':
            return 2 * recur(string[start + 1])

        else:
            print(0)
            exit()

    if string[start] == '[':
        if string[start + 1] == ']':
            return 3 + recur(string[start + 2:])
        
        elif string[start + 1] == '(' or '[':
            return 3 * recur(string[start + 2:])

        else:
            print(0)
            exit()

string = str(input())

if string[start] == (')' or ']'):
    print(0)
    exit()

else:
    print(recur(string))