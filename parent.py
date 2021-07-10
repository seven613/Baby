#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :daddy.py
@说明        :
@时间        :2021/07/09 15:31:36
@作者        :张强
@版本        :1.0
'''


class Daddy:
  def __init__(self) -> None:
      self.dadName='张  强'

  def provide_gene(self):
    return 'Y'

class Mommy:
  def __init__(self) -> None:
      self.momName='肖敬文'

  def provide_gene(self):
    return 'X'