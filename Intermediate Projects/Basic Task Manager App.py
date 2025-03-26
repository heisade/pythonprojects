class Task_Manager:
    print("📜 Task Manager App")

    def __init__(self):
        self.tasks_list = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks_list = []
                for line in file.readlines():
                    task_info = line.strip().split(" | ")
                    if len(task_info) == 2:
                        self.tasks_list.append({"Task": task_info[0], "Completed": task_info[1] == "True"})
        except FileNotFoundError:
            with open("task.txt", "w") as file:
                pass
            self.tasks_list = []
    
    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks_list:
                file.write(f"{task['Task']} | {task['Completed']}\n")

    def Add_task(self, task):
        self.tasks_list.append({"Task": task, "Completed": False})
        print("-" * 60)
        print(f"📃 Task:'{task}' successfully added to Task List")
        self.save_tasks()
        
    
    def mark_task(self, completed):
        for task in self.tasks_list:
            if task["Task"] == completed:
                task["Completed"] = True
                print("-" * 60)
                print(f"✅ Task: '{task["Task"]}' has been marked as completed.")
                self.save_tasks()
                return
        print("❌ Task not found.")

    def view_tasks(self):
        if not self.tasks_list:
            print("No tasks available.")
            return
        
        print("\n📃**Task List: **\n")
        for index, task in enumerate(self.tasks_list, 1):
            status = "✅" if task["Completed"] else "❌"
            print(f"{index}. {task["Task"]} | {status}")
        print("-" * 60)

    def delete_task(self, delete):
        for task in self.tasks_list:
            if task["Task"] == delete:
                self.tasks_list.remove(task)
                print(f"🗑️  Task: {delete} has successfully been removed.")
                self.save_tasks()
                return
        print("-" * 60)
        print("❌ Task not found in Task list.")



taskmanager = Task_Manager()

print("\n1. To view Tasks.\n"
      "2. To add Task.\n"
      "3. To mark Task.\n"
      "4. To Delete Task.\n"
      "5. To End.")

user_input = input("Enter your choice (1-5): ").strip()
if user_input == "1":
    taskmanager.view_tasks()
elif user_input == "2":
    add_task_input = input("Enter task you want to add: ").strip()
    if add_task_input:
        taskmanager.Add_task(add_task_input)
    else:
        print("❌ Task cannot be empty.")
elif user_input == "3":
    mark_task_input = input("Enter task you want to mark: ").strip()
    if mark_task_input:
        taskmanager.mark_task(mark_task_input)
    else:
        print("❌ Task cannot be empty.")
elif user_input == "4":
    delete_task_input = input("Enter task you want to delete: ").strip()
    if delete_task_input:
        taskmanager.delete_task(delete_task_input)
    else:
        print("❌ Task cannot be empty.")
elif user_input == "5":
    print("Exiting the Program.")
    quit
else:
    print("❌ Invalid Input. Please enter a number between 1 and 5.")
