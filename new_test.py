# statuse is set to "incomplete" as default
status = "Incomplete"
#blank dictionarry
#'FIRST': [1,status],'SECOND': [2,status], 'THIRD': [3,status]
task_dict = {}

#set up interface function
def interface():
    #print("Welcome to the To-Do List App!\n")# POSSIBLY PRINT ONCE AT START AND TAKE OUT OF FUNCTION 
    print("\nmenue:")
    print("1. Add a task\n2. View tasks\n3. Mark a task as complete\n4. Delete a task\n5. Quit ")

def app():
    #one time welcome message for when user first uses app 
    print("\nWelcome to the To-Do List App!")
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
                
            elif choice == 'View tasks':
                print("\nList:\n")
                for key, value in task_dict.items():
                    print(f"{key}: {value[0]} / {value[1]}")
                choice = input("\nTo go back enter 'b'\nChoice: ")
                
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
                
            elif choice == 'Quit':
                break
            elif choice == 'b':
                break
            else:
                print('\nchoice is not available try again\n')
                break
        if choice == 'Quit':
            break

app()
