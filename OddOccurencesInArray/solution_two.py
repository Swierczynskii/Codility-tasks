def solution(A):
    
    num_dict = {}

    for i in range(len(A)):
        if A[i] in num_dict:
            num_dict[A[i]] = num_dict[A[i]] + 1
        else:
            num_dict[A[i]] = 1

    for key in num_dict:
        if num_dict[key] == 1:
            return key