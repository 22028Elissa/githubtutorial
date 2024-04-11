#docstring- Elissa Piao- Airplance batabse application
#import
import sqlite3

#Contants and variables
DATABASE = "fighters.db"


#functions
def print_all_aircraft():
    '''print all the aircraft nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighter;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    for fighter in results:
        print(fighter)
        #loop finishes here
    db.close()


#main code
print_all_aircraft()