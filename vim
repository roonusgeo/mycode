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
           
while true:
    print(question1["question"])

    # key()=Returns a list containing the dictionary's keys
    question1_list= list(question1.keys()) 
    
    print(question1_list[1])
    print(question1_list[2])
    print(question1_list[3])
    print(question1_list[4])
    
    answer= input(">")
    
    if answer in question1_list:
        break
        
     else:
         print("cmon man choose one of the options (eyeroll)")
