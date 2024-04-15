'''
# Creating user inteface 
def interface():
    print("Welcome to the To-Do List App!\n")
    print("menue:")
    print("1. Add a task\n2. View tasks\n3. Mark a task as complete\n4. Delete a task\n5. Quit ")
#interface()   
# crating a function instead of variable in order to display multiple times
# varible would have to be changed and cleared each time you use it 
# functions allow you to continue to use a blank input statement withouht the need to clear a variable
def user_choice():
    return input("Select an option: ")
    

# statuse is set to "incomplete" as default
status = "Incomplete"
task_dict = {}

# add to list function 
def adding_to_list():
    while True :
        #navigate to option 1 and back
        if user_choice() == "Add a task":
            print("\n")
            title= input("Title: ")
            new_task = input("Task: ")
            # adds users title, task, and status to dictionary
            task_dict[title] = [new_task,status]
            #option for user to continue to add another task or go back to main menue
            print("lets add some more tasks!\nType 'Add a task' to add a new task or b to go back to the menue: ")
            if user_choice () == 'b':
                interface()
            
#adding_to_list()

# view task function
def view_task():
    if user_choice() == "View tasks":
        for key, value in task_dict.items():
            print(f"{key}: {value[0]}/ {value[1]}")

prints dictionary
#for key, value in task_dict.items():
# print(f"{key}: {value[0]}/ {value[1]}")


def to_do_list_app():
    interface()
    adding_to_list()
    view_task()

to_do_list_app()
'''


# statuse is set to "incomplete" as default
status = "Incomplete"
#blank dictionarry
task_dict = {'FIRST': [1,status],'SECOND': [2,status], 'THIRD': [3,status]}

#set up interface function
def interface():
    #print("Welcome to the To-Do List App!\n")# POSSIBLY PRINT ONCE AT START AND TAKE OUT OF FUNCTION 
    print("\nmenue:")
    print("1. Add a task\n2. View tasks\n3. Mark a task as complete\n4. Delete a task\n5. Quit ")

#set up 'Add a task' function
def add_a_task(choice):
    if choice == 'Add a task':
        print("\n")
        title= input("Title: ")
        new_task = input("Task: ")
        # adds users title, task, and status to dictionary
        task_dict[title] = [new_task,status]
       

'''
def app():
    #one time welcome message for when user first uses app 
    print("Welcome to the To-Do List App!\n")
    #While loop to allow user to come back to interface while using the same 'choice'
    while True:
        #calling interface function 
        interface()
        choice = input("choice: ")
        while True:
            if choice == 'Add a task':
                print("\n")
                title= input("Title: ")
                new_task = input("Task: ")
                # adds users title, task, and status to dictionary
                task_dict[title] = [new_task,status]
                choice = input("To add another task enter 'Add a task'.\nTo go back enter 'b'\nChoice: ")
                if choice == 'b':
                    break
                else:
                    print('\nchoice is not available try again\n')
                    break
            elif choice == 'View tasks':
                print("\nList:\n")
                for key, value in task_dict.items():
                    print(f"{key}: {value[0]} / {value[1]}")
                choice = input("\nTo go back enter 'b'\nChoice: ")
                if choice == 'b':
                    break
                else:
                    print('\nchoice is not available try again\n')
                    break
            elif choice == 'Mark a task as complete':
                print('\nlist:\n')
                for key, value in task_dict.items():
                    print(f"{key}: {value[0]} / {value[1]}")
                mark_complete = input("which would you like to mark complete (title): ")
                try:
                    task_dict[mark_complete][1] = "Complete"
                except KeyError:
                    print('\nchoice is not available try again\n')
                    break
                print(task_dict)#test
                try:
                    choice = input("To go back enter 'b' Choice: ")
                except KeyError:
                    print('\nchoice is not available try again\n')
                    break
                if choice == 'b':
                    break
                else:
                    print('\nchoice is not available try again\n')
                    break
            elif choice == 'Delete a task':
                print('\nlist:')
                for key, value in task_dict.items():
                    print(f"{key}: {value[0]}/ {value[1]}")
                delete_choice = input("Which would you like to delete (tittle): ")
                try:
                    del task_dict[delete_choice]
                except KeyError:
                    print('\nchoice is not available try again\n')
                    break
                print(task_dict) #test
                choice = input("\nTo go back enter 'b'\nChoice: ")
                if choice == 'b':
                    break
                else:
                    print('\nchoice is not available try again\n')
                    break
            elif choice == 'Quit':
                break
        if choice == 'Quit':
            break

app()
'''

def app():
    #one time welcome message for when user first uses app 
    print("Welcome to the To-Do List App!\n")
    #While loop to allow user to come back to interface while using the same 'choice'
    while True:
        #calling interface function 
        interface()
        user_choice = input("choice: ")
        while True:
            add_a_task(user_choice)
            user_choice = input("To add another task enter 'Add a task'.\nTo go back enter 'b'\nChoice: ")
            while True:
                if user_choice == 'Add a task':
                    break
            if user_choice == 'b':
                    break
            else:
                print('\nchoice is not available try again\n')
                break

app()