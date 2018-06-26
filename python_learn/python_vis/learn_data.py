# -*- coding: utf-8 -*-
# @Time    : 18-6-25 下午10:11
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : learn_data.py
# @Software: PyCharm Community Edition

from matplotlib.pyplot import *

x = [1,2,3,4]
y = [4,2,3,1]

figure()

subplot(231)
plot(x,y)

subplot(232)
bar(x,y)

subplot(233)
barh(x, y)

subplot(234)
bar(x,y)

y1 = [7,8,5,3]
bar(x, y1, bottom=y, color='r')

subplot(235)
boxplot(x)

subplot(236)
scatter(x, y)

show()
