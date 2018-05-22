import sqlite3
import random
db = sqlite3.connect('game.db') # if didnt found database will create it 
c=db.cursor()
c.execute("CREATE TABLE IF NOT EXISTS data(name TEXT , highscore REAL)")
db.commit()

def welcome(name,highscore): # Display welcome message 
	print("                    Hello {} ! \n\n                    Welcome to Math game \n\n                    Your high score : {}\n\n____________________________________________________________\n\n".format(name,highscore))
	input("Press Enter to start ")
	
def main():
	print("____________________________________________________________\n\n                         [MATH GAME]\n\n____________________________________________________________\n")
	data=c.execute("SELECT * FROM data")
	x=0
	for i in data: # check if database table is empty
		x=x+1
	if x==0: # if empty (first open)
		name = input("[+] Please Enter your name : ") 
		print("\n___________________________________________________________\n")
		c.execute("INSERT INTO data VALUES(?,?)",(name,"0")) # set name in database 
		db.commit()  
		welcome(name,"0")
		highscore=0
	else:
		data=c.execute("SELECT * FROM data")
		for i in data: #get name and highscore		
			name=i[0]
			highscore=i[1]
		welcome(name,highscore)
	score=0
	lose=False
	while lose!=True:
		calc=random.randint(0,1) # calculation type 0=[+] 1=[*]
		if calc==0: #(+)
			fnum=random.randint(2,50) #first number
			snum=random.randint(2,50) #second number
			result=fnum+snum
			inp="[+] {} + {} = " #user input text
			
		else: #(*)
			fnum=random.randint(1,10)
			snum=random.randint(1,10)
			result=fnum * snum
			inp="[+] {} * {} ="
		def askUser(): #ask user what is a result
				userInput=input(inp.format(fnum,snum))
				try:
					userInput=int(userInput) #try to make input as int
					return userInput
				except: # if user input text or leave empty
					print("Enter vaild value")
					askUser() # re ask again
		userInput=askUser()
		if userInput==result: #true answer 
			 score=score+1 
			 if score>highscore: # if this score is high score 
			 	c.execute("UPDATE data SET highscore =  ? WHERE name = ?",(score,name)) # change highscore in database
			 	db.commit()
			 	print("True ! , High score ! your score : {} ".format(score)) # show message
			 else: # score is not highscore
			 	print("True ! your score : {}".format(score))
		else: #false answer
			score=0
			print("Oops ! False Answer!")
			userAgain=input("[+] Play Again (y,n) : ").lower()
			if userAgain=="n":
				print("god bye !")
				lose=True
main()






