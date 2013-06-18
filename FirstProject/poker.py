class card:
    '''
    Playing card object class.  Holds the value and suit of a card and contains
    dictionaries to translate the suit and value into their corresponding string
    names.
    
    :ivar value: Integer value of the card
    :ivar suit:  Integer value of the suit
    :cvar valueNames: Dictionary relating card values with their string names
    :cvar suitNames:  Dictionary relating suit values with their string names
    '''
    
    valueNames = {
        -1:"Invalid value",           
        0:"Joker", 
        1:"Ace",         
        2:"Two",
        3:"Three",
        4:"Four",
        5:"Five",
        6:"Six",
        7:"Seven",
        8:"Eight",
        9:"Nine",
        10:"Ten",
        11:"Jack",
        12:"Queen",
        13:"King",
        14:"Ace"}
    suitNames = {
        -1:"Invalid suit",         
        0:"Jokers",
        1:"Clubs",
        2:"Diamonds",
        3:"Hearts",
        4:"Spades"} 
    
    def __init__(self, cardVal = 0, cardSuit = 0):
        '''
        Initializes the card object, both parameters default to 0 when not
        defined, represented by the Joker of Jokers.  If cardVal or cardSuit
        extend their range, the value or suit variable will be set to -1, which
        is the invalid case.
 
        :param cardVal:  Integer value of the card
        :param cardSuit: Represents the suit of the card in alphabetical order
                         from 1 to 4
        '''

        if (cardVal >= 0) & (cardVal <= 14):
            self.value = cardVal
        else:
            self.value = -1
        if (cardSuit >= 0) & (cardSuit <= 4):
            self.suit = cardSuit
        else:
            self.suit = -1
                
    def getValue(self):
        """Returns the integer value of the card"""
        return self.value
    
    def getSuit(self):
        '''
        Returns the integer value of the suit, order of which is alphabetical
        from 1 to 4
        '''
        return self.suit
    
    def getValueName(self):
        '''
        Returns the string name corresponding to integer value of the card
        Ex: A card value of 11 would return "Jack"
        '''
        return self.valueNames[self.value]
    
    def getSuitName(self):
        '''
        Returns the string name corresponding to integer value of the suit
        Ex: A suit value of 2 would return "Diamonds"
        '''
        return self.suitNames[self.suit]
        
# class hand:
#      
#     defaultHand = {card(10,4), card(11,4), card(12,4), card(13,4), card(14,4)}
#      
#     def __init__(self, cardSet = defaultHand):
#         self.cardsInHand = cardSet
#         self.cardCount = len(self.cardsInHand)
#          
#     def getCard(self, position):
#          
#     def removeCard(self, position):
#          
#     def addCard(self, cardToAdd):
#          
#     def getHand(self):
#          
#     def sortHand(self):
#          