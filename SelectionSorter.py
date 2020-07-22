from random import seed
from random import randint

randomArray = []

for randIndex in range(10):
	value = randint(0, 100)
	randomArray.append(value)
	
print(randomArray)

randomArray = [1,1,1,1,1,1,1,1,1,1]

for i in range(len(randomArray)):
	minIndex = i

	for j in range(i+1, len(randomArray)):
		if randomArray[j] < randomArray[minIndex]:
			minIndex = j
			
	randomArray[i], randomArray[minIndex] = randomArray[minIndex], randomArray[i]

print(randomArray)
input("End of Program")