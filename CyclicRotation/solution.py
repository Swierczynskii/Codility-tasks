def solution(A, K):
    
    if not A:
        return A
        
    for _ in range(K):
        temp = A[len(A)-1]
        for i in range(len(A)-2, -1, -1):
            A[i+1] = A[i]
        A[0] = temp

    return A