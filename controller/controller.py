# _*_coding:utf-8
from model.model import Model
from view.view import View

class Controller(object):
    '''控制器层'''

    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        sudoku = self.model.get_sudoku();
        self.view.show_sudoku(sudoku);

        possibleList = self.model.possible_list_sudoku(sudoku)
        # self.view.show_possible_list_sudoku(possibleList);

        possibleList2 = self.model.analyse_sudoku(possibleList)
        self.view.show_possible_list_sudoku(possibleList2);
