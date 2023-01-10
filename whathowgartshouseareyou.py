#!/usr/bin/env python3

Ravenclaw=0
Hufflepuff=0
Gryffindor=0
Slytherin=0


question1= {"question": "Choose one of the four classical elements",
            "answer": ["water",
                       "air",
                       "fire",
                       "earth",]
           }
           
while True:
    print(question1["question"])

    # key()=Returns a list containing the dictionary's keys
    answer_list= list(question1["answer"])

    print(answer_list)
    
    answer= input(">")

    if answer in answer_list:
        break

    else:
         print("cmon man choose one of the options (eyeroll)")

if answer in answer_list:
        if answer == answer_list[0]:
            Ravenclaw += 1
        elif answer == answer_list[1]:
            Hufflepuff += 1
        elif answer == answer_list[2]:
            Gryffindor += 1
        elif  answer == answer_list[3]:
            Slytherin += 1

    ### CHAD CHANGES
    # hi Maria! this script is AWESOME! to answer your email, here's how you could
    # increment your house scores depending on the answer chosen.
    # I'm pretty sure the first answer is always Ravenclaw, last answer Slytherin,
    # so this code should work for all your questions!

question2= {"question": "Choose your favorite color out of the ones listed below:",
            "answer": ["blue",
                       "yellow",
                       "red",
                       "green",]
           }
           
while True:
    print(question2["question"])

    # key()=Returns a list containing the dictionary's keys
    answer_list= list(question2["answer"])
    
    print(answer_list)
    
    answer= input(">")
    
    if answer in answer_list:
        break
        
    else:
         print("cmon man choose one of the options (eyeroll)") 


if answer in answer_list:
    if answer == answer_list[0]:
        Ravenclaw += 1
    elif answer == answer_list[1]:
        Hufflepuff += 1
    elif answer == answer_list[2]:
        Gryffindor += 1
    elif  answer == answer_list[3]:
        Slytherin += 1
           
           
question3= {"question": "Choose the word that best describes you:",
            "answer": ["Creative",
                       "kind",
                       "courageous",
                       "ambitious",]
           }
           
while True:
    print(question3["question"])

    # key()=Returns a list containing the dictionary's keys
    answer_list= list(question3["answer"])
    
    print(answer_list)
    
    answer= input(">")
    
    if answer in answer_list:
        break
        
    else:
         print("cmon man choose one of the options (eyeroll)")

if answer in answer_list:
    if answer == answer_list[0]:
            Ravenclaw += 1
    elif answer == answer_list[1]:
            Hufflepuff += 1
    elif answer == answer_list[2]:
            Gryffindor += 1
    elif answer == answer_list[3]:
            Slytherin += 1
         
question4= {"question": "what would be your favorite class at hogwarts:",
            "answer": ["history of magic",
                       "herbology",
                       "defense against the dark arts",
                       "potions",]
           }
           
while True:
    print(question4["question"])

    # key()=Returns a list containing the dictionary's keys
    answer_list= list(question4["answer"])
    
    print(answer_list)
    
    answer= input(">")
    
    if answer in answer_list:
        break
        
    else:
         print("cmon man choose one of the options (eyeroll)") 

if answer in answer_list:
    if answer == answer_list[0]:
            Ravenclaw += 1
    elif answer == answer_list[1]:
            Hufflepuff += 1
    elif answer == answer_list[2]:
            Gryffindor += 1
    elif answer == answer_list[3]:
            Slytherin += 1
         
question5= {"question": "you would be most hurt if someone called you?:",
            "answer": ["dumb",
                       "mean",
                       "dull",
                       "weak",]
           }
           
while True:
    print(question5["question"])

    # key()=Returns a list containing the dictionary's keys
    answer_list= list(question5["answer"])
    
    print(answer_list)
    
    answer= input(">")
    
    if answer in answer_list:
        break
        
    else:
         print("cmon man choose one of the options (eyeroll)")

if answer == answer_list[0]:
    Ravenclaw += 1
elif answer == answer_list[1]:
    Hufflepuff += 1
elif answer == answer_list[2]:
    Gryffindor += 1
elif answer == answer_list[3]:
    Slytherin += 1

# to tally up the answers is as follows: 
# create a dictionary where the keys are the scores and the values are the house names
tempdict = {Ravenclaw:"Ravenclaw",Hufflepuff:"Hufflepuff",Slytherin:"Slytherin",Gryffindor:"Gryffindor"}

# grab the key with the highest value
biggestkey= max(tempdict)

# use that key to return a value (which is the name of the house)
winner= tempdict[biggestkey]

print(winner)        

if winner == Ravenclaw:
     print('The Sorting Hat would only put you in this house if you demonstrated excellent wisdom, wit and a skill for learning. Ravenclaws are often known for being quite eccentric and most of the great wizarding inventors and innovators have come from this house. Future scientist maybe?')


#if winner == Ravenclaw:

    #print('The Sorting Hat would only put you in this house if you demonstrated excellent wisdom, wit and a skill for learning. Ravenclaws are often known for being quite eccentric and most of the great wizarding inventors and innovators have come from this house. Future scientist maybe?') 
