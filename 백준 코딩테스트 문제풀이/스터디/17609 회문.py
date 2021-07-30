# 유사회문 검사 function
def inner_palindrome(input_str, start, end):
    while start < end:
        if input_str[start] == input_str[end]:
            start += 1
            end -= 1
        else:
            return False
    return True

def palindrome(input_str, start, end):
    while start < end:
        if input_str[start] == input_str[end]:
            start += 1
            end -= 1
        else:
            fc = inner_palindrome(input_str, start, end-1)
            sc = inner_palindrome(input_str, start+1, end)
            #  fc와 sc 둘 중에 하나를 만족한다면, 유사 회문이기 때문에 값 1을 반환해준다.
            if fc or sc:
                return 1
            else:
                return 2
    return 0


test_case = int(input())
for _ in range(test_case):
    input_str = input()
    print(palindrome(input_str, 0, len(input_str)-1))