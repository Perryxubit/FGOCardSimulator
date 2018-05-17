# coding=utf-8

class FGOMysticCode:

    __codeID = -1
    __codeName = ''
    __codeRare = -1
    __codeSkill = ''
    __codeSkillMax = ''
    __codeExplaination = ''

    def __init__(self, ID, name, rare, skill, skillmax, explain):
        #initial the role
        self.__codeID = int(ID)
        self.__codeName = name
        self.__codeRare = int(rare)
        self.__codeSkill = skill
        self.__codeSkillMax = skillmax
        self.__codeExplaination = explain
        return

    def getMysticCodeInfo(self):
        str = ''
        alignSpace = 10
        str += ' '
        for i in range(0, self.__codeRare):
            if(i != 0):
                str += ' '
            str += '*'
        for i in range(0, 5-self.__codeRare):
            str += '  '
        str += '  ' + self.__codeName
        return str

    def getRare(self):
        return self.__codeRare

    def getSkill(self):
        return self.__codeSkill

    def getSkillMax(self):
        return self.__codeSkillMax

    def getExplain(self):
        return self.__codeExplaination

    def getID(self):
        return self.__codeID

