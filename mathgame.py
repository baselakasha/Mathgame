import sqlite3
db = sqlite3.connect('game.db') # if didnt found database will create it 
c=db.cursor()
c.execute("CREATE TABLE IF NOT EXISTS data(name TEXT , highscore REAL)")
db.commit()
def welcome(name,highscore): # Display welcome message 
	print("                    Hello {} ! \n\n                    Welcome to Math game \n\n                    Your high score : {}\n\n____________________________________________________________\n\n".format(name,highscore))
	input("Press Enter to start ") #Stop message
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
	else:
		data=c.execute("SELECT * FROM data")
		for i in data: #get name and highscore		
			name=i[0]
			highscore=i[1]
		welcome(name,highscore)
main()