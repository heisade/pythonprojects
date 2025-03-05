# Load tasks from file
# Instructions: Create a txt file called tasks and save it on the same folder with this python script.
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

# Save tasks to file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in to_do_list:
            file.write(task + "\n")
        
# Add tasks to file
def add_to_list(x):
    to_do_list.append(x)
    save_tasks()

# Remove task from file
def remove_from_list(x):
    if 1 <= index <= len(to_do_list):
        to_do_list.pop(index-1)
        save_tasks()
    else:
        print("Invalid index!")


to_do_list = load_tasks()


user_input = input("Enter [1] to list out To Do list\n"
                   "Enter [2] to add to To Do list\n"
                   "Enter [3] to remove from To Do list\n"
                   "Enter input: ")

if user_input == '1':
    print('Your To Do list:')
    for index, task in enumerate(to_do_list, start=1):
        print(f"{index}: {task}")

elif user_input == '2':
    print('Your To Do list:')
    for index, task in enumerate(to_do_list, start=1):
        print(f"{index}: {task}")

    task = input("Enter task to be added to To Do list: ")
    add_to_list(task)
    print("Updated To Do list: ")
    for index, task in enumerate(to_do_list, start=1):
        print(f"{index}: {task}")

elif user_input == '3':
    print('Your To Do list:')
    for index, task in enumerate(to_do_list, start=1):
        print(f"{index}: {task}")
    
    try:
        remove = int(input("Enter task [index] to remove: "))
        remove_from_list(remove)
        print("Updated To Do list:")
        for index, task in enumerate(to_do_list, start=1):
            print(f"{index}: {task}")
    except ValueError:
        print("Please enter a valid number!")
        