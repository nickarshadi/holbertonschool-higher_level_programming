#!/usr/bin/python3
'''Module for MyList class.'''


class MyList(list):
    '''MyList class.'''
    def print_sorted(self):
        '''Print sorted list.'''
        print(sorted(self))
