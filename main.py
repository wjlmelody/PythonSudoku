# _*_coding:utf-8
'''主程序'''
from controller.controller import Controller

def main():
    controller = Controller()
    controller.run()

    # while True:
    #     controller = Controller()
    #     controller.run()

if __name__ == '__main__':
    main()