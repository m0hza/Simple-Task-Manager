import sqlite3

class Databaze:
    def __init__(self):
        self.conn = sqlite3.connect("todolist.db")
        self.conn.execute('PRAGMA foreign_keys = ON')
        self.cursor = self.conn.cursor()

        # Create tables
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                 UserID INTEGER PRIMARY KEY AUTOINCREMENT,
                 name VARCHAR(100),
                 email VARCHAR(100)
            );
        ''')
        
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS UserDetails(
                 UserDetails_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 UserID INTEGER,
                 Email VARCHAR(100),
                 phone_number VARCHAR(100),
                 address TEXT,
                 FOREIGN KEY(UserID) REFERENCES Users(UserID)
            );
        ''')



        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS tags(
                 Usertag_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 tag VARCHAR(100)
            );
        ''')




        """Create tables if they don't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                UserTasks_id INTEGER PRIMARY KEY AUTOINCREMENT,
                UserID INTEGER,
                Task_Details TEXT,
                Due_date TEXT,
                status TEXT,
                FOREIGN KEY (UserID) REFERENCES Users(UserID) 
            );
        """)


        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks_tags (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                UserTasks_id INTEGER,
                Usertag_id INTEGER,
                FOREIGN KEY (UserTasks_id) REFERENCES tasks(UserTasks_id) ,
                FOREIGN KEY (Usertag_id) REFERENCES tags(Usertag_id) 
            );
        """)
        
        self.conn.commit()
