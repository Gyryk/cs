class Card:
    # Number - Integer
    # Colour - String
    def __init__(self, num, col):
        self.__Number = num
        self.__Colour = col

    def GetNumber(self):
        return self.__Number
    
    def GetColour(self):
        return self.__Colour
    
global chosen
chosen = []


def ChooseCard():
    global chosen
    available = False
    while not available:
        inx = int(input("Please input the index of the card you want (1-30): "))
        if(inx > 0 and inx <= 30):
            if inx in chosen:
                print("That card has already been chosen please choose another.")
                available = False
            else:
                chosen.append(inx)
                available = True
        else:
            print("Please input a number between 1 and 30 only")
            available = False
    return inx-1

arr = [Card for i in range(30)]

try:
    cardsFile = open('CardValues.txt', "r")
    for i in range(0, 30):
        currNum = int(cardsFile.readline())
        currCol = cardsFile.readline()
        arr[i] = Card(currNum, currCol)

    cardsFile.close()
except IOError:
    print("File could not be opened")

Player1 = [] # of Card

while len(Player1) < 4:
    Player1.append(arr[ChooseCard()])

for c in Player1:
    print(c.GetNumber(), c.GetColour())
