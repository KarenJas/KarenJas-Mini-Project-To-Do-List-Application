#blank dictionarry that will hold users task,description, and status
task_dict = {}
# statuse is set to "incomplete" as default
status = "Incomplete"

#set up interface function
def interface():
    print("\nmenue:")
    print("1. Add a task\n2. View tasks\n3. Mark a task complete\n4. Delete a task\n5. Quit ")

#set up 'Add a task' function
def add_a_task():
    print("\n")
    #asking user for task name and storing it in variable
    title = input("Task: ")
    #asking user for task description and storing it in variable
    task_decription = input("Description: ")
    #adds users title, task, and status to dictionary
    task_dict[title] = [task_decription,status]

#set up 'View tasks' function
def view_tasks():
    print("\nList:\n")
    #print all the tasks, task descriptions, and status inside 'task_dict'
    for key, value in task_dict.items():      
        print(f"Task: {key} \nDescription: {value[0]} \nStatus: {value[1]}\n")

#set up 'Mark a task complete' function
def mark_task_complete():
    print('\nList:\n')
    #print all the tasks, task descriptions, and status inside 'task_dict' so user can see the option
    for key, value in task_dict.items():
        print(f"Task: {key} \nDescription: {value[0]} \nStatus: {value[1]}\n")
    #ask user for tittle of task and store inside variable 
    mark_complete = input("which would you like to mark complete (task name): ")
    #if user inputs anything other than string they will get an error message 
    #user will then be prompted to try again or go back 
    try:
        task_dict[mark_complete][1] = "Complete"
        print('\nNew List:\n')
        for key, value in task_dict.items():
            print(f"Task: {key} \nDescription: {value[0]} \nStatus: {value[1]}\n")
    except KeyError:
        print('\nchoice is not available try again\n')

#set up 'Delete a task' function 
def delete_task():
    print('\nlist:\n')
    #print all the tasks, task descriptions, and status inside 'task_dict' so user can see the option
    for key, value in task_dict.items():
        print(f"Task: {key} \nDescription: {value[0]} \nStatus: {value[1]}\n")
    #ask user for tittle of task and store inside variable 
    delete_choice = input("Which would you like to delete (task name): ") 
    #if user inputs anything other than string they will get an error message 
    #user will then be prompted to try again or go back 
    try:
        del task_dict[delete_choice]    #use 'delete_choice' variable to delete task from 'task_dict' 
        print('\nNew List:\n')
        for key, value in task_dict.items():
            print(f"Task: {key} \nDescription: {value[0]} \nStatus: {value[1]}\n")
    except KeyError:
        print('\nchoice is not available try again\n')
   

#set up finial app function 
def app():
    #one time welcome message for when user first uses app 
    print("Welcome to the To-Do List App!\n")
    #While loop to allow user to come back to interface while using the same 'choice'
    while True:
        #calling interface function 
        interface()
        #store users choice in a variable 
        user_choice = input("choice: ")
        print("\n```")
        #while loop to allow user to go back to the menue 
        while True:
            #use if statements to trigger function calls
            #update 'user_choice' varible to allow user to repeat an action or go back to menue 
            if user_choice == "Add a task":
                add_a_task()
                user_choice = input("\nTo add another task enter 'Add a task'.\nTo go back enter 'b'\nChoice: ")
                print("\n```")
            elif user_choice == "View tasks":
                view_tasks()
                user_choice = input("To go back enter 'b'\nChoice: ")
                print("\n```")
            elif user_choice == "Mark a task complete":
                mark_task_complete()
                user_choice = input("To mark another task complete enter 'Mark a task complete' To go back enter 'b'\nChoice: ")
                print("\n```")
            elif user_choice == "Delete a task":
                delete_task()
                user_choice = input("To delete another task enter 'Delete a task' To go back enter 'b'\nChoice: ")
                print("\n```")
            elif user_choice == "Quit":
                break
            #break first loop to go back to menue 
            elif user_choice == 'b':
                break
            else:
                print('\nchoice is not available try again\n')
                print("```")
                break
        #break both loops when 'user_choice' is == 'Quit'
        if user_choice == "Quit":
            break   

#call 'app' function                
app()