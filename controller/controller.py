# _*_coding:utf-8
from model.model import Model
from view.view import View

class Controller(object):
    '''控制器层'''

    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        sudoku = self.model.get_sudoku()
        self.view.show_sudoku(sudoku)

        possibleList = self.model.possible_list_sudoku(sudoku)
        fill_in_number_store = self.model.fill_in_number(possibleList)
        self.view.show_fill_in_number(fill_in_number_store)

        while True:
            possibleList = self.model.analyse_sudoku(possibleList)
            fill_in_number = self.model.fill_in_number(possibleList)
            self.view.show_fill_in_number(fill_in_number)

            if fill_in_number_store == fill_in_number:
                self.view.show_possible_list_sudoku(possibleList)
                break

            if fill_in_number == 81:
                result_sudoku = self.model.result_sudoku(possibleList)
                self.view.show_result_sudoku(result_sudoku)
                break

            fill_in_number_store = fill_in_number
