#!/usr/bin/python3
def uniq_add(my_list=[]):
    sums = 0
    flag = True
    if my_list:
        for i in range(len(my_list)):
            flag = True
            for j in range(i + 1, len(my_list)):
                if my_list[i] == my_list[j]:
                    flag = False
                    break
            if flag:
                sums += my_list[i]
        return sums
    else:
        return sums
