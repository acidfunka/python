from random import randint

# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

dict = { 0: "rock" , 1: "Spock" , 2: "paper" , 3: "lizard" , 4: "scissors"}

print ("Here are your options")

print ("0 - rock")
print ("1 - Spock")
print ("2 - paper")
print ("3 - lizard")
print ("4 - scissors")
print ("5 - Random")
playerNum = int(input("Choose your item: "))

if (playerNum > 0 and playerNum < 5):
    #print ("Good")
    print ("Player chooses " + dict[playerNum])
    computerNum = randint(0,4)
    print ("Computer chooses " + dict[computerNum])

    playMod = playerNum % 5
    compMod = computerNum % 5
    
##    print (playMod)
##    print (compMod)

    if playMod == compMod:
        print("It is a draw")
    elif playMod > compMod:
        print("Player wins")
    else:
        print("Computer wins")
        
elif playerNum == 5:
    playerNum = randint(0,4)
    computerNum = randint(0,4)

    print ("Player chooses " + dict[playerNum])
    print ("Computer chooses " + dict[computerNum])
    playMod = playerNum % 5
    compMod = computerNum % 5
    
##    print (playMod)
##    print (compMod)

    if playMod == compMod:
        print("It is a draw")
    elif playMod > compMod:
        print("Player wins")
    else:
        print("Computer wins")
else:
    print ("Invalid item!")




