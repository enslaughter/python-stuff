#alltheeggs
import tkinter as tk

#initialization block
gameBoard = [[0,0,0], [0,0,0], [0,0,0]]

currentPlayer = 1
gameFinished = 0
caninit = 1

def CheckWinCondition(rowDef, colDef):
	global gameBoard
	
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
	if caninit == 1:
	
		#Tkinter GUI Setup
		gameWindow = tk.Tk()
		gameWindow.title("Tic Tac Toe")
		
		topframe = tk.Frame(master=gameWindow)
		topframe.grid(row=0, column=0, pady=1, sticky="nsew")
		toptext=tk.Label(master=topframe, text="Player 1s turn")
		toptext.pack()
		
		bottomframe = tk.Frame(master=gameWindow)
		bottomframe.grid(row=1, column=0, sticky="nsew")
		bottomframe.rowconfigure([0, 1, 2], minsize=50, weight=1)
		bottomframe.columnconfigure([0, 1, 2], minsize=50, weight=1)

		buttonarray = [[0,0,0], [0,0,0], [0,0,0]]
		E="E"
		buttontext = [[E,E,E], [E,E,E], [E,E,E]]

		for i in range(3):
			for j in range(3):
				buttonframe = tk.Frame(master=bottomframe, relief=tk.RAISED, borderwidth=1)
				buttonframe.grid(row=i, column=j, padx=1, pady=1, sticky="nsew")
		
				buttontext[i][j] = tk.StringVar()
				buttontext[i][j].set(" - ")
				buttonarray[i][j] = tk.Button(master=buttonframe, textvariable=buttontext[i][j], command = lambda i=i,j=j: ButtonClicked(i,j))
				buttonarray[i][j].grid(row=i, column=j, sticky="nsew")
				
		caninit = 0
		
	else:
		continue
		
	def ButtonClicked(rowID,colID):
		global currentPlayer
		global gameBoard
		
		print("Button clicked row and column is" + str(rowID) + str(colID))
		
		if currentPlayer == 1:
			buttontext[rowID][colID].set("X")
			gameBoard[rowID][colID] = currentPlayer
			currentPlayer = 2
			toptext["text"] = "Player 2s turn"
			
		elif currentPlayer == 2:
			buttontext[rowID][colID].set("O")
			gameBoard[rowID][colID] = currentPlayer
			currentPlayer = 1
			toptext["text"] = "Player 1s turn"
			
		buttonarray[rowID][colID]["state"] = "disable"
		
		wincondition = CheckWinCondition(rowID,colID)
		print("wincondition is " + str(wincondition))
		if wincondition == 1:
			if currentPlayer == 1:
				toptext["text"] = "Player 2 Wins!"
			elif currentPlayer == 2:
				toptext["text"] = "Player 1 Wins!"
				
			for x in range(3):
				for y in range(3):
					buttonarray[x][y]["state"] = "disable"


	gameWindow.mainloop()