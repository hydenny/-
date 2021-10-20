global start, result
start, result = 0, 0

def round(string):
    global start

    if string[start + 1] == ']':
        print(0)
        exit()

    elif string[start + 1] == ')':
        start += 2
        print(result)
        return 2

    elif string[start + 1] == '(':
        start += 1
        print(result)        
        return 2 * round(string[start:])

    else:
        start += 1
        print(result)
        return 2 * angled(string[start:])

def angled(string):
    global start

    if string[start + 1] == ')':
        print(0)
        exit()

    elif string[start + 1] == ']':
        start += 2
        print(result)
        return 3

    elif string[start + 1] == '[':
        start += 1
        print(result)
        return 3 * angled(string[start:])

    else:
        start += 1
        print(result)
        return 3 * round(string[start:])

string = str(input())

if string[start] == (')' or ']'):
    print(0)
    exit()

else:
    result = 0

    while start != (len(string) - 1):
        if string[start] == '(':
            result += round(string[start:])

        else:
            result += angled(string[start:])

print(result)