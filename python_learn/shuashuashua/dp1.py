# -*- coding: utf-8 -*-
# @Time    : 18-6-26 下午8:35
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : dp1.py
# @Software: PyCharm Community Edition

#python2 实现
# N = int(input().strip())
#
# ab = map(int, input().strip().split(' '))
#
# (K, D) = map(int, input().split(' '))
#
# dmax = [[0]*N for i in range(K)]
# dmin = [[0]*N for i in range(K)]
#
# res = (1<<64) -1
#
# print(res)
#
# for i in range(N):
#     dmax[0][i] = dmin[0][i] = ab[i]
#     for k in range(1, K):
#         for pre in range(max(0, i-D), i):
#             dmax[k][i] = max(dmax[k][i],
#                              max(dmax[k-1][pre]*ab[i], dmin[k-1][pre]*ab[i]))
#             dmin[k][i] = min(dmin[k][i], min(dmax[k-1][pre]*ab[i], dmin[k-1][pre]*ab[i]))
#         res = max(res, dmax[K-1][i])
#     print(res)

import sys
a = []

for line in sys.stdin:
    if line.strip() == '':
        break
    a.extend(line.split())
print(len(set(a)))
