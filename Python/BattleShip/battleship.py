from time import sleep
numRow = 6
numCol = 6
board1 = [[False for column1 in range(numCol)] for row1 in range(numRow)]
board2 = [[False for column2 in range(numCol)] for row2 in range(numRow)]


def setShip1(coord1,coord2):
        coord1 = int(coord1)
        coord2 = int(coord2)
        board1[coord1][coord2] = True

def askForCoords():
    row = input("\nEnter Row Number:\n")
    col = input("\nEnter Column Number\n")
    return {
        "row": row,
        "col": col
    }

def player2Start():
    print("Let's start setting up your board")
    print("First we will set up your 1 space spy-ship:\n")
    for i in range(1):
        coords = askForCoords()
        row = coords["row"]
        column = coords["col"]
        setShip1(row, column)
    print("Done.\n")
    print("\nNow for your 2 space ship")
    for k in range(2):
        coords = askForCoords()
        row = coords["row"]
        column = coords["col"]
        setShip1(row, column)
    print("\n\nNow your 3 space ship")
    for x in range(3):
        coords = askForCoords()
        row = coords["row"]
        column = coords["col"]
        setShip1(row, column)
    print("\n\n4 space ship:")
    for x in range(4):
        coords = askForCoords()
        row = coords["row"]
        column = coords["col"]
        setShip1(row, column)
    print("\n\nAnd last but not least, the 5 Space Ship")
    for x in range(5):
        coords = askForCoords()
        row = coords["row"]
        column = coords["col"]
        setShip1(row, column)
    print("\n\n\n\n\n\tDone!")

def player1Start():
    print("Let's start setting up your board")
    print("First we will set up your 1 space spy-ship:\n")
    for i in range(1):
        coords = askForCoords()
        row = coords["row"]
        column = coords["col"]
        setShip1(row, column)
    print("Done.\n")
    print("\nNow for your 2 space ship")
    for k in range(2):
        coords = askForCoords()
        row = coords["row"]
        column = coords["col"]
        setShip1(row, column)
    print("\n\nNow your 3 space ship")
    for x in range (3):
        coords = askForCoords()
        row = coords["row"]
        column = coords["col"]
        setShip1(row, column)
    print("\n\n4 space ship:")
    for x in range (4):
        coords = askForCoords()
        row = coords["row"]
        column = coords["col"]
        setShip1(row, column)
    print("\n\nAnd last but not least, the 5 Space Ship")
    for x in range (5):
        coords = askForCoords()
        row = coords["row"]
        column = coords["col"]
        setShip1(row, column)
    print("\n\n\n\n\n\tDone!")


print("Welcome to Felipe's Battleship game!")
sleep(3)
fakeTable = [['0,0', '0,2', '0,3', '0,4', '0,5', '0,6'],
             ['2,0', '2,2', '2,3', '2,4', '2,5', '2,6'],
             ['3,0', '3,2', '3,3', '3,4', '3,5', '3,6'],
             ['4,0', '4,2', '4,3', '4,4', '4,5', '4,6'],
             ['5,0', '5,2', '5,3', '5,4', '5,5', '5,6'],
             ['6,0', '6,2', '6,3', '6,4', '6,5', '6,6']]
for row in fakeTable:
    print(row)
print("\nWhat you see above is the way that your board will be spread out\n\n\tYou will have 5 ships:\n")
print("1 battleship, takes 5 spaces\n1 cruiser that takes up 4 spaces\n1 submarine that takes up 3 spaces")
print("1 destroyer that takes 2 spaces\n1 spy ship that takes up 1 space")
print("\n\nPlayer 1, take the computer and don't show your oponent")
sleep(2)
ready = input("Ready? [y/n]\n")
if ready == "yes" or ready == "y":
    player1Start()
    print("You have 4 seconds to pass the computer to the other player so that they can set up")
    sleep(5)
    player2Start()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLets Start!")
    print("Player 1 will start you have 2 seconds to hand back the computer")
    sleep(2)


elif ready == "no" or ready == "n":
    print("Ok then")
    import sys
    sys.exit()

else:
    print("Ok then")
    import sys

    sys.exit()
