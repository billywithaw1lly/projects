print("Welcome to my computer quiz!")

play_on = True

score = 0

def questions():
    global score

    answer1 = input("What does CPU stands for ?\n A : control processing unit\n B : central progeccing unit\n C : control processed unit\n D : central processed unit \n").strip().upper()
    if answer1 == 'B':
        score +=1
        print("correct\n")
    else:
        print("incorrect\n")

    answer2 = input("how many colours are in a rainbow ?\n A : 6\n B : 7\n C : 8\n D : 9 \n").strip().upper()
    if answer2 == 'B':
        score +=1
        print("correct\n")
    else:
        print("incorrect\n")

    answer3 = input("wavelength of colour red in nanometer ?\n A : 650\n B : 550\n C : 750\n D : 850 \n").strip().upper()
    if answer3 == 'A':
        score +=1
        print("correct\n")
    else:
        print("incorrect\n")

    print(f"\nYour final score is: {score}/3\n")





while play_on:
    while True:
        playing = input ("wanna play ? Y/N :: ").strip().upper() # handles spaces and converts to upper
        if playing == 'N':
            print("okay maybe next time!\n")
            play_on = False
            quit() #quits the program

        elif playing == 'Y':
            print("great!!\n")
            questions()
            break
        else:

            print("Invalid Input")