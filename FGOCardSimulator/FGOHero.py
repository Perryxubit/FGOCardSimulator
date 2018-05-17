# coding=utf-8

class FGOHero:

    __roleID = -1
    __roleName = ''
    __roleGender = ''
    __roleClass = ''
    __roleRare = -1

    def __init__(self, ID, name, rare, rClass, gender):
        #initial the role
        self.__roleID = ID
        self.__roleName = name
        self.__roleGender = gender
        self.__roleClass = rClass
        self.__roleRare = int(rare)
        return

    def getHeroInfo(self):
        str = ''
        str += '     '
        for i in range(0, self.__roleRare):
            if(i != 0):
                str += ' '
            str += '*'
        for i in range(0, 5-self.__roleRare):
            str += '  '
        str += '  ' + self.__roleClass
        str += '  ' + self.__roleName
        return str

    def getRare(self):
        return self.__roleRare
