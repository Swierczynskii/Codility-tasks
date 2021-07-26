
def solution(A):
    
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if (A[i] == A[j]):
                A[i] = -1
                A[j] = -1
                break
    return max(A)