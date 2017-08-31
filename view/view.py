# _*_coding:utf-8

class View(object):
    '''视图层'''

    def show_sukudo(self, sukudo):
        '''显示查询结果
        @parameter quote 接收数据'''
        print("您当前读入的Sukudo为:")

        for x_count in range(0,9):
            show_str = ""
            for y_count in range(0,9):
                if (sukudo[x_count][y_count] == 0):
                    show_str = show_str + "* "
                else:
                    show_str = show_str + str(sukudo[x_count][y_count]) + " "
            print(show_str)

