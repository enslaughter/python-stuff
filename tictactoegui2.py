#alltheeggs
import tkinter as tk

#initialization block
gameBoard = [[0,0,0], [0,0,0], [0,0,0]]

currentPlayer = 1
gameFinished = 0
turnNumber = 1
gameWon = 0
rowDef = 0
colDef = 0
playerInput = 0

#Tkinter GUI Setup
gameWindow = tk.Tk()
gameWindow.title("Tic Tac Toe")
gameWindow.rowconfigure([0, 1, 2], minsize=50, weight=1)
gameWindow.columnconfigure([0, 1, 2], minsize=50, weight=1)

buttonarray = gameBoard
E="E"
buttontext = [[E,E,E], [E,E,E], [E,E,E]]

textframe = tk.Frame(master=gameWindow, width = 150, height = 100)
textframe.pack()

for i in range(3):
	for j in range(3):
		buttonframe = tk.Frame(master=gameWindow, relief=tk.RAISED, borderwidth=1)
		buttonframe.grid(row=i, column=j)
		buttonframe.pack()
		
		buttontext[i][j] = tk.StringVar()
		buttontext[i][j].set(" - ")
		buttonarray[i][j] = tk.Button(master=buttonframe, textvariable=buttontext[i][j], command = lambda i=i,j=j: ButtonClicked(i,j))
		buttonarray[i][j].grid(row=i, column=j, sticky="nesw")
		buttonarray[i][j].pack()
		
def ButtonClicked(rowID,colID):
	buttontext[rowID][colID].set("X")

gameWindow.mainloop()

def GetPlayerInput(turnNumber, gameBoard):
	validTurn = 0
	
	while validTurn == 0:
		playerInput = int(input('Player ' + str(currentPlayer) + ' : Enter your move\n'))
	
		if not (1<=playerInput<=9) or gameBoard[(playerInput-1)//3][(playerInput-1)%3] != 0:
			print('Invalid Input. Enter a number from 1 to 9 on a free space')
			continue
			
		else:
			return playerInput
			break
		
def CheckWinCondition(gameBoard, playerInput):
	rowDef = (playerInput-1)//3
	colDef = (playerInput-1) % 3
	
	#check vertical WC
	if gameBoard[rowDef][0] == gameBoard[rowDef][1] == gameBoard[rowDef][2] != 0:
		return 1
		
	#check horizontal WC
	if gameBoard[0][colDef] == gameBoard[1][colDef] == gameBoard[2][colDef] != 0:
		return 1
		
	#check 1st diagonal WC
	if gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2] != 0:
		return 1
		
	#check 2nd diagonal WC
	if gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0] != 0:
		return 1
		
	#if no condition is met
	else:
		return 0
	

while gameFinished == 0:
	playerInput = GetPlayerInput(turnNumber, gameBoard)
	
	gameWon = CheckWinCondition(gameBoard, playerInput)
	if gameWon == 1:
		print('Congratulations Player ' + str(currentPlayer) + '! You win!')
		break
	
	if currentPlayer == 1:
		currentPlayer = 2
	else:
		currentPlayer = 1
		
	turnNumber += 1
	print("\nTurn Number: " + str(turnNumber))
	if turnNumber > 9:
		print('Board is filled! Draw')
		break

input('Game Complete! Enter Anything to Exit\n')