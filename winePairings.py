from random import shuffle

nameFile = open('names.txt')
people = [line.rstrip('\n') for line in nameFile]
shuffle(people)
pairs = []
for x in range(len(people) // 2):
	pairs.append([people[2*x], people[2*x + 1]])
	print(str(x) + ": " + people[2*x] + ", " + people[(2*x) + 1])

invalidPairs = input("Enter invalid pair numbers: ")
while invalidPairs:
	invalidList = []
	invalidPairs = [int(invalidPair) for invalidPair in invalidPairs.split()]
	for invalidPair in invalidPairs:
		invalidList.append(pairs[invalidPair][0])
		invalidList.append(pairs[invalidPair][1])
	shuffle(invalidList)
	for index, invalidPair in enumerate(invalidPairs):
		pairs[invalidPair] = [invalidList[2 * index], invalidList[2 * index + 1]]
	for x in range(len(people) // 2):
		print(str(x) + ": " + pairs[x][0] + ", " + pairs[x][1])		
	invalidPairs = input("Enter invalid pair numbers: ")

print("FINAL LIST: ")
for x in range(len(people) // 2):
	print(str(x) + ": " + pairs[x][0] + ", " + pairs[x][1])	
