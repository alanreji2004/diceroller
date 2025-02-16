import random
print("how many dice would you like to roll")
while True:
    try:
        number = int(input("type an integer between 1 and 10\n"))
        if(number > 0 and number <10):
            break;
        else:
            print("invalid entry!please try again")
    except :
            print("provide an integer!")
            
def rollDice(amountOfDice):
    totalsum = 0;
    possibleFaces = [1,2,3,4,5,5,6]
    for die in range (amountOfDice):
        roll = random.choice(possibleFaces)
        print("die",die+1,";",roll)
        totalsum += roll
    print("total sum",totalsum)
    
rollDice(number)

