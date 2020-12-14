print("christmas is in danger! Santa is kidnapped!")
print("you're not really anyone special but you decided it was you that was going to save christmas.")
print("when playing this game you get up to 2 choices each time and have to decide between them by writing either 1, 2 or 3 no other options are available and only one option is correct")
print(".......................")
variable = 1

print("after having a dream about santa getting kidnapped you knew you had to save him but before going to save santa you had to get more information")
while variable <3>0:
    val1=int(input("you can choose between the following 1.the wise tree 2. an information broker"))
    if val1 == 1: 
        print("you went to the wise tree to see if he knew where santa was")
        print("the tree said it knew and then told you santa was held in a warehouse two towns over")
        val2=int(input("now that you had the information"))

    elif val1 == 2:
        print("you went to a information broker because surely they had the information you wanted so you went and asked where santa was being kept by the kidnappers")
        val2=int(input("he said sure but it will cost you will you pay the fee for the information 1. yes i will pay the 1000$ or also known all my money 2. no you won't pay and goes back home to choose again"))
        if val2 == 1:
            print("congrats you're now broke but atleast you got the information or so you thought ")
            print("because what the information broker says next makes you think that you have wasted that money")
            print("he said santa isn't real and then just walked away")
            print("how will you now travel to where santa is kidnapped if you do not have the money to travel even if you dont know where that is")
            variable=5 
        elif val2==2:
            print("you instead decided to go back and decide again")

print("GAME OVER")
            
    
