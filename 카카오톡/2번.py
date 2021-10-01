Max = 1000000
def change_to_k(n, k):
    n = int(n)
    result = ''
    while n > 0:
        remainder = n % k
        n //= k
        result += str(remainder)
    
    return result[::-1]

def eratos():
    array = [True] * Max
    for i in range(2, int(Max ** 0.5) + 1):
        if array[i] == True:
            for j in range(2 * i, Max, i):
                array[j] = False
    array = [i for i in range(2, Max) if array[i] == True]
    
    return array

def solution(n, k):
    answer = 0
    
    prime = eratos()
    #print(prime)
    number = change_to_k(n, k)
    print(number)
    number = list(number.split('0'))

    #print(number)
    for i in number:
        if i == '':
            continue
        if int(i) in prime:
            answer += 1
            
    return answer

n, k = map(int, input().split())

print(solution(n, k))