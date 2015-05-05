#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Manuel VIVES
# @Date:   2015-05-05 09:51:14
# @Last Modified by:   Manuel VIVES
# @Last Modified time: 2015-05-05 09:51:59


def min_quadratic(alist: list):
    min = alist[0]
    for i in alist:
        for j in alist:
            if j < i and j < min:
                min = j
    return min


def min_linear(alist: list):
    min = alist[0]
    for i in alist:
        if i < min:
            min = i
    return min
