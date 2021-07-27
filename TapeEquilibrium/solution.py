# Not the best performance - 53%

def solution(A):

    scores = [] 

    for i in range(0,len(A)):
        sum_j = 0
        sum_k = 0
        if i == 0:
            pass
        else:
            for j in range(0,i):
                sum_j = sum_j+A[j]
            for k in range(i, len(A)):
                sum_k = sum_k+A[k]
            scr = abs(sum_j-sum_k)
            scores.append(scr)

    return min(scores)