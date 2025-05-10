print("Welcome to my computer quiz!")

play_on = True

while play_on:
    playing = input ("wanna play ? Y/N :: ").strip().upper() # handles spaces and converts to upper
    if playing == 'N':
        print("okay maybe next time!\n")
        play_on = False
    elif playing == 'Y':
        print("great!!\n")
    else:
        print("Invalid Input")

#making changes here 
#yeah the changes are visible 