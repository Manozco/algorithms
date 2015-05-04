#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: manu
# @Date:   2015-05-03 20:16:21
# @Last Modified by:   Manuel VIVES
# @Last Modified time: 2015-05-04 10:50:50


def insertion_sort(l: list):
    i, j, n = 0, 0, len(l)
    for i in range(n):
        j = i
        while ((j > 0) and (l[j] < l[j-1])):
            l[j], l[j-1] = l[j-1], l[j]
            j = j - 1


def test_insertion_sort(display: bool=True):
    s = "INSERTIONSORT"
    l = list(s)
    insertion_sort(l)
    if l != ['E', 'I', 'I', 'N', 'N', 'O', 'O', 'R', 'R', 'S', 'S', 'T', 'T']:
        raise ValueError
    if display:
        print(l)


def bubble_sort(l: list):
    last = len(l)
    while True:
        swapped = False
        for i in range(1, last - 1):
            if l[i - 1] > l[i]:
                l[i], l[i-1] = l[i-1], l[i]
                swapped = True
        if not swapped:
            break


def test_bubble_sort(display: bool=True):
    s = "BUBBLESORT"
    l = list(s)
    bubble_sort(l)
    if l != ['B', 'B', 'B', 'E', 'L', 'O', 'R', 'S', 'U', 'T']:
        raise ValueError
    if display:
        print(l)


def main():
    test_bubble_sort()

if __name__ == "__main__":
    main()
