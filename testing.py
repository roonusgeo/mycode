Ravenclaw=0
Hufflepuff=1
Gryffindor=2
Slytherin=4

# create a dictionary where the keys are the scores and the values are the house names
tempdict = {Ravenclaw:"Ravenclaw",Hufflepuff:"Hufflepuff",Slytherin:"Slytherin",Gryffindor:"Gryffindor"}

# grab the key with the highest value
biggestkey= max(tempdict)

# use that key to return a value (which is the name of the house)
winner= tempdict[biggestkey]

print(winner)
