#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Manuel VIVES
# @Date:   2015-05-04 14:22:54
# @Last Modified by:   Manuel VIVES
# @Last Modified time: 2015-05-05 15:19:03


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
        for i in range(1, last):
            if l[i - 1] > l[i]:
                l[i], l[i-1] = l[i-1], l[i]
                swapped = True
        if not swapped:
            break


def merge_sort(a_list: list):
    if len(a_list) > 1:
        mid = len(a_list) // 2
        lefthalf = a_list[:mid]
        righthalf = a_list[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i, j, k = 0, 0, 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                a_list[k] = lefthalf[i]
                i = i + 1
            else:
                a_list[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            a_list[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            a_list[k] = righthalf[j]
            j = j + 1
            k = k + 1
