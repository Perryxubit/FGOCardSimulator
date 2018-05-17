# -*- coding:utf-8 -*-
from __future__ import print_function
from FGOHero import *
from FGOMysticCode import *

heroSourceFile = 'D:/Crawler/FGO/FGO Hero/HeroList.txt'
mycodeSourceFile = 'D:/Crawler/FGO/FGO Mystic Code/MysticCodeList.txt'

class FGODataLoader:

    def loadHeroRareIndex(self):
        rareData = {}
        heroMap = self.loadHeroData()
        for rare in heroMap:
            rareData[rare] = []
        for rare in heroMap:
            list = heroMap[rare]
            for entry in list:
                rareData[rare].append(entry['ID'])

        return rareData

    def loadHeroObjects(self):
        heroMap = {}
        fo = open(heroSourceFile, 'r')
        str = fo.readline()
        while (str):
            # name, rare, rClass, gender
            '''Data structure
              0###玛修·基列莱特###Shielder###4###女性###武内崇###骑乘,人型,从者（被EA克制）,天/地从者,半从者
           '''
            data = str.split('###')
            if(len(data) >= 5):
                hero = FGOHero(data[0], data[1], data[3], data[2], data[4])
                heroMap[data[0]] = hero
            str = fo.readline()
        fo.close()

        # e.g. get info for hero index 3
        # info = heroMap['3'].getHeroInfo()
        #print(info)
        print('* Hero Data has been loaded from - ' + heroSourceFile)
        return heroMap

    def loadMysticCodeObjects(self):
        mycodeMap = {}
        fo = open(mycodeSourceFile, 'r')
        str = fo.readline()
        while (str):
            # name, rare, rClass, gender
            '''Data structure
              1###顽强###1###自身的防御力提升3%###自身的防御力提升5%[最大解放]###成为坚固之物。修炼即是将肉体化作岩石。
           '''
            data = str.split('###')
            if (len(data) >= 6):
                #name, rare, skill, skillMax, explain
                mycode = FGOMysticCode(data[0], data[1], data[2], data[3], data[4], data[5])
                mycodeMap[data[0]] = mycode
            str = fo.readline()
        fo.close()

        # e.g. get info for mycode index 3
        #info = mycodeMap['3'].getMysticCodeInfo()
        #print(info)
        print('* Mystic Code Data has been loaded from - ' + mycodeSourceFile)
        return mycodeMap

    def sortedDictKeys(self, dict):
        keys = dict.keys()
        keys.sort()
        rev = {}
        for key in keys:
            rev[key] = dict[key]

        return rev

    def printSeparator(self):
        for j in range(0, 10):
            print('-----', end='')
        print('')
        return

    def printHeroStatistics(self):
        # load data from file
        heroMap = self.loadHeroData()

        # HOW TO SHOW CHINESE IN CONSOLE:
        # print unicode(heroMap['0'][0]['NAME'], 'utf-8')
        print('Hero data has been loaded.')

        # 1.hero rare statistics
        print("Data Statistics:")
        for key in heroMap:
            print(key + '星从者 -  ' + str(len(heroMap[key])) + '个')
        self.printSeparator()

        painterMap = {}  # {person1 -> [hero1, hero2, hero3, ...]}
        for rare in heroMap:
            heroList = heroMap[rare]
            # print(heroList)
            for index in range(0, len(heroList)):
                painter = heroList[index]['WRITER']
                hero = heroList[index]['NAME']
                if (not painterMap.has_key(painter)):
                    # new painter -> new list insert
                    painterMap[painter] = [hero]
                else:
                    painterMap[painter].append(hero)

        # for painter in painterMap.keys():
        # print(painter + ' - ' + str(len(painterMap[painter])))
        # Output Chinese -> string_escape
        print(str(painterMap).decode('string_escape'))

    def __init__(self):
        print('Loading data from files...')




