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
    print(f"name                          speed   max_g climb range payload")
    for fighter in results:
            print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
        #loop finishes here
    db.close()

def print_all_aircraft_in_speed_desc():
    '''print all the aircraft nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighter ORDER BY max_speed DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"name                          speed   max_g climb range payload")
    for fighter in results:
            print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
        #loop finishes here
    db.close()

def print_all_aircraft_by_climbrate_desc():
    '''print all the aircraft nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighter ORDER BY climbrate DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"name                          speed   max_g climb range payload")
    for fighter in results:
            print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
        #loop finishes here
    db.close()

def print_all_aircraft_by_range_desc():
    '''print all the aircraft nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighter ORDER BY range DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"name                          speed   max_g climb range payload")
    for fighter in results:
            print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
        #loop finishes here
    db.close()

def print_all_aircraft_by_payload_desc():
    '''print all the aircraft nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighter ORDER BY payload DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"name                          speed   max_g climb range payload")
    for fighter in results:
            print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
        #loop finishes here
    db.close()

#main code
while True:
    user_input = input("\nWhat would you like to do?. \n1. Print all aircraft\n2. Print all aircraft ordered by speed descending\n3. Print all aircraft ordered by climbrate descending\n4. Print all aircraft ordered by range descending\n5. Print all aircraft ordered by payload descending\n6. Exit\n")
    if user_input == "1":
        print_all_aircraft()
    if user_input == "2":
        print_all_aircraft_in_speed_desc()
    if user_input == "3":
        print_all_aircraft_by_climbrate_desc()
    if user_input == "4":
        print_all_aircraft_by_range_desc()
    if user_input == "5":
        print_all_aircraft_by_payload_desc()
    if user_input == "6":
         break
    else:
        print("\nThat was not an option\n")
