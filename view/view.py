# _*_coding:utf-8

class View(object):
    '''视图层'''

    def show_sudoku(self, sudoku):
        '''显示查询结果
        @parameter quote 接收数据'''
        print("您当前读入的sudoku为:")

        for xCount in range(0,9):
            showStr = ""
            for yCount in range(0,9):
                if sudoku[xCount][yCount] == 0:
                    showStr = showStr + "* "
                else:
                    showStr = showStr + str(sudoku[xCount][yCount]) + " "
            print(showStr)

    def show_possible_list_sudoku(self, possibleList):
        for x in range(0, 9):
            for y in range(0, 9):
                print(x, y, possibleList[x][y])

