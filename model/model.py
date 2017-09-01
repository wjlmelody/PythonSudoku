# _*_coding:utf-8
from database.database import *  # 导入数据

class Model(object):
    '''模型层'''

    def get_sudoku(self):
        return Sudoku;

    def possible_list_sudoku(self, sudoku):
        result = []

        for xCount in range(0,9):
            resultSub = []
            for yCount in range(0,9):
                if sudoku[xCount][yCount] != 0:
                    listNum = [sudoku[xCount][yCount]]
                    resultSub.append(listNum)
                else:
                    resultSub.append(self.possible_list_sudoku_sub(sudoku, xCount, yCount))
            result.append(resultSub)

        return result

    def possible_list_sudoku_sub(self, sudoku, xCount, yCount):
        result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        resultMinus = []

        for y in range(0,9):
            if sudoku[xCount][y] != 0 :
                resultMinus.append(sudoku[xCount][y])

        for x in range(0,9):
            if sudoku[x][yCount] != 0 :
                resultMinus.append(sudoku[x][yCount])

        xDivmodNumber = self.divmod_number(xCount)
        yDivmodNumber = self.divmod_number(yCount)

        for x in range(xDivmodNumber, xDivmodNumber + 3):
            for y in range(yDivmodNumber, yDivmodNumber + 3):
                if sudoku[x][y] != 0:
                    resultMinus.append(sudoku[x][y])

        resultSet = set(result)
        resultMinusSet = set(resultMinus)

        return list(resultSet - resultMinusSet)

    def divmod_number(self, count):
        return divmod(count, 3)[0] * 3

    def analyse_sudoku(self, guessList):
        for xCount in range(0,9):
            for yCount in range(0,9):
                if len(guessList[xCount][yCount]) != 1:
                    guessList[xCount][yCount] = self.analyse_sudoku_sub(guessList, xCount, yCount)
        return guessList

    def analyse_sudoku_sub(self, guessList, xCount, yCount):
        possibleUnion = []

        for y in range(0, 9):
            possibleUnion.extend(guessList[xCount][y])

        for x in range(0, 9):
            possibleUnion.extend(guessList[x][yCount])

        xDivmodNumber = self.divmod_number(xCount)
        yDivmodNumber = self.divmod_number(yCount)

        for x in range(xDivmodNumber, xDivmodNumber + 3):
            for y in range(yDivmodNumber, yDivmodNumber + 3):
                possibleUnion.extend(guessList[x][y])

        universalSet = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
        possibleUnionSet = set(possibleUnion)
        candidateResult = universalSet - possibleUnionSet

        if len(candidateResult) > 0:
            return list(candidateResult & set(guessList[xCount][yCount]))
        else:
            return guessList[xCount][yCount]

    # def exclusion_method(self, guessList, xCount, yCount):
    #     # 摒除法
    #
    # def exclusion_method_x(self, guessList, xCount, yCount):
