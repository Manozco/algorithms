#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: manu
# @Date:   2015-05-03 20:16:21
# @Last Modified by:   manu
# @Last Modified time: 2015-05-03 20:35:02


def insertion_sort(l: list):
    i, j, n = 0, 0, len(l)
    for i in range(n):
        j = i
        while ((j > 0) and (l[j] < l[j-1])):
            l[j], l[j-1] = l[j-1], l[j]
            j = j - 1


def test_insertion_sort(display: bool=False):
    s = "INSERTIONSORT"
    l = list(s)
    insertion_sort(l)
    if l != ['E', 'I', 'I', 'N', 'N', 'O', 'O', 'R', 'R', 'S', 'S', 'T', 'T']:
        raise ValueError
    if display:
        print(l)


def main():
    test_insertion_sort(True)

if __name__ == "__main__":
    main()
