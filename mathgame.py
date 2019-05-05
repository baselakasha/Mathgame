import sqlite3
import random
db = sqlite3.connect('database.db')
c=db.cursor()
c.execute("CREATE TABLE IF NOT EXISTS data(name TEXT , highscore REAL)")
db.commit()

def welcome(name,highscore): # Display the welcoming message 
    print("                    Hello {} ! \n\n                    Welcome to Maths game \n\n                    Your high score : {}\n\n____________________________________________________________\n\n".format(name,highscore))
    input("Press Enter to start")
    
def main():
    print("____________________________________________________________\n\n                         [MATH GAME]\n\n____________________________________________________________\n")
    data=c.execute("SELECT * FROM data")

    # Count the number of the table's rows 
    x=0
    for i in data:
        x=x+1
        
    if x==0: # If empty (first run)
        # Ask about the user name
        ask=True
        while ask:
            try:
                name = input("[+] Please Enter your name : ")
                if name=="" or len(name)==0:
                    print("Please Enter a valid value !")
                else:
                    ask=False                
            except valueError:
                print("Please Enter a valid value")
                askName()
                
        print("\n___________________________________________________________\n")
        c.execute("INSERT INTO data VALUES(?,?)",(name,"0")) # Set the name in database 
        db.commit()  
        welcome(name,"0")
        highscore=0
        
    else: # User played before
        data=c.execute("SELECT * FROM data")
        for i in data: # Get the name and highscore        
            name=i[0]
            highscore=i[1]
        welcome(name,highscore)
        
    score=0
    lose=False
    while lose!=True:
        calc=random.randint(0,1) # Generate a random calculation type 0=[+] 1=[*]

        if calc==0: #(+)
            fnum=random.randint(2,50) # First number
            snum=random.randint(2,50) # Second number
            result=fnum+snum
            inp="[+] {} + {} = " # User input text
            
        else: #(*)
            fnum=random.randint(1,10)
            snum=random.randint(1,10)
            result=fnum * snum
            inp="[+] {} * {} ="
            
        def askUser(): # Ask user what is the result
                userInput=input(inp.format(fnum,snum))
                try:
                    userInput=int(userInput) # Try to make input as int
                    return userInput
                except: # If user input a text or leaft it empty
                    print("Enter a valid value")
                    askUser() # Reask again
        userInput=askUser()
        
        if userInput==result: # Correct answer 
             score=score+1 
             if score>highscore: # If this score is the high score 
                 c.execute("UPDATE data SET highscore =  ? WHERE name = ?",(score,name)) # Change highscore in database
                 db.commit()
                 print("Correct ! , High score ! your score : {} ".format(score)) # Show message
             else: # The score is not the highscore
                 print("Correct ! your score : {}".format(score))

        else: # Wrong answer
            score=0
            print("Oops ! Wrong Answer!")
            userAgain=input("[+] Play again? (y,n) : ").lower()
            if userAgain=="n":
                print("Good bye !")
                db.close()
                lose=True
main()

