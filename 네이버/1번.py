def min_index(card):
    return card.index(min(card))

def second_value(card):
    min_card = min(card)
    max_card = max(card)

    max_index = card.index(max(card))
    for i in range(3):
        if i != min_index(card):
            if i != max_index:
                return card[i]

def solution(cards):
    score = []

    number = len(cards)

    changed = [False] * number 

    for i in range(number):
        for j in range(number):
            if i == j:
                break
            if changed[i] == True:
                break    
            if changed[j] == True:
                continue

            one = cards[i]
            two = cards[j]

            one_second = second_value(cards[i])
            two_second = second_value(cards[j])

            if min_index(one) == min_index(two):
                continue
            elif min_index(one) == two.index(two_second) and two_second == (min(two) + 1) or two_second == min(two):
                continue                        
            elif min_index(two) == one.index(one_second) and one_second == (min(one) + 1) or one_second == min(one):
                continue
            else:
                cards[i][min_index(one)] += 1
                cards[j][min_index(two)] += 1
                changed[i], changed[j] = True, True

    for i in cards:
        score.append(min(i))

    answer = sum(score)
    return answer