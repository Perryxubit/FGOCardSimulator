#coding=utf-8
import random
from FGOHero import *
from FGOMysticCode import *

class FGOCardLottery:
    'FGO card lottery simulator'
    statistic = {} # statistic dictionary record

    def __init__(self):
        #initial the lottery statistic information
        self.statistic['5_Servant'] = 0
        self.statistic['4_Servant'] = 0
        self.statistic['3_Servant'] = 0
        self.statistic['5_MysticCode'] = 0
        self.statistic['4_MysticCode'] = 0
        self.statistic['3_MysticCode'] = 0
        return

    def drawOneCard(self, isPrint):
        # draw one card
        randomValue = random.randint(0, 99)
        if (randomValue == 0):
            res = '5_Servant'
        elif (randomValue <= 3):
            res = '4_Servant'
        elif (randomValue <= 7):
            res = '5_MysticCode'
        elif (randomValue <= 19):
            res = '4_MysticCode'
        elif (randomValue <= 59):
            res = '3_Servant'
        else:
            res = '3_MysticCode'

        if (isPrint == True):
            # whether print and update statistics
            self.__printCard(res)
        return res

    def drawTenCards(self):
        # draw 10 cards
        getGolden = False
        for i in range(0, 9):
            # get 9 times to see whether we have drawn golden cards already
            card = self.drawOneCard(True)
            if(card.startswith('5_') or card.startswith('4_')):
                getGolden = True
        if (getGolden == False):
            # get one golden card on purpose
            card = ""
            while (not card.startswith('5_') and not card.startswith('4_')):
                # draw one card but not print or update the statistics if it is not a golden one
                card = self.drawOneCard(False)
            self.__printCard(card)
        else: # get last card
            self.drawOneCard(True)

    def __getOutputString(self, res):
        # mapping the hash key with output formatted String
        if(res.startswith('5_Ser')):
            return ("* * * * * 英灵")
        elif(res.startswith('4_Ser')):
            return ("* * * *   英灵")
        elif (res.startswith('3_Ser')):
            return ("* * *     英灵")
        elif (res.startswith('5_Mys')):
            return ("* * * * * 概念礼装")
        elif (res.startswith('4_Mys')):
            return ("* * * *   概念礼装")
        elif (res.startswith('3_Mys')):
            return ("* * *     概念礼装")

    def __printCard(self, res):
        # output the card and update statistics
        self.statistic[res] += 1
        print(self.__getOutputString(res) + " 获取！")
        return

    def printStatisitcs(self):
        # print statistics record
        count = 0
        for key in self.statistic.keys():
            outputStr = self.__getOutputString(key)
            val = self.statistic[key]
            count += val
            print(outputStr + " - " + str(val))
        # print summary
        print("共抽取" + str(count) + "次, 消耗圣晶石" + str(count*3) + "个。")
