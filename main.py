#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: manu
# @Date:   2015-05-03 20:16:21
# @Last Modified by:   Manuel VIVES
# @Last Modified time: 2015-05-05 13:29:32
from algorithms import sort
from algorithms import min
from algorithms import search

import random
import time


def compute_time(msg, cb, *args, **kwargs):
    start_time = time.time()
    ret = cb(*args, **kwargs)
    end_time = time.time()
    print("{0:.3f}secs - {1}".format(end_time - start_time, msg))
    return ret


def main():
    len_l = random.randint(1000, 10000)
    l = [random.randint(1000, 1000000) for i in range(len_l)]
    compute_time("BubbleSort", sort.bubble_sort, l)

    idx_key = random.randint(0, len(l) - 1)
    key = l[idx_key]
    print("Key: ", key, idx_key)
    i = compute_time("BinarySearch", search.binary_search, l, key)
    if i:
        print(l[i], key)

    i = compute_time("LinearSearch", search.linear_search, l, key)
    if i:
        print(l[i], key)

    # print(l)

if __name__ == "__main__":
    main()
