#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    list1 = [i for i in set_1 if i not in set_2]
    list2 = [i for i in set_2 if i not in set_1]
    return set(list1 + list2)
