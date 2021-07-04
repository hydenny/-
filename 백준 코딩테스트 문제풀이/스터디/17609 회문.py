t = int(input())

def palindrome(word):
    count = 0
    while True:
        length = word.len()
        forward = 0
        backward = -1

        if word[forward] == word[backward]:
            forward += 1
            backward -= 1
            