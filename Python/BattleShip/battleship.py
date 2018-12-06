import time

numRow = 6
numCol = 6
board1 = [[False for column1 in range(numCol)] for row1 in range(numRow)]
board2 = [[False for column2 in range(numCol)] for row2 in range(numRow)]


def setShip1(coords):
    if len(coords) == 2:
        coord1 = coords[0]
        coord2 = coords[2]
        board1[coord1][coord2]

print("Welcome to Felipe's Battleship game\nDecide who will play first and pass the computer to them")
print("Waiting for 5 seconds...")
time.sleep(5)
print("Alright Player 1, Let's start\n\n")
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
time.sleep(1)
ready = input("Ready? [y/n]\n")
if ready == "yes" or ready == "y":
    print("Let's start setting up your board")
    print("First we will set up your 1 space spy-ship:\n")
    coordinates = input("Enter the coordinates for your ship. Example: 3,3 or 1,2\n(Type it with a comma)\n\t")
    print(coordinates)
    setShip(1,coordinates)
    print(board1)
elif ready == "no" or ready == "n":
    print("Ok then")
    import sys

    sys.exit()

else:
    print("Ok then")
    import sys

    sys.exit()
