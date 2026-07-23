#!/usr/bin/env python3

from sys import path

path.append("..\\modules")

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]

print(module.sum_list(zeroes))
print(module.product_list(ones))