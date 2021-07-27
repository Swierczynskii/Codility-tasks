

def solution(A):
    
    if not A:
        return 1
        
    B = []
    max_A = max(A)

    for i in range(0, max_A+1):
        B.append(i)

    if sum(B) == sum(A):
        B.append(max_A+1)
        
    return(sum(B) - sum(A))