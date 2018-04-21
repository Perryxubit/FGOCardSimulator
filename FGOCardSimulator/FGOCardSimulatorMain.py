#coding=utf-8
from FGOCardLottery import *

def printHelpDocument():
    print("指令说明:");
    print(" 1                 - 单抽抽卡");
    print(" 10                - 十连抽卡");
    print(" a1                - 模拟1000次 单抽方式");
    print(" a01               - 模拟1000次 10连方式");
    print(" statistics/stat/s - 查看历史抽卡统计信息");
    print(" r                 - 重置统计信息");
    print(" exit/e            - 退出程序");
    return

if( __name__ == "__main__"):
    lottery = FGOCardLottery()
    while True:
        # exit when input 'e'
        str = raw_input("Please input command: (input 'help' for help or 'exit' for exiting)\n")
        if (str.lower() == 'exit' or str.lower() == 'e'):
            break
        elif (str == '1'): # single-draw
            lottery.drawOneCard(True)
        elif (str == '10'): # 10s-draw
            lottery.drawTenCards()
        elif (str.lower() == 'help' or str.lower() == 'h'):
            printHelpDocument();
        elif (str.lower() == 'statistics' or str.lower() == 'stat' or str.lower() == 's'): # check statistics
            lottery.printStatisitcs()
        elif (str.lower() == 'a1'): # simulate 1000 times with single-draw
            for i in range(1000):
                lottery.drawOneCard(True)
        elif (str.lower() == 'a10'): # simulate 1000 times with 10s-draw
            for i in range(100):
                lottery.drawTenCards()
        elif (str.lower() == 'r'): # reset statistics record
            lottery = FGOCardLottery()
        else:
            print('Wrong input, please try again.')
