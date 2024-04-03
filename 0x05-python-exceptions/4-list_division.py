#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    c = []
    for i in range(list_length):
        try:
            c.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            c.append(0)
        except TypeError:
            print("wrong type")
            c.append(0)
        except IndexError:
            print("out of range")
            c.append(0)
        finally:
            continue
    return c
