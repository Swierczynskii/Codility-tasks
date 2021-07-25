def solution(N):
    bin_num = bin(N).replace('0b', '')
    flag = 0
    counter = 0
    max_c = []

    for i in bin_num:
        if i == '1' and flag == 0:
            flag = 1
        if i == '0':
            counter = counter+1
        if i == '1' and flag == 1:
            max_c.append(counter)
            flag = 0
            counter = 0

    return max(max_c)