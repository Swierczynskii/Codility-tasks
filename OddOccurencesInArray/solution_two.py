# only 66%

def solution(A):
    
    num_dict = {}

    for i in A:
        if i in num_dict:
            num_dict[i] = num_dict[i] + 1
        else:
            num_dict[i] = 1

    for key in num_dict:
        if num_dict[key] == 1:
            return key