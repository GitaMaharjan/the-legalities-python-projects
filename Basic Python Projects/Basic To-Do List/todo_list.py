# 4.  Basic To-Do List   
#    *Description*: Develop a simple command-line to-do list application.  
#    *Skills*: Lists, loops, file handling.



def add_task(tasks):
    task = input("Enter the new task: \n")
    tasks.append(task)
    print(f"'{task}' has been added to your to-do list.")

def display_task(tasks):
    if tasks:
        print("Here is your todo list")
        for index, task in enumerate(tasks,1):
            print(f"{index}. {task}")
    else:
        print("Your to do list is empty.")

def delete_task(tasks):
    if tasks:
        display_task(tasks)
        
        try:
            delete_task_number=int(input("\nEnter the task number you want to delete: \n"))
            if(1<=delete_task_number<=len(tasks)):
                delete_task=tasks.pop(delete_task_number-1)
                print(f"'{delete_task}' has been removed from your to-do list.")
            else:
                print("Invalid task number")
        except ValueError:
            print("Enter a valid task number")

    else:
        print("There is no task to delete")

def save_task_to_file(tasks):
    with open("todo_list.txt",'w') as file:
        for task in tasks:
            file.write(task + "\n")  

def load_taskfile(filename="todo_list.txt"):
    try:
        with open(filename, 'r') as file:
                tasks = [line.strip() for line in file]
                print("Your todolist is loaded successfully:\n")
                print(tasks)
                return tasks
    except FileNotFoundError:
        print("The file with that name doesnt exists.")
        return []

def todo_list():
    tasks = load_taskfile()

    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Save tasks")
        print("5. Load tasks")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            display_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            save_task_to_file(tasks)
        elif choice == '5':
            tasks = load_taskfile()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")




todo_list()