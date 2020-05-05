import random

def Intro():

    Play_BlackJack=input("Welcome to the table. You start out with 100 chips and each hand costs 2 chips. Try to get your cards to total 21 by asking for a card if you're under. If you go over, it's a bust. Ready to play? ")

    if(Play_BlackJack == "No" or Play_BlackJack == "no" or Play_BlackJack == "N" or Play_BlackJack == "n"):
        print("Sucks\n")
    elif (Play_BlackJack == "Yes" or Play_BlackJack == "yes" or Play_BlackJack == "Y" or Play_BlackJack == "y" or Play_BlackJack == "YES"):
        print("Good let's start!\n")

def BlackJack():

    j=0
    Coins=100
    print(str(Coins)+" coins.")

    while j<30:

        Bets=0
        Betm=0
        if (Coins>1): #While the user has coins they can play
            Computer_CardH=random.randint(1,10)
            Computer_CardS=random.randint(1,10)
            User_Cards1=random.randint(1,10)
            User_Cards2=random.randint(1,10)
            UCards=[User_Cards1, User_Cards2] #displays cards
            CCards=[Computer_CardH, Computer_CardS]
            Coins-=2
            print()
            User_Move=input("These are your cards "+str(User_Cards1)+ " " + str(User_Cards2)+" \nDo you want to hit? You have "+str(Coins)+ " coins. Each hit costs 5 chips(y/n)")
        else:
            print("Sorry")
            print("Game Over")
            R=input("Play again and start fresh with 100 coins?")
            if (R!=("n")):
                BlackJack()
            else:
                break
              
        i=0
        TwentyOneU=0
        TwentyOneC=0
        TwentyO=0
        TwentyOO=0
        TwentyO=User_Cards1+User_Cards2
        TwentyOneU=TwentyO

        if(Coins>4 and User_Move!="n"):
            i=0
            Coins-=5
            Bets+=1

            while i<9:
                Hit=random.randint(1,10)
                UCards.append(Hit)
                print("\n"+str(UCards))
                TwentyOneU+=Hit

                if (TwentyOneU>21):
                    print("Bust")
                    i+=10    

                elif(Coins>=0):
                    print(str(Coins)+" coins")
                    h=input("\nHit? (y/n)")
                    if (h=="n"):
                        i+=10
                    elif(Coins>4 and h!="n"): #pays coins & makes bet
                        Coins-=5
                        Bets+=1
                        i+=1
                    elif (Coins<5 and h!="n"): #cant hit without sufficient coins
                        i+=10

        if(User_Move=="n" or i>5 or Coins<5):
            print()
            print("Computer cards are "+str(Computer_CardH)+" "+str(Computer_CardS))
            TwentyOO=Computer_CardH+Computer_CardS
            TwentyOneC=TwentyOO

            if(TwentyOneU==TwentyOneC and 17<TwentyOneC<22): 
                i+=10
            elif (TwentyOneU>TwentyOneC and TwentyOneU<22): 
                i=0
                Bets+=1

                while i<9:
                    Hit=random.randint(1,10)
                    CCards.append(Hit)
                    print(CCards)
                    TwentyOneC+=Hit

                    if(TwentyOneC>21):
                        print("Bust")
                        i+=10
                    elif(TwentyOneU==TwentyOneC and 17<TwentyOneC<22):
                        i+=10
                    elif (TwentyOneC>TwentyOneU):
                        i+=10

                    elif(TwentyOneU>=TwentyOneC and TwentyOneU<22):
                        Bets+=1
                        i+=1

                    elif(17<TwentyOneC<=21):
                         i+=10
                         
                    else:
                        Bets+=1
                        i+=1
            elif(TwentyOneU>21 or TwentyOneC>TwentyOneU):
                i+=10
            if(TwentyOneU==TwentyOneC and 17<TwentyOneC<22):
                i+=10
                                   
            if(i>5):
                print("\nYou had "+str(UCards)+" "+str(TwentyOneU)+"  Computer had "+ str(CCards)+" "+str(TwentyOneC))
                if((TwentyOneU>TwentyOneC and TwentyOneU<22) or (TwentyOneC>21 and TwentyOneU<22) ):
                    Betm+=(5*Bets)
                    print("You win "+str(Betm)+" coins")
                    Coins+=Betm
                    print("You have "+str(Coins)+" coins.") 
                    if(Coins!=0):
                        A=input("Again (y/n)?")
                        if (A=="n"):
                            print("Bye!")
                            break
                        else:
                            j+=1
                    else:
                        print("Sorry")
                        print("Game Over")
                        R=input("Play again and start fresh with 100 coins?")
                        if (R!=("n")):
                            BlackJack()
                        else:
                            break

                elif((TwentyOneC>TwentyOneU and TwentyOneC<22) or (TwentyOneU>21 and TwentyOneC<22)):
                    print("You lose")
                    print("You have "+str(Coins)+" coins.") 
                    if(Coins!=0):
                        A=input("Again (y/n)?")
                        if (A=="n"):
                            print("Bye!")
                            break
                        else:
                            j+=1
                    else:
                        print("Sorry")
                        print("Game Over")
                        R=input("Play again and start fresh with 100 coins?")
                        if (R!=("n")):
                            BlackJack()
                        else:
                            break
                    
                else:
                    print("Tie. You have " + str(Coins)+ " coins")
                    j+=1
              
def main():
    Intro()
    BlackJack()

if __name__ == '__main__':

    main()