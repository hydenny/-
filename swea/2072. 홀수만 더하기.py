T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc = list(map(int, input().split()))
    result = 0
    for i in tc:
    	if i % 2 != 0:
            result += i
    print("#" + str(test_case), result)