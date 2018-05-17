# -*- coding:utf-8 -*-
import random
from FGOHero import *
from FGOMysticCode import *

class FGOCardLottery:
    'FGO card lottery simulator'
    cardStatisticRecord = {} # statistic dictionary record

    __heroIndexMap = {}
    __heroDataMap = {} # ID-> hero object[name, rare, etc.]

    __mycodeIndexMap = {} # Rare(int) -> [mycode object1, mycode object2, etc]
    __mycodeDataMap = {} # ID-> mycode object(name, rare, etc.)
    __mycodeCount = 0
    __heroCount = 0

    def __init__(self, heroDataDict, mycodeDataDict):
        #initial the lottery statistic information
        self.cardStatisticRecord['5_Servant'] = 0
        self.cardStatisticRecord['4_Servant'] = 0
        self.cardStatisticRecord['3_Servant'] = 0
        self.cardStatisticRecord['5_MysticCode'] = 0
        self.cardStatisticRecord['4_MysticCode'] = 0
        self.cardStatisticRecord['3_MysticCode'] = 0

        self.__heroDataMap = heroDataDict
        self.__mycodeDataMap = mycodeDataDict
        self.matchMyCodeIndexMap()
        self.matchHeroIndexMap()

        print('共有' + str(self.__mycodeCount) + '张可抽礼装卡')
        print('共有' + str(self.__heroCount) + '张英灵卡')
        return

    def matchHeroIndexMap(self):
        for key in self.__heroDataMap:
            heroObject = self.__heroDataMap[key]
            rare = heroObject.getRare()
            if (rare not in self.__heroIndexMap): # create new list
                self.__heroIndexMap[rare] = []

            self.__heroIndexMap[rare].append(heroObject)
            self.__heroCount += 1

        return

    def matchMyCodeIndexMap(self):
        for key in self.__mycodeDataMap:
            mycodeObject = self.__mycodeDataMap[key]
            rare = mycodeObject.getRare()
            if(rare not in self.__mycodeIndexMap): # create new list
                self.__mycodeIndexMap[rare] = []

            # Mystic Code filter
            if(self.isValidMysticCode(mycodeObject)):
                self.__mycodeIndexMap[rare].append(mycodeObject)
                self.__mycodeCount += 1
        return

    def isValidMysticCode(self, mycodeObject):
        if ('——' in mycodeObject.getSkill()):
            return False
        elif (mycodeObject.getSkillMax().startswith('——')):
            return False
        elif (mycodeObject.getSkillMax().startswith('--')):
            return False
        elif('任务通关时' in mycodeObject.getSkill()):
            return False
        elif ('活动期间限定' in mycodeObject.getSkill()):
            return False

        # else, return true to validate this Mystic Code
        return True

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
            self.__getCard(res)
        return res

    def drawTenCards(self):
        # draw 10 cards
        getGolden = False
        getHero = False
        getRareMysticCode = False
        for i in range(0, 8):
            # get 8 times to see whether we have drawn golden cards already
            card = self.drawOneCard(True)
            if('Servant' in card):
                getHero = True
            if('4_MysticCode' in card or '5_MysticCode' in card):
                getRareMysticCode = True

        # the 9th draw to get a Hero if there is no one in last 8 times (>=3 stars)
        if (not getHero):
            card = self.drawOneCard(False)
            while ('Servant' not in card): # get cards until get a hero!
                card = self.drawOneCard(False)
            self.__getCard(card)
        else:
            # Otherwise, just draw a card randomly
            card = self.drawOneCard(True)
            if ('4_MysticCode' in card or '5_MysticCode' in card):
                getRareMysticCode = True

        # the 10th draw to get a Rare MysticCode if there is no one before (>=4 stars)
        if (not getRareMysticCode):
            card = self.drawOneCard(False)
            while (not('4_MysticCode' in card or '5_MysticCode' in card)):
                card = self.drawOneCard(False)
            self.__getCard(card)
        else: # get last card
            self.drawOneCard(True)

    def __getOutputCard(self, res):
        rare = res[0:1] # rarity  0\1\2\3\4\5

        if('Ser' in res): # get Hero
            heroPool = self.__heroIndexMap[int(rare)]
            randomIndex = random.randint(0, len(heroPool) - 1)
            heroObject = heroPool[randomIndex]

            # get a hero card and print it out
            return ('英灵 ' + heroObject.getHeroInfo() + ' 获取!')
        else:
            mycodePool = self.__mycodeIndexMap[int(rare)]
            randomIndex = random.randint(0, len(mycodePool) - 1)
            mycodeObject = mycodePool[randomIndex]

            # get a mystic code card and print it out
            return ('概念礼装 ' + mycodeObject.getMysticCodeInfo() + ' 获取！' + '   (' + mycodeObject.getSkillMax() + ')')

    def __getCard(self, res):
        # output the card and update statistics
        self.cardStatisticRecord[res] += 1
        print(self.__getOutputCard(res))
        return

    def printStatisitcs(self):
        # print statistics record
        count = 0
        cardTuple = ('5_Servant', '4_Servant', '3_Servant', '5_MysticCode', '4_MysticCode', '3_MysticCode')
        for key in cardTuple:
            rare = int(key[0:1])
            if ('Serv' in key):
                print('英灵    '),
            else:
                print('概念礼装'),
            # print rarity starts
            for i in range(0, rare):
                print('*'),
            for i in range(0, 5 - rare):
                print(' '),
            if(key in self.cardStatisticRecord):
                print('  ' + str(self.cardStatisticRecord[key]) + '张')
                count += self.cardStatisticRecord[key]
            else:
                print('  0张')
        # print summary
        print("共抽取" + str(count) + "次, 消耗圣晶石" + str(count*3) + "个。")
