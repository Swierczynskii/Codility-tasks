# Only 44%

def solution(X, Y, D):
    
    counter = 0
    while True:
        if X == Y:
            break
        X = X + D
        counter = counter + 1
        if X > Y:
            break
    return counter