from cardbank import *
from user import *
import math

scoreint = ['High','One Pair','Two Pairs','3 of a Kind','Straight','Flush','Full House','4 of a Kind','Straight Flush']
scoretimes = {}

#初始界面
print('-'*10)
print('Hello ~ Welcome to the Poker')
print('Now it\'s time to play')
print('You have two cards')
print('-'*10)
times0 = times = 10000

while times != 0:
    #创建牌库
    bank = cardbank()
    bank.CreateCards()
    bank.ShuffleCards()

    #创建牌堆
    tablecards = cardbank()

    #创建用户
    userlist = []
    user1 = user('Alice',1000)

    #发牌
    user1.DrawCards(bank)
    # user1.handcards.ShowCards()

    # print('What do you want to do next?')
    # print('Fold? Call? or Raise?')

    # next = input('f/c/r')

    #翻牌
    tablecards = bank.Flop()
    # tablecards.ShowCards()

    #
    # next = input('f/c/r')

    #转牌
    tablecards.Add(bank.Turn())
    # tablecards.ShowCards()

    # next = input('f/c/r')
    #河牌
    tablecards.Add(bank.River())
    # print('bankcards:')
    # tablecards.ShowCards()
    # print('-'*20)
    user1.handcards.Add(tablecards)
    # print('-'*20)
    # print('This is your fianl quant:')
    q = user1.handcards.AllQuant()
    p = math.floor(q)
    try:
        scoretimes[scoreint[p]]+=1
    except:
        scoretimes[scoreint[p]]=1
    # print(q)
    # print(scoreint[p])

    # print('-'*20)
    times = times -1
    if times%(times0/100) == 0:
        print("正在计算---->",100-times/(times0/100),'%')

for key in scoretimes:
    scoretimes[key]= scoretimes[key]/times0
print(scoretimes)