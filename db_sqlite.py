import sqlite3

def insert_data(life_meaningless, scared_withoutreason, over_react, close_panic, relax_diff, work_initiate, worth_less):
 conn = sqlite3.connect('demo.db') 
 cursor = conn.cursor()
 print("Database created and Successfully Connected to SQLite")
 
 # sql='''CREATE TABLE d2(
    # travel_date VARCHAR,
    # travel_period VARCHAR,
    # trip_type VARCHAR,
    # adults VARCHAR,
    # child VARCHAR,
    # budget VARCHAR,
    # email VARCHAR,
    # phno VARCHAR
  # )'''
 cursor.execute('''INSERT INTO d2(life_meaningless, scared_withoutreason, over_react, close_panic, relax_diff, work_initiate, worth_less) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (life_meaningless, scared_withoutreason, over_react, close_panic, relax_diff, work_initiate, worth_less))
   
	
 print("Table created successfully........")

 # Commit your changes in the database
 conn.commit()

 #Closing the connection
 conn.close()

 
#if __name__ == "__main__":
 #insert_data('12-10-2017',3, 'adventure', 2, 1, 6000, 'qwerty@gmail.com', 987654321)
 
