# FGOCardSimulator
<pre>
A little python program to simulate the draw card process in famous mobile game - Fate Grand Order (FGO)
This program used the output file from another github project of mine - FGOCrwaler as input data files.
Currently we only load Hero/Mystic code cards text data, in future I'll improve it in GUI mode and provide real picture for
each card drawing.

You need to set the path parameters in FGODataLoader.py as input path:
  heroSourceFile = 'D:/Crawler/FGO/FGO Hero/HeroList.txt'
  mycodeSourceFile = 'D:/Crawler/FGO/FGO Mystic Code/MysticCodeList.txt'
Then please run FGOCardSimulatorMain.py to start the command mode loop.

Command explaination in command mode:
 help/h            - 帮助信息 
 1                 - 单抽抽卡 (draw 1 card)
 10                - 十连抽卡 (draw 10 cards)
 a1                - 模拟1000次 单抽方式 (draw 1 card 1000 times)
 a01               - 模拟1000次 10连方式 (draw 10 cards 100 times)
 statistics/stat/s - 查看历史抽卡统计信息
 r                 - 重置统计信息 (reset statistic record)
 exit/e            - 退出程序
 
Examples:
input: 10 
概念礼装  * * *      星光盛宴 获取！   (自身星星集中度提升200% & 自身的Quick卡性能提升3%[最大解放])
概念礼装  * * * *    死灵魔术 获取！   (自身的HP为0时一定概率赋予毅力状态（HP回复1000）[最大解放])
概念礼装  * * *      白鹳骑士 获取！   ([Berserker]职阶装备时宝具威力提升25%[最大解放])
英灵      * * *      Lancer  罗穆路斯 获取!
概念礼装  * * *      SLAYER之王子殿下 获取！   (赋予自身每回合获得2个星星状态 & 赋予[龙]特攻状态10%[最大解放])
英灵      * * *      Caster  冯·霍恩海姆·帕拉塞尔苏斯 获取!
英灵      * * *      Archer  比利小子 获取!
英灵      * * *      Assassin  百貌的哈桑 获取!
概念礼装  * * * *    Graceful sweet time  获取！   (赋予自身必中状态 & 赋予伤害增加600状态 & 受到的伤害减少300[最大解放])
概念礼装  * * *      睿智之光 获取！   (自身的Arts卡性能提升8% & NP获得量提升5%[最大解放])
input: 1
英灵      * * *      Lancer  迪尔姆德·奥迪纳 获取!
input: s
英灵     * * * * *   0张
英灵     * * * *     0张
英灵     * * *       12张
概念礼装 * * * * *   3张
概念礼装 * * * *     7张
概念礼装 * * *       14张
共抽取36次, 消耗圣晶石108个。

</pre>
