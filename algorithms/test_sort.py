#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Manuel VIVES
# @Date:   2015-05-04 14:23:26
# @Last Modified by:   Manuel VIVES
# @Last Modified time: 2015-05-04 14:24:43
from algorithms import sort


def test_insertion_sort(display: bool=True):
    s = "INSERTIONSORT"
    l = list(s)
    sort.insertion_sort(l)
    if l != ['E', 'I', 'I', 'N', 'N', 'O', 'O', 'R', 'R', 'S', 'S', 'T', 'T']:
        raise ValueError
    if display:
        print(l)


def test_bubble_sort(display: bool=True):
    s = "BUBBLESORT"
    l = list(s)
    sort.bubble_sort(l)
    if l != ['B', 'B', 'B', 'E', 'L', 'O', 'R', 'S', 'U', 'T']:
        raise ValueError
    if display:
        print(l)
