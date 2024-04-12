# Creating user inteface 
print("Welcome to the To-Do List App!\n")
print("menue:")
print("1. Add a task\n2. View tasks\n3. Mark a task as complete\n4. Delete a task\n5. Quit ")
# variables
navigate_to = input("Select a number: ")
status = "Incomplete"

def adding_to_list():
    if navigate_to == "1":
        add_choice = input("lets add some tasks!\nType n to add a new task or b to go back to the menue: ")
        if add_choice =="n":
            task_dict = {}
            title= input("Title: ")
            new_task = input("Task: ")
            task_dict[title] = [new_task,status]
            #for key, value in task_dict.items():
               # print(f"{key}: {value[0]}/ {value[1]}")
            


adding_to_list()


task = {

}

