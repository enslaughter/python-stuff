#alltheeggs

print('Welcome to Tic Tac Toe! Initializing Board...')

#initialization block
gameBoard = [[0,0,0], [0,0,0], [0,0,0]]
E = "E"
guiBoard = [[E,E,E], [E,E,E], [E,E,E]]
currentPlayer = 1
gameFinished = 0
turnNumber = 1
gameWon = 0
rowDef = 0
colDef = 0
playerInput = 0

#introduction statements
print('Board initialized! It starts with Player 1, who enters Os')
print('Please enter a number to signify where you will place your piece:')
print(' 1, 2, 3 \n 4, 5, 6 \n 7, 8, 9')
print('The current game board is: ')
print(" " + str(guiBoard[0][0]) + " " + str(guiBoard[0][1])+ " " + str(guiBoard[0][2]))
print(" " + str(guiBoard[1][0]) + " " + str(guiBoard[1][1])+ " " + str(guiBoard[1][2]))
print(" " + str(guiBoard[2][0]) + " " + str(guiBoard[2][1])+ " " + str(guiBoard[2][2]))


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
	
def UpdateGameBoard(playerInput, gameBoard, currentPlayer, guiBoard, rowDef, colDef):
	rowDef = (playerInput-1)//3	
	colDef = (playerInput-1) % 3

	gameBoard[rowDef][colDef] = currentPlayer
	if currentPlayer == 1:
		guiBoard[rowDef][colDef] = "O"
		
	if currentPlayer == 2:
		guiBoard[rowDef][colDef] = "X"
		
	
def DrawGameBoard(guiBoard):
	print("\n " + str(guiBoard[0][0]) + " " + str(guiBoard[0][1])+ " " + str(guiBoard[0][2]))
	print(" " + str(guiBoard[1][0]) + " " + str(guiBoard[1][1])+ " " + str(guiBoard[1][2]))
	print(" " + str(guiBoard[2][0]) + " " + str(guiBoard[2][1])+ " " + str(guiBoard[2][2]))
	
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
	UpdateGameBoard(playerInput, gameBoard, currentPlayer, guiBoard, rowDef, colDef)
	DrawGameBoard(guiBoard)
	
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