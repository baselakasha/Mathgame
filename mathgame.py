import sqlite3
db = sqlite3.connect('game.db') # if didnt found database will create it 
c=db.cursor()
c.execute("CREATE TABLE IF NOT EXISTS data(name TEXT , highscore REAL)")
db.commit()

