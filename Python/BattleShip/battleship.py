import time
print("Welcome to Felipe's Battleship game\nDecide who will play first and pass the computer to them")
print("Waiting for 5 seconds...")
time.sleep(5)
print("Alright Player 1, Let's start\n\n")
fakeTable = [['A1', 'A2', 'A3', 'A4', 'A5', 'A6'],
['B1', 'B2', 'B3', 'B4', 'B5', 'B6'],
['C1', 'C2', 'C3', 'C4', 'C5', 'C6'],
['D1', 'D2', 'D3', 'D4', 'D5', 'D6'],
['E1', 'E2', 'E3', 'E4', 'E5', 'E6'],
['F1', 'F2', 'F3', 'F4', 'F5', 'F6']]
for row in fakeTable:
    print(row)
print("\nWhat you see above is the way that your board will be spread out\n\n\tYou will have 5 ships")
print("You will have the following type of ships:")
print("1 battleship, takes 5 spaces\n1 cruiser that takes up for spaces\n1 submarine that takes up 3 spaces")
print("\n1 destroyer that takes two spaces\n And one spy ship that takes up 1 space")
