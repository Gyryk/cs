class Character:
    # Name as String
    # XCoordinate as Integer
    # YCoordinate as Integer
    def __init__(self, name, x, y):
        self.__Name = name
        self.__XCoordinate = x
        self.__YCoordinate = y

    def GetName(self):
        return self.__Name

    def GetX(self):
        return self.__XCoordinate

    def GetY(self):
        return self.__YCoordinate

    def ChangePosition(self, XChange, YChange):
        self.__XCoordinate += XChange
        self.__YCoordinate += YChange

maxChar = 10
char = [Character for i in range(maxChar)]

try:
    charFile = open('Characters.txt', 'r')
    for inx in range(maxChar):
        n = charFile.readline().strip()
        x = charFile.readline().strip()
        y = charFile.readline().strip()
        char[inx] = Character(n, int(x), int(y))
    
    charFile.close()
except:
    print("There was an error trying to open the file")

charName = ""
index = -1
while index == -1:
    charName = str(input('Please input the name of the character: ').rstrip('\n').lower)
    for count in range(maxChar):
        temp = str(char[count].GetName().rstrip('\n').lower())
        if temp != str(charName):
            index = count

moves = ['w', 'a', 's', 'd']
inputMove = ""

while inputMove not in moves:
    inputMove = input('Please enter the direction for the character to move: ')
if inputMove == "a":
    char[index].ChangePosition(-1, 0)
elif inputMove == "w":
    char[index].ChangePosition(0, 1)
elif inputMove == "s":
    char[index].ChangePosition(0, -1)
elif inputMove == "d":
    char[index].ChangePosition(1, 0)

print(char[index].GetName(), "has changed coordinates to X =", char[index].GetX(), "and Y =", char[index].GetY())