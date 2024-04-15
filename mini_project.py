# statuse is set to "incomplete" as default
status = "Incomplete"
#blank dictionarry
task_dict = {'FIRST': [1,status],'SECOND': [2,status], 'THIRD': [3,status]}

#set up interface function
def interface():
    print("\nmenue:")
    print("1. Add a task\n2. View tasks\n3. Mark a task complete\n4. Delete a task\n5. Quit ")


#set up 'Add a task' function
def add_a_task():
    print("\n")
    title = input("Task: ")
    task_decription = input("Description: ")
    # adds users title, task, and status to dictionary
    task_dict[title] = [task_decription,status]

def view_tasks():
    print("\nList:\n")
    for key, value in task_dict.items():      
        print(f"Task: {key} \nDescription: {value[0]} \nStatus: {value[1]}\n")

def mark_task_complete():
    print('\nList:\n')
    for key, value in task_dict.items():
        print(f"Task: {key} \nDescription: {value[0]} \nStatus: {value[1]}\n")
    mark_complete = input("which would you like to mark complete (task name): ")
    try:
        task_dict[mark_complete][1] = "Complete"
        print('\nNew List:\n')
        for key, value in task_dict.items():
            print(f"Task: {key} \nDescription: {value[0]} \nStatus: {value[1]}\n")
    except KeyError:
        print('\nchoice is not available try again\n')


def delete_task():
    print('\nlist:\n')
    for key, value in task_dict.items():
        print(f"Task: {key} \nDescription: {value[0]} \nStatus: {value[1]}\n")
    delete_choice = input("Which would you like to delete (task name): ")
    try:
        del task_dict[delete_choice]
        print('\nNew List:\n')
        for key, value in task_dict.items():
            print(f"Task: {key} \nDescription: {value[0]} \nStatus: {value[1]}\n")
    except KeyError:
        print('\nchoice is not available try again\n')
   


def app():
    #one time welcome message for when user first uses app 
    print("Welcome to the To-Do List App!\n")
    #While loop to allow user to come back to interface while using the same 'choice'
    while True:
        #calling interface function 
        interface()
        user_choice = input("choice: ")
        print("\n```")
        while True:
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
            elif user_choice == 'b':
                break
            else:
                print('\nchoice is not available try again\n')
                print(",,,")
                break
        if user_choice == "Quit":
            break    
               
app()