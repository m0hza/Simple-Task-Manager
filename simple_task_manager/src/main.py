
from sqlcommands import DatabaseManagement
import art
import inquirer
from termcolor import colored
from prettytable import PrettyTable

def main():

    databaze = DatabaseManagement()



    ascii_banner = art.text2art("TASK MANAGER")
    print(colored(ascii_banner, 'green'))
    print("welcome to the task manager\nchoose what you want to do:\n")

    actions = ["0.update a task",
        "1. create a user",
        "2. create a user detail",
        "3. create a task",
        "4. Add a tag",
        "5. View all users",
        "6. View all tasks",
        "7. View all tags",
        "8. View all tasks for a user",
        "9. View all tags for a task","10. remove a tag from a task",
        "11. Exit","12. Delete a task"
    ]

    answer = None  # Initialize the answer variable

    while True:

        answer = inquirer.prompt([
            inquirer.List("action",
                          message="Choose an action",
                          choices=actions,
                          ),
        ])["action"]
        if answer == "12. Delete a task":
            TaskID = input("Enter the task's ID: ")
            databaze.deletetask(TaskID)
            print("Task deleted successfully")
        if answer == "0.update a task":
            TaskID = input("Enter the task's ID: ")
            new_status = input("Enter the new status: ")
            databaze.updatetask(TaskID, new_status)
            print("Task updated successfully\n")
            tasks = databaze.readtasks()
            table = PrettyTable(["TaskID", "UserID", "Task_Details", "Due_date", "Status"])
            for task in tasks:
                table.add_row(task)
            print(table)

        if answer == "1. create a user":
            name = input("Enter the user's name: ")
            email = input("Enter the user's email: ")
            databaze.insertUser(name, email)
            print(art.text2art("User created successfully"))


        elif answer == "2. create a user detail":
            UserID = input("Enter the user's ID: ")
            email = input("Enter the user's email: ")
            phone_number = input("Enter the user's phone number: ")
            address = input("Enter the user's address: ")
            databaze.create_user_detail(UserID, email, phone_number, address)
            print(art.text2art("User detail created successfully"))


        elif answer == "3. create a task":
            try:
                user_id = int(input("Enter the User ID: "))
                task_details = input("Enter task details: ")
                due_date = input("Enter due date (YYYY-MM-DD): ")
                status = input("Enter task status: ")
                tags = input("Enter tags (comma-separated please): ").split(",")  # Convert input into a list
                databaze.addTask(user_id, task_details, due_date, status, tags)
                print("Task created successfully with tags!")
            except Exception as e:
                print(f"An error occurred: {e}")


        elif answer == "4. Add a tag":
            tag = input("Enter the tag: ")
            databaze.insertTag(tag)
            print("Tag created successfully")



        elif answer == "5. View all users":
            users =databaze.readUsers()
            table = PrettyTable( ["UserID", "Name", "Email"])
            for user in users:
                table.add_row(user)
            print(table)



        elif answer == "6. View all tasks":
            tasks = databaze.readtasks()
            table = PrettyTable(["TaskID", "UserID", "Task_Details", "Due_date", "Status"])
            for task in tasks:
                table.add_row(task)
            print(table)
                



        elif answer == "7. View all tags":
            tags = databaze.readTags()
            table = PrettyTable(["Tag ID", "Tag Name"])
            for tag in tags:
                table.add_row(tag)
            print(table)



        elif answer == "8. View all tasks for a user":
            UserID = input("Enter the user's ID: ")
            tasks = databaze.readtask(UserID)
            table = PrettyTable(["TaskID", "UserID", "Task_Details", "Due_date", "Status"])
            for task in tasks:
                table.add_row(task)
                
            print(table)


        elif answer == "9. View all tags for a task":
            TaskID = input("Enter the task's ID: ")
            table = PrettyTable(["Tag Name"])
            tags = databaze.readTagsForTask(TaskID)
            for tag in tags:
                table.add_row(tag)
            
            
            print(table)


        elif answer == "10. remove a tag from a task":
            TaskID = input("Enter the task's ID: ")
            tag_id = input("Enter the tag's ID: ")
            databaze.remove_tag_from_task(TaskID, tag_id)
            print("Tag removed successfully")    


        if answer == "11. Exit":
            print("Goodbye!")
            break

        

if __name__ == '__main__':
    main()