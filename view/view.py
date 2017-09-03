# _*_coding:utf-8

class View(object):
    '''视图层'''

    def __init__(self):
        self.iteration_number = 0

    def show_sudoku(self, sudoku):
        '''显示查询结果
        @parameter quote 接收数据'''
        print("\n您当前读入的Sudoku为:")

        for xCount in range(0,9):
            showStr = ""
            for yCount in range(0,9):
                if sudoku[xCount, yCount] == 0:
                    showStr = showStr + "* "
                else:
                    showStr = showStr + str(sudoku[xCount, yCount]) + " "
            print(showStr)
        print("")

    def show_possible_list_sudoku(self, possibleList):
        print("\n您当前Sudoku的最新求解为:")
        for xCount in range(0, 9):
            showStr = ""
            for yCount in range(0, 9):
                if len(possibleList[xCount, yCount]) != 1:
                    showStr = showStr + "* "
                else:
                    showStr = showStr + str(possibleList[xCount,yCount][0]) + " "

            print(showStr)

    def show_fill_in_number(self, fill_in_number):
        self.iteration_number += 1
        print("经过第%s次迭代分析，当前Sudoku已填入数字个数为:%s" % (self.iteration_number, fill_in_number))

    def show_result_sudoku(self, sudoku):
        print("\nSudoku的求解结果为:")

        for xCount in range(0,9):
            showStr = ""
            for yCount in range(0,9):
                showStr = showStr + str(sudoku[xCount, yCount]) + " "
            print(showStr)
        print("")
