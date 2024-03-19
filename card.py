class card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.value = self.RankToValue(rank)

    def RankToValue(self,rank):
        if rank == 'A':
            value = 14
        elif rank == 'K':
            value =13
        elif rank == 'Q':
            value = 12
        elif rank == 'J':
            value = 11
        else:
            value =eval(rank)
        return value
    
#test
# card1 = card('9','C')
# print(card1.value)
