print("Hockey Team Performance Calculator!")
teamName = input("Enter your team name: ") 
wins = input("Enter season Wins: ")
losses = input("Enter season Losses: ")  

games=(int(wins)+int(losses))

winLoss = (int(wins)/games)*100
print("The win percentage for the",teamName, "is: {0:.4f}%" .format(winLoss)) 
print("They have won",int(wins),"of their",games,"games this season.")