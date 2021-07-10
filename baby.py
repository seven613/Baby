#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :Baby.py
@说明        :
@时间        :2021/07/10 16:43:17
@作者        :张强
@版本        :1.0
'''

from parent import Daddy, Mommy
from utils import show, count_down


class Baby(Daddy, Mommy):
    def __init__(self):
        Daddy.__init__(self)
        Mommy.__init__(self)

        self.myName = ''
        self.myBirthday = ''
        self.myGender = ''

        self.__create()

    def __create(self):
        self.myName = '张荣彧'
        self.myBirthday = '2021 年 7 月 12 日'
        if(Daddy.provide_gene(self) == 'Y' and Mommy.provide_gene(self) == 'X'):
            self.myGender = 'Boy'
        else:
            self.myGender = 'Girl'
        self.myWords = 'Hello World!'


if __name__ == '__main__':
    count_down(3, 'D')
    me = Baby()
    show(me.myName, me.myBirthday, me.myGender, me.myWords)
    count_down(3, 'A')
