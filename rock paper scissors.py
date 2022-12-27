import random
Cchoice=["Rock","Paper","Scissors"]             
while True:
        youwin,computerwin=0,0
        print("Rock Paper scissors Game:")
        
        for i in range(1,6):                    # 5 Round game
                print("Round",i,"Start:")
                print("Please select any one option:")
                print("1.Rock","2.Paper","3.Scissors",sep="\n") #choose any number(1,2 or 3)
                Yourchoice=int(input())
                if Yourchoice==1:
                        print("You selected: Rock")
                        Yourchoice="Rock"
                elif Yourchoice==2:
                        print("You selected: Paper")
                        Yourchoice="Paper"
                elif Yourchoice==3:
                        print("You selected :Scissor")
                        Yourchoice="Scissors"
                else:
                        print("Invalid Choice")
                        break
                Computerchoice=random.choice(Cchoice)  
                print("Computer selected:",Computerchoice)
                if Yourchoice==Computerchoice:    
                        youwin+=1
                        computerwin+=1
                        print("This Round is Draw:")
                elif (Yourchoice=="Paper" and Computerchoice=="Rock") or (Yourchoice=="Rock" and Computerchoice=="Scissors") or(Yourchoice=="Scissor" and Computerchoice=="Paper"):
                        youwin+=1
                        print("You won this Round")
                else:
                        computerwin+=1
                        print("Computer won this Round")
        if youwin>computerwin:
                print("You Won the game:")
                print("Score is:","Your score:",youwin,"Computer score:",computerwin,sep=" ")
        elif computerwin>youwin:
                print("You Lost the game. Computer win the game:")
                print("Score is:","Your score:",youwin,"Computer score:",computerwin,sep=" ")
        else:
                print("Match Drawn")
                print("Score is:","Your score:",youwin,",Computer score:",computerwin,sep=" ")
        user_choice=input("Want to Play again?(Yes/Exit)")
        if user_choice=='yes' or user_choice=='Yes' or user_choice=='YES':
                continue             
        else:
                break

