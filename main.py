#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: manu
# @Date:   2015-05-03 20:16:21
# @Last Modified by:   Manuel VIVES
# @Last Modified time: 2015-05-05 09:52:31
from algorithms import test_sort
from algorithms import min


def main():
    test_sort.test_bubble_sort()
    l = [-1, -4, 4, 10, 12, -6, 12]
    print(min.min_quadratic(l))
    print(min.min_linear(l))

if __name__ == "__main__":
    main()
