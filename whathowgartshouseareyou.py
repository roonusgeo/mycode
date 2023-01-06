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
   
    ### CHAD CHANGES
    # hi Maria! this script is AWESOME! to answer your email, here's how you could
    # increment your house scores depending on the answer chosen.
    # I'm pretty sure the first answer is always Ravenclaw, last answer Slytherin,
    # so this code should work for all your questions!
    if answer in answer_list: 
        if answer == answer_list[0]:
            Ravenclaw += 1
            break
        elif answer == answer_list[1]:
            Hufflepuff += 1
            break
        elif answer == answer_list[2]:
            Gryffindor += 1
            break
        else answer == answer_list[3]:
            Slytherin += 1
            break

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

# The only other thing left to do is to compare each house and announce which has the highest score! You can use the max() function for this;
