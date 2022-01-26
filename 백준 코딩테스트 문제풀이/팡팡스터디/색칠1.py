import sys

input = sys.stdin.readline


def part():
    square = [[False] * (w - f) for _ in range(h // (c + 1))]
    for y in range(y1, y2):
        for x in range(x1, x2):
            square[y][x] = True
    return  square


def solution():
    gap = abs(2 * f - w)
    pivot = part()
    square_false = 0
    for y in range(y2):
        square_false += pivot[y].count(False)
    result = square_false * (c + 1)  
      
    if max(f, w - f) == w - f:
        remain = [[False] * (w - f - gap) for _ in range(y2)]
        square_false2 = 0
        for y in range(y2):
            for x in range(x2 - gap):
                remain[y][x] = pivot[y][x]
        for y in range(y2):
            square_false2 += remain[y].count(False)
        result += square_false2 * (c + 1)        
    else:
        result *= 2
        result += (gap * h)
    
    print(result)



w, h, f, c, x1, y1, x2, y2 = map(int, input().split())

solution()