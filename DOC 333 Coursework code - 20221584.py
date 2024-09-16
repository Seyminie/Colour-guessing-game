import random

def Main():
    
    #Initialize variables
    Game=0
    S_Name=0
    Game_opt="No"
    key1=0
    key2=0
    key3=0
    key4=0
    key=[]
    Attempt=0
    n=1
    v_input="No"
    v_Guess="No"
    v_length="No"
    Guess=0
    Continue=True
    Replay=0

    B_pegs=0
    W_pegs=0
    N_pegs=0

    v_black1="No"
    v_black2="No"
    v_black3="No"
    v_black4="No"

    v_white1="No"
    v_white2="No"
    v_white3="No"
    v_white4="No"
    


    #Process

    while Continue==True:

        if Game_opt=="No":
            
            try:
                Game=input("Would you like to start the game(Yes/No): ")
                
                if Game in["YES","Yes","yes","NO","No","no"]:
                    Game_opt="Yes"
                else:
                    print("Invalid input")
                    Game_opt="No"
                    print()

            except:
                print("Invalid input")
                Game_opt="No"

            if Game_opt=="Yes" and Game in["NO","No","no"]:                
                Game_opt="No"
                print("Good Bye!! See you again!!")
                exit()                

            if Game_opt=="Yes" and Game in ["Yes","YES","yes"]:
                print()

            S_Name=(input("Enter your name: "))
            print("Hello "+S_Name+" Welcome to GameInt")
            print()



            print("................................................................................Instructions............................................................................................")
            print()
            print("1. Guess a 4 Colour code for the hidden pegs")
            print("2. You are provided with 8 Attempts to guess the hidden code")
            print("3. Numbers and represented colours-- 1-White 2-Blue 3-Red 4-Yellow 5-Grees 6-Purple")
            print("4. Duplication of numbers are allowed")
            print("5. After each attempt a validation of the entered number is provided using black and white pegs")
            print("6. Black(1) will indicate that correct colour in correct position")
            print("7. White(0) will indiate that correct colour is in wrong position")
            print("8. # will idicate wrong colour in wrong position")
            print()
            print("Best of Luck!!!")
            print()
            print()
            print("Guess the hidden code - x x x x ")
            

            key1=random.randint(1,6)
            key2=random.randint(1,6)
            key3=random.randint(1,6)
            key4=random.randint(1,6)

            key.append(key1)
            key.append(key2)
            key.append(key3)
            key.append(key4)
            key=list(key)

            print()

            while n<=8:

                B_pegs=0
                W_pegs=0
                N_pegs=0
                v_input="No"
                v_length="No"
                v_Guess="No"

                if v_input=="No" or v_length=="No" or v_Guess=="No":

                    Attempt=str(input("\nEnter your Attempt"+str(n)+":"))
                   

                if Attempt=="0000":
                    print()
                    print("Game ended______Good Bye!!")
                    Continue=False
                    exit()

                if v_input=="No":

                    try:
                        int(Attempt)
                        v_input="Yes"

                        Guess=map(int,Attempt)
                        Guess_list=list(Guess)

                    except:
                        print("Enter a valid integer")                       
                        v_input="No"

                if v_input=="Yes" and v_length=="No":

                    if len(Guess_list)==len(key):
                        v_length="Yes"

                    else:
                        v_length="No"
                        print("Enter only 4 colours")                        

                   
                if v_input=="Yes" and v_length=="Yes" and v_Guess=="No":

                    if Guess_list[0]>0 and Guess_list[0]<7:
                        if Guess_list[1]>0 and Guess_list[1]<7:
                            if Guess_list[2]>0 and Guess_list[2]<7:
                                if Guess_list[3]>0 and Guess_list[3]<7:
                                    v_Guess="Yes"
                                    n=n+1
                                    
                                    

                    if v_Guess=="No":
                        print("Enter a value between range 1-6")                      
                        v_Guess="No"

                if v_input=="Yes" and v_length=="Yes" and v_Guess=="Yes":                
                    print("Colours you guessed are: ",Guess_list)
                                      
                    #Validation of guessed numbers
                    print("Validation of guessed numbers are: ",end='')

                    #Validation of 1st colour
                    if Guess_list[0]==key[0]:
                        B_pegs+=1
                        print("1",end='')
                        v_black1="Yes"

                    else:
                        v_black1="No"

                    if v_black1=="No":                    
                        if Guess_list[0] in key:
                            print("0",end='')
                            W_pegs+=1
                            v_white1="Yes"

                        else:
                            v_white1="No"

                        if v_white1=="No":
                            print("#",end='')
                            N_pegs+=1
                            v_black1="Yes"
                            v_white1="Yes"


                    #Validation of 2nd colour
                    if Guess_list[1]==key[1]:                    
                        B_pegs+=1
                        print("1",end='')
                        v_black2="Yes"

                    else:
                        v_black2="No"

                    if v_black2=="No":                    
                        if Guess_list[1] in key:
                            print("0",end='')
                            W_pegs+=1
                            v_white2="Yes"

                        else:
                            v_white2="No"

                        if v_white2=="No":
                            print("#",end='')
                            N_pegs+=1
                            v_black2="Yes"
                            v_white2="Yes"


                    #Validation of 3rd colour
                    if Guess_list[2]==key[2]:
                        B_pegs+=1
                        print("1",end='')
                        v_black3="Yes"

                    else:
                        v_black3="No"

                    if v_black3=="No":                    
                        if Guess_list[2] in key:
                            print("0",end='')
                            W_pegs+=1
                            v_white3="Yes"

                        else:
                            v_white3="No"

                        if v_white3=="No":
                            print("#",end='')
                            N_pegs+=1
                            v_black3="Yes"
                            v_white3="Yes"

                    #Validation of 4th colour
                    if Guess_list[3]==key[3]:
                        
                        B_pegs+=1
                        print("1",end='')
                        v_black4="Yes"

                    else:
                        v_black4="No"

                    if v_black4=="No":                    
                        if Guess_list[3] in key:
                            print("0",end='')
                            W_pegs+=1
                            v_white4="Yes"

                        else:
                            v_white4="No"

                        if v_white4=="No":
                            print("#",end='')
                            N_pegs+=1
                            v_black4="Yes"
                            v_white4="Yes"

                    print()

                    #While getting 8 attempts
                    if B_pegs==4:
                        n=10                        
                        print("All Guesses are correct :)")
                        print("You Won!!!")
                        print("Well played :)")
                        print()

                    if n==9 and B_pegs!=4:
                        n=10
                        print("You lost!!!")
                        print("Try again and hope for better result")
                        print()

                                
            Replay=str(input("Do you want to play another game : "))
            
            if Replay in["YES","Yes","yes"]:
                Main()
                print()
                
            if Replay in["NO","No","no"]:
                print("Good Bye _______________________________ Game ended")
                print()
                exit()
                
                 
                                                                                                
Main()                     
                    
                    
                        

                                   
                     

            
                    

                

                

            

                
        


            
         

      
            
        

    


    

    


        

    
