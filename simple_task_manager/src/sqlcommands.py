import sqlite3
from createdb import Databaze  # Importing the database creation class

class DatabaseManagement(Databaze):
    def __init__(self):
        super().__init__()  # Initialize the parent class (Databaze)
        self.con = sqlite3.connect("todolist.db")
        self.con.execute('PRAGMA foreign_keys = ON')
        self.con.commit()
        self.cursor = self.con.cursor()

    ####### ✅ USERS CRUD ########
    def readUsers(self):
        self.cursor.execute("SELECT * FROM Users")
        return self.cursor.fetchall()

    def insertUser(self, name, email):
        self.cursor.execute("INSERT INTO Users(name, email) VALUES(?, ?)", (name, email))
        self.con.commit()

    def updateUser(self, name, email, UserID):
        self.cursor.execute("UPDATE Users SET name = ?, email = ? WHERE UserID = ?", (name, email, UserID))
        self.con.commit()

    def deleteUser(self, UserID):
        self.cursor.execute("DELETE FROM Users WHERE UserID = ?", (UserID,))
        self.con.commit()

    def readUser(self, id=None, name=None):
        self.cursor.execute("SELECT * FROM Users WHERE UserID = ? OR name = ?", (id, name))
        return self.cursor.fetchall()

    ####### ✅ TAGS CRUD ########
    def readTags(self):
        self.cursor.execute("SELECT * FROM tags")
        return self.cursor.fetchall()

    def insertTag(self, tagname):
        """Inserts a tag if it doesn't exist and returns its ID."""
        self.cursor.execute("INSERT OR IGNORE INTO tags(tag) VALUES(?)", (tagname,))
        self.cursor.execute("SELECT Usertag_id FROM tags WHERE tag = ?", (tagname,))
        return self.cursor.fetchone()[0]  # Fetch the tag's ID

    def updatetag(self, tagID, tagname):
        self.cursor.execute("UPDATE tags SET tag = ? WHERE Usertag_id = ?", (tagname, tagID))
        self.con.commit()

    def deletetag(self, tagID):
        self.cursor.execute("DELETE FROM tags WHERE Usertag_id = ?", (tagID,))
        self.con.commit()

    def readtag(self, id=None, tagname=None):
        self.cursor.execute("SELECT * FROM tags WHERE Usertag_id = ? OR tag = ?", (id, tagname))
        return self.cursor.fetchall()

    def readTagsForTask(self, TaskID):
        self.cursor.execute("""
            SELECT tags.tag 
            FROM tasks_tags 
            INNER JOIN tags ON tasks_tags.Usertag_id = tags.Usertag_id
            WHERE tasks_tags.UserTasks_id = ?
        """, (TaskID,))
        
        return self.cursor.fetchall()


    ####### ✅ USER DETAILS CRUD ########
    def create_user_detail(self, UserID, email, phone_number, address):
        self.cursor.execute("INSERT INTO UserDetails(UserID, Email, phone_number, adress) VALUES(?,?,?,?)",
                            (UserID, email, phone_number, address))
        self.con.commit()

    def readUserDetails(self):
        self.cursor.execute("SELECT * FROM UserDetails")
        return self.cursor.fetchall()

    def updateUserDetails(self, UserID, Email, phone_number, adress):
        self.cursor.execute("UPDATE UserDetails SET Email = ?, phone_number = ?, adress = ? WHERE UserID = ?",
                            (Email, phone_number, adress, UserID))
        self.con.commit()

    def deleteUserDetails(self, UserID):
        self.cursor.execute("DELETE FROM UserDetails WHERE UserID = ?", (UserID,))
        self.con.commit()

    def readUserDetails(self, id=None, Email=None):
        self.cursor.execute("SELECT * FROM UserDetails WHERE UserID = ? OR Email = ?", (id, Email))
        return self.cursor.fetchall()

    ####### ✅ TASKS CRUD ########
    def readtasks(self):
        self.cursor.execute("SELECT * FROM tasks")
        return self.cursor.fetchall()

    def addTask(self, user_id, task_details, due_date, status, tags_list):
        # Step 1: Insert Task into 'tasks' table
        self.cursor.execute("""
            INSERT INTO tasks (UserID, Task_Details, Due_date, status) 
            VALUES (?, ?, ?, ?)
        """, (user_id, task_details, due_date, status))
        
        self.conn.commit()
        
        # Step 2: Get the last inserted Task ID
        task_id = self.cursor.lastrowid
        
        # Step 3: Insert tags and link them to the task
        for tag in tags_list:
            # Check if tag exists, if not, insert it
            self.cursor.execute("SELECT Usertag_id FROM tags WHERE tag = ?", (tag,))
            result = self.cursor.fetchone()

            if result:
                tag_id = result[0]  # Tag already exists
            else:
                # Insert new tag
                self.cursor.execute("INSERT INTO tags (tag) VALUES (?)", (tag,))
                self.conn.commit()
                tag_id = self.cursor.lastrowid  # Get new tag ID
            
            # Step 4: Insert into tasks_tags table to link task and tag
            self.cursor.execute("""
                INSERT INTO tasks_tags (UserTasks_id, Usertag_id) 
                VALUES (?, ?)
            """, (task_id, tag_id))
        
        self.conn.commit()
        return task_id  # Return the new Task ID

    def updatetask(self, TaskID, status):
        self.cursor.execute("UPDATE tasks SET status = ? WHERE UserTasks_id = ?",
                            ( status,TaskID, ))
        self.con.commit()

    def deletetask(self, TaskID):
        self.cursor.execute("DELETE FROM tasks_tags WHERE UserTasks_id = ?", (TaskID,))
        self.con.commit()
        
        # Then, delete the task from the tasks table
        self.cursor.execute("DELETE FROM tasks WHERE UserTasks_id = ?", (TaskID,))
        self.con.commit()
        
    def readtask(self, id):
        self.cursor.execute("SELECT * FROM tasks WHERE UserTasks_id = ?", (id,))
        return self.cursor.fetchall()
    
    def readTagsForTask(self, task_id):
        self.cursor.execute("""
            SELECT tags.tag 
            FROM tags
            JOIN tasks_tags ON tags.Usertag_id = tasks_tags.Usertag_id
            WHERE tasks_tags.UserTasks_id = ?
        """, (task_id,))
        
        return self.cursor.fetchall()
    def remove_tag_from_task(self, task_id, tag_id):
        """Removes the association between a task and a tag."""
        try:
            self.cursor.execute("""
                DELETE FROM tasks_tags
                WHERE UserTasks_id = ? AND Usertag_id = ?
            """, (task_id, tag_id))

            self.conn.commit()
            print(f"Tag {tag_id} removed from Task {task_id} successfully.")

        except sqlite3.Error as e:
            print(f"Error removing tag from task: {e}")
            
            return self.cursor.fetchall()  


    ####### ✅ CLOSE CONNECTION ########
    def close_connection(self):
        self.con.close()
