import random
y = "y"
n = "n"
reponse = y or n

roll = input("Do you wish to roll a dice?")

while reponse == y:
    number = random.randint(1,6)
    if (number == 1):
        print("[-----]")
        print("[     ]")
        print("[  0  ]") 
        print("[     ]")
        print("[-----]")
        response = input("Press y to play and n to exit")
    elif (number == 2):
         print("[-----]")
         print("[ 0   ]")
         print("[     ]") 
         print("[    0]")
         print("[-----]")
         response = input("Press y to play and n to exit")
    elif (number == 3):
        print("[-----]")
        print("[     ]")
        print("[0 0 0]") 
        print("[     ]")
        print("[-----]")
        response = input("Press y to play and n to exit")    
    elif (number == 4):
        print("[-----]")
        print("[0   0]")
        print("[     ]") 
        print("[0   0]")
        print("[-----]")
        response = input("Press y to play and n to exit") 
    elif (number == 5):
        print("[-----]")
        print("[0   0]")
        print("[  0  ]") 
        print("[0   0]")
        print("[-----]")  
        response = input("Press y to play and n to exit")    
    elif (number == 6):
        print("[-----]")
        print("[0   0]")
        print("[0   0]") 
        print("[0   0]")
        print("[-----]")
        reponse = input("Press y to play and n to exit")
               
