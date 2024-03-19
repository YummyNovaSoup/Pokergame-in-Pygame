from cardbank import *
import random
class user():
    def __init__(self,name,money):
        self.money = money
        self.name = name
    
    def DrawCards(self,bank):
        self.handcards = bank.DistributeCards()


#test
# user1 = user('Alice',1000)
# user1.DrawCards()
# user1.handcards.ShowCards()

# user2 = user('Peter',1000)
# user2.DrawCards()
# user2.handcards.ShowCards()

# print(bank.amount)