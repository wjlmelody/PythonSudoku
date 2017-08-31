# _*_coding:utf-8
from database.database import *  # 导入数据

class Model(object):
    '''模型层'''

    def get_sukudo(self):
        return Sudoku;