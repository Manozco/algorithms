#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Manuel VIVES
# @Date:   2015-05-05 12:30:33
# @Last Modified by:   Manuel VIVES
# @Last Modified time: 2015-05-05 13:29:16


def binary_search(sorted_list: list, key, imin=None, imax=None):
    imin = imin if imin is not None else 0
    imax = imax if imax is not None else len(sorted_list) - 1
    if imax < imin:
        return None
    else:
        imid = imin + ((imax - imin) // 2)
        if sorted_list[imid] > key:
            return binary_search(sorted_list, key, imin, imid - 1)
        elif sorted_list[imid] < key:
            return binary_search(sorted_list, key, imid + 1, imax)
        else:
            return imid


def linear_search(sorted_list: list, key):
    for i, v in enumerate(sorted_list):
        if v == key:
            return i
        elif v > key:
            return None
