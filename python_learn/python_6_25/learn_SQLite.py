# -*- coding: utf-8 -*-
# @Time    : 18-6-25 下午8:50
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : learn_SQLite.py
# @Software: PyCharm Community Edition

import sqlite3
conn = sqlite3.connect('/home/user/Disk1.8T/unicoe_notebook/python_learn/python_6_25/database.db')

curs = conn.cursor()

conn.commit()

conn.close()