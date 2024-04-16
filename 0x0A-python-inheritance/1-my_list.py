#!/usr/bin/python3
''' 1. My list '''


class MyList(list):
    ''' class MyList '''
    def print_sorted(self):
        '''  prints the list, but sorted '''
        sortedList = self[:]
        sortedList.sort()
        print(sortedList)
