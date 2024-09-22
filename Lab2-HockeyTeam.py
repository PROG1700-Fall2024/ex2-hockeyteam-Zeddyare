# LAB 2 - HOCKEY TEAM
#Write a program that will ask the user to enter the name of a hockey team, how many wins the team has and 
# how many losses #the team has.

#The program should calculate and display a single string output containing the team name, it's win-loss 
# ratio and the win #percentage formatted to 4 decimal places.

#Ex: The Calgary Flames have 10 wins and 5 losses, with a win percentage of 0.6667.

#Purpose/Concepts: Input and output to screen, string concatentation, string formatting, datatype casting, 
# simple math operations
 

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    print("Hockey Team Performance Calculator!")
    teamName = input("Enter your team name: ") 
    wins = input("Enter season Wins: ")
    losses = input("Enter season Losses: ")  

    games=(int(wins)+int(losses))

    winLoss = (int(wins)/games)*100
    print("The win percentage for the",teamName, "is: {0:.4f}%" .format(winLoss)) 
    print("They have won",int(wins),"of their",games,"games this season.")










    # YOUR CODE ENDS HERE

main()