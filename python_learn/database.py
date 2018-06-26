# -*- coding: utf-8 -*-
# @Time    : 18-6-25 下午7:59
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : database.py
# @Software: PyCharm Community Edition

import sys, shelve

def store_person(db):
    """
    query user for data and store it in the shelf object
    :param db: 
    :return: 
    """
    pid = raw_input("enter unique ID number")
    person = {}
    person['name'] = raw_input('enter name: ')
    person['age']  = raw_input('enter age: ')
    person['phone'] = raw_input('enter phone number: ')

    db[pid] = person

def lookup_person(db):
    "query user for ID and desired field."

    pid = raw_input('enter id number: ')
    field = raw_input('what would you like to know?(name, age, phone)')
    field = field.strip().lower()
    print field.capitalize() + ":" , db[pid][field]

def print_help():
    print 'the available commands are: '
    print 'store : stores info about a person'
    print 'lookup: looks up a person info from id number'
    print  'quit : save changes and exit'
    print '? : prints this message'

def enter_command():
    cmd  = raw_input('enter command(? for help) :')
    cmd  = cmd.strip().lower()
    return cmd

def main():
    database = shelve.open("/home/user/Disk1.8T/unicoe_notebook/python_learn/database.dat")
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:
        database.close()

if __name__ == '__main__':
    main()