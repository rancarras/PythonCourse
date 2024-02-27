import animals

myMammal = animals.Mammals()
myMammal.printMembers()

myBird = animals.harmless.Birds()
myBird2 = animals.dangerous.Birds()
myBird.printMembers()
myBird2.printMembers()

myFish = animals.dangerous.Fish()
myFish.printMembers()