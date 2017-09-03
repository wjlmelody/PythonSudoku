# _*_coding:utf-8
from database.database import *  # 导入数据
import numpy as np

class Model(object):
    '''模型层'''

    def get_sudoku(self):
        return Sudoku

    def possible_list_sudoku(self, sudoku):
        result = []

        for xCount in range(0,9):
            resultSub = []
            for yCount in range(0,9):
                if sudoku[xCount, yCount] != 0:
                    listNum = [sudoku[xCount, yCount]]
                    resultSub.append(listNum)
                else:
                    resultSub.append(self.possible_list_sudoku_sub(sudoku, xCount, yCount))
            result.append(resultSub)

        return np.array(result)

    def possible_list_sudoku_sub(self, sudoku, xCount, yCount):
        result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        resultMinus = []

        for y in range(0,9):
            if sudoku[xCount, y] != 0 :
                resultMinus.append(sudoku[xCount, y])

        for x in range(0,9):
            if sudoku[x, yCount] != 0 :
                resultMinus.append(sudoku[x, yCount])

        xDivmodNumber = self.divmod_number(xCount)
        yDivmodNumber = self.divmod_number(yCount)

        for x in range(xDivmodNumber, xDivmodNumber + 3):
            for y in range(yDivmodNumber, yDivmodNumber + 3):
                if sudoku[x, y] != 0:
                    resultMinus.append(sudoku[x, y])

        resultSet = set(result)
        resultMinusSet = set(resultMinus)

        return list(resultSet - resultMinusSet)

    def divmod_number(self, count):
        return divmod(count, 3)[0] * 3

    def analyse_sudoku(self, guessList):
        for xCount in range(0,9):
            for yCount in range(0,9):
                if len(guessList[xCount, yCount]) != 1:
                    guessList[xCount, yCount] = self.exclusion_method_sudoku_sub(guessList, xCount, yCount)
        for xCount in range(0,9):
            for yCount in range(0,9):
                if len(guessList[xCount,yCount]) != 1:
                    guessList[xCount, yCount] = self.remaining_method_sudoku_sub(guessList, xCount, yCount)
        return guessList

    def exclusion_method_sudoku_sub(self, guessList, xCount, yCount):
        # 摒除法
        possibleUnionX = self.exclusion_method_x(guessList, xCount, yCount)
        possibleUnionY = self.exclusion_method_y(guessList, xCount, yCount)
        possibleUnionXY = self.exclusion_method_xy(guessList, xCount, yCount)

        resultList = guessList[xCount, yCount]

        resultList = self.exclusion_method_output(resultList, possibleUnionX)
        resultList = self.exclusion_method_output(resultList, possibleUnionY)
        resultList = self.exclusion_method_output(resultList, possibleUnionXY)

        return resultList

    def exclusion_method_x(self, guessList, xCount, yCount):
        possibleUnion = []
        for x in range(0, 9):
            if x != xCount:
                possibleUnion.extend(guessList[x, yCount])
        return possibleUnion

    def exclusion_method_y(self, guessList, xCount, yCount):
        possibleUnion = []
        for y in range(0, 9):
            if y != yCount:
                possibleUnion.extend(guessList[xCount, y])
        return possibleUnion

    def exclusion_method_xy(self, guessList, xCount, yCount):
        possibleUnion = []
        xDivmodNumber = self.divmod_number(xCount)
        yDivmodNumber = self.divmod_number(yCount)
        for x in range(xDivmodNumber, xDivmodNumber + 3):
            for y in range(yDivmodNumber, yDivmodNumber + 3):
                if x != xCount or y != yCount:
                    possibleUnion.extend(guessList[x, y])
        return possibleUnion

    def exclusion_method_output(self, resultlist, possibleUnion):
        universalSet = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
        possibleUnionSet = set(possibleUnion)
        candidateResult = universalSet - possibleUnionSet
        if len(candidateResult) > 0:
            return list(candidateResult & set(resultlist))
        else:
            return resultlist

    def remaining_method_sudoku_sub(self, guessList, xCount, yCount):
        universalSet = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
        resultMinus = []

        for y in range(0,9):
            if len(guessList[xCount, y]) == 1:
                resultMinus.append(guessList[xCount, y][0])

        for x in range(0,9):
            if len(guessList[x, yCount]) == 1:
                resultMinus.append(guessList[x, yCount][0])

        xDivmodNumber = self.divmod_number(xCount)
        yDivmodNumber = self.divmod_number(yCount)

        for x in range(xDivmodNumber, xDivmodNumber + 3):
            for y in range(yDivmodNumber, yDivmodNumber + 3):
                if len(guessList[x, y]) == 1:
                    resultMinus.append(guessList[x, y][0])

        resultMinusSet = set(resultMinus)
        return list((universalSet - resultMinusSet) & set(guessList[xCount, yCount]))

    def fill_in_number(self, possibleList):
        result = 0
        for xCount in range(0,9):
            for yCount in range(0,9):
                if len(possibleList[xCount, yCount]) == 1:
                    result += 1
        return result

    def result_sudoku(self, possible_list):
        result = []
        for xCount in range(0,9):
            resultSub = []
            for yCount in range(0,9):
                resultSub.append(possible_list[xCount, yCount][0])
            result.append(resultSub)
        return np.array(result)
