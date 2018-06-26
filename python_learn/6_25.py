# -*- coding: utf-8 -*-
# @Time    : 18-6-25 下午7:49
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : 6_25.py
# @Software: PyCharm Community Edition

values = range(1,11) + 'Jack Queen King'.split()

suits = "diamonds clubs hearts spades".split()

deck = ["%s of %s" % (v,s) for v in values for s in suits]

from pprint import pprint

#pprint(deck[:12])

from random import shuffle
shuffle(deck)

pprint(deck[:52])

while deck:
    raw_input(deck.pop())