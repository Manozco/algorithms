#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Manuel VIVES
# @Date:   2015-05-04 14:22:54
# @Last Modified by:   Manuel VIVES
# @Last Modified time: 2015-05-04 14:24:48


def insertion_sort(l: list):
    i, j, n = 0, 0, len(l)
    for i in range(n):
        j = i
        while ((j > 0) and (l[j] < l[j-1])):
            l[j], l[j-1] = l[j-1], l[j]
            j = j - 1


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


