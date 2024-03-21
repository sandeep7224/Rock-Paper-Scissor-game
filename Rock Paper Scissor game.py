import random
def rules():
    print("\n\nRules for the game")
    print("Between Rock and paper = paper win")
    print("Between rock and scissor = rock win")
    print("Between scissor and paper = scissor win")
   

print("Welcome to rock , paper , scissor game")
print("please select the game mode")
a= int(input("Enter 1 for FRIEND    and    Enter 2 for Computer = "))

print("\n\nInsruction for the game")
print("1. For Rock enter 'r' ")
print("2. For Scissor enter 's' ")
print("3. For Paper enter 'p' ")
if(a==1):
    rules()
    user1 = str(input("\nfirst player enter the option = "))
    user2 = str(input("\nsecond player enter the option = "))
    if(user1 == "r" and user2 == "s"):
        print("first player win the game")
    if(user1 == "r" and user2 == "p"):
        print("second player win the game")
   
   
    if(user1 == "p" and user2 == "r"):
        print("first player win the game")
    if(user1 == "p" and user2 == "s"):
        print("second player win the game")
       
       
    if(user1 == "s" and user2 == "p"):
        print("first player win the game")
    if(user1 == "s" and user2 == "r"):
        print("second player win the game")
       
    if((user1 == "s" and user2 == "s") or (user1 == "p" and user== "p") or (user1 == "r" and user2 == "r")):
        print("GAME tie (Please choice different option")
         
       
    print("\n\nThanks for playing the game")
    print("Please visit again")
       
if(a==2):
    rules()
    user2 = random.randint(1,3)
   
    user1 = str(input("\n\nUser please enter the optionn = "))
   
    if(user1 == "r" and user2 == 3):
        print("you win the game")
    if(user1 == "r" and user2 == 2):
        print("Computer win the game")
   
   
   
    if(user1 == "p" and user2 == 1):
        print("you win the game")
    if(user1 == "p" and user2 == 3):
        print("Computer win the game")
       
       
    if(user1 == "s" and user2 == 2):
        print("you win the game")
    if(user1 == "s" and user2 == 1):
        print("Computer win the game")
       
    if((user1 == "s" and user2 == 3) or (user1 == "p" and user2 == 2) or (user1 == "r" and user2 == 1)):
        print("GAME tie (you have both choice the same option")
       
    print("\n\nThanks for playing the game")
    print("Please visit again")