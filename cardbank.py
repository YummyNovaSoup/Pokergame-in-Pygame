from card import *
import random
class cardbank():
    def __init__(self):
        self.cardlist = []
        self.amount = 0
        self.score = 0
        self.belong = [0,0,0,0,0,0,0,0,0]
        self.scoreref = ['High','One pair','Two pairs','3 of a kind','Straight','Flush','Full house','4 of a kind','Straight Flush']
        
    def CreateCards(self):
        ranklist = []
        suitlist = ['spade','club','heart','dimond']
        for i in range(2,11):
            ranklist.append(str(i))
        ranklist.append('J')
        ranklist.append('Q')
        ranklist.append('K')
        ranklist.append('A')
        for rank in ranklist:
            for suit in suitlist:
                cardnow = card(rank,suit)
                self.cardlist.append(cardnow)
        self.CardsAmount()
        
    def ShowCards(self):
        for card in self.cardlist:
            print(card.rank + ' of ' + card.suit)

    def ShuffleCards(self):
        random.shuffle(self.cardlist)

    #从self里分发出两张牌作为一个新cardbank
    def DistributeCards(self):
        cardsgiven = cardbank()
        card = self.cardlist.pop()
        cardsgiven.cardlist.append(card)
        card = self.cardlist.pop()
        cardsgiven.cardlist.append(card)
        self.CardsAmount()
        return cardsgiven
    
    def CardsAmount(self):
        self.amount = len(self.cardlist)

    def Flop(self):
        FlopCards = cardbank()
        card = self.cardlist.pop()
        FlopCards.cardlist.append(card)
        card = self.cardlist.pop()
        FlopCards.cardlist.append(card)
        card = self.cardlist.pop()
        FlopCards.cardlist.append(card)
        self.CardsAmount()
        return FlopCards
    
    def Add(self,bank2):
        self.cardlist = self.cardlist + bank2.cardlist
        self.CardsAmount()
    
    def Turn(self):
        TurnCards = cardbank()
        card = self.cardlist.pop()
        TurnCards.cardlist.append(card)
        self.CardsAmount()
        return TurnCards
    
    def River(self):
        TurnCards = cardbank()
        card = self.cardlist.pop()
        TurnCards.cardlist.append(card)
        self.CardsAmount()
        return TurnCards

    def AmountCheck(self):
        if len(self.cardlist) != 5:
            print('error! JudgeCards must be 5')
            return 0
        else:
            return 5
    
    def GetSuit(self):
        self.suits = []
        for card in self.cardlist:
            self.suits.append(card.suit)

    def GetRank(self):
        self.ranks = []
        for card in self.cardlist:
            self.ranks.append(card.rank)

    def GetValue(self):
        self.values = []
        for card in self.cardlist:
            self.values.append(card.value)

    def isFlush(self):
        if self.AmountCheck() != 5:
            return KeyError
        self.GetSuit()
        self.GetValue()
        self.values.sort()
        heartN = self.suits.count('heart')
        spadeN = self.suits.count('spade')
        dimondN = self.suits.count('dimond')
        clubN = self.suits.count('club')
        if heartN==5 or  spadeN==5 or dimondN==5 or clubN==5:
            self.score = 5 + 0.1*self.values[4]/15
            self.belong[5] = 1
            return 1
        else:
            return 0
    
    def is4ofaKind(self):
        if self.AmountCheck() != 5:
            return KeyError
        maxamount = 0
        self.GetValue()
        valuesdic = set(self.values)
        for value in valuesdic:
            maxamount = max(maxamount,self.values.count(value))
            if maxamount == 4:
                self.score = 7+ 0.1*value/15
                self.belong[7] = 1
                return 1
        return 0
    
    def is3ofaKind(self):
        if self.AmountCheck() != 5:
            return KeyError
        if self.is4ofaKind():
            return 0
        
        maxamount = 0
        self.GetValue()
        valuesdic = set(self.values)
        for value in valuesdic:
            maxamount =max(maxamount,self.values.count(value))
            if maxamount == 3 and len(set(self.values))==3:
                self.score = 3+0.1*value/15
                self.belong[3] = 1
                return 1
        return 0

    def isFullhouse(self):
        if self.AmountCheck() != 5:
            return KeyError
        if self.is4ofaKind():
            return 0
        
        maxamount = 0
        self.GetValue()
        valuesdic = set(self.values)
        for value in valuesdic:
            maxamount =max(maxamount,self.values.count(value))
            if maxamount == 3 and len(set(self.values))==2:
                self.score = 6+0.1*value/15
                self.belong[6] = 1
                return 1
        return 0
        
    def isTwoPairs(self):
        if self.AmountCheck() != 5:
            return KeyError
        if self.is4ofaKind() or self.is3ofaKind() or self.isFullhouse():
            return 0
        
        pairsamount = 0
        pairs = []
        high = []
        self.GetValue()
        valueset = set(self.values)
        for value in valueset:
            if self.values.count(value) == 2:
                pairsamount += 1
                pairs.append(value)
            else:
                high.append(value)
        if pairsamount == 2:
            pairs.sort()
            self.score = 2 + 0.1*pairs[1]/15 + 0.01*pairs[0]/15 +0.001*high[0]/15
            self.belong[2]=1
            return 1
        else:
            return 0

    def isOnePair(self):
        if self.AmountCheck() != 5:
            return KeyError
        if self.is4ofaKind() or self.is3ofaKind() or self.isFullhouse() :
            return 0
        
        pairsamount = 0
        pairs = []
        high = []
        self.GetValue()
        valueset = set(self.values)
        for value in valueset:
            if self.values.count(value) == 2:
                pairsamount += 1
                pairs.append(value)
            else :
                high.append(value)
        if pairsamount == 1:
            high.sort()
            self.score = 1+0.1*pairs[0]/15+0.01*high[2]/15 +0.001*high[1]/15 +0.0001*high[0]/15
            self.belong[1] = 1
            return 1
        else:
            return 0

    def noPair(self):
        if self.AmountCheck() != 5:
            return KeyError
        if self.is4ofaKind() or self.is3ofaKind() or self.isFullhouse() or self.isOnePair() or self.isTwoPairs():
            return 0
        return 1

    def isStraight(self):
        if not self.noPair():
            return 0
        self.values.sort()
        if max(self.values)-min(self.values)==4:
            self.score = 4 + 0.1*max(self.values)/15
            self.belong[4] = 1
            return 1
        elif self.values == [2,3,4,5,14]:
            self.score = 4 + 0.1*5/15
            self.belong[4] = 1
            return 1
        else:
            return 0
        
    def isStraightFlush(self):
        if self.isFlush() and self.isStraight():
            if self.values == [2,3,4,5,14]:
                self.score = 8 + 0.1*5/15
            else:
                self.score = 8 + 0.1*max(self.values)/15
            self.belong[8]=1
            return 1
        else:
            return 0
        
    def isHigh(self):
        if self.noPair() and not self.isStraight() and not self.isFlush():
            self.values.sort()
            self.score = 0 + 0.1*self.values[4]/15 + 0.01*self.values[3]/15 + 0.001*self.values[2]/15 + 0.0001*self.values[1]/15 + 0.00001*self.values[0]/15 
            return 1
        else:
            return 0
        
    #ban
    def BelongCheck(self):
        self.belong = []
        if self.isHigh()[0]==1:
            self.belong.append(1)
        else:
            self.belong.append(0)
        if self.isOnePair()[0]==1:
            self.belong.append(1)
        else:
            self.belong.append(0)
        if self.isTwoPairs()[0]==1:
            self.belong.append(1)
        else:
            self.belong.append(0)
        if self.is3ofaKind()[0]==1:
            self.belong.append(1)
        else:
            self.belong.append(0)
        if self.isStraight()[0]==1:
            self.belong.append(1)
        else:
            self.belong.append(0)
        if self.isFlush()[0]==1:
            self.belong.append(1)
        else:
            self.belong.append(0)
        if self.isFullhouse()[0]==1:
            self.belong.append(1)
        else:
            self.belong.append(0)
        if self.is4ofaKind()[0]==1:
            self.belong.append(1)
        else:
            self.belong.append(0)
        if self.isStraightFlush()[0]==1:
            self.belong.append(1)
        else:
            self.belong.append(0)
        
    def Quant(self):
        self.GetValue()
        self.GetRank()
        self.GetSuit()
        if self.isStraightFlush()==1:
            return self.score
        if self.isHigh()==1:
            return self.score
        if self.isOnePair()==1:
            return self.score
        if self.isTwoPairs()==1:
            return self.score
        if self.is3ofaKind()==1:
            return self.score
        if self.isStraight()==1:
            return self.score
        if self.isFlush()==1:
            return self.score
        if self.isFullhouse()==1:
            return self.score
        if self.is4ofaKind()==1:
            return self.score

    def Cards7to5(self):
        if len(self.cardlist) != 7:
            return KeyError
        cards5list = []
        for i in range(7):
            for j in range(i+1,7):
                changecards = cardbank()
                changecards.cardlist = self.cardlist.copy()
                del changecards.cardlist[j]
                del changecards.cardlist[i]
                cards5list.append(changecards)

        return cards5list

    def AllQuant(self):
        allcard5 = self.Cards7to5()
        maxquant = 0
        for finalcards in allcard5:
            finalcards.Quant()
            maxquant = max(maxquant,finalcards.score)
        return maxquant
    
    #先不考虑相等的情况
    # def WinJudge(self,userdic):
    #     for name,handcards in userdic.items():
