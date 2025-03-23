class task_manager_app:
    def __init__(self):
        self.all_task = []

    def add_task(self, task):
        self.all_task.append({"Task": task, "Completed": False})

    def edit_tasks(self, old_task, new_task):
        for task in self.all_task:
            if task["Task"] == old_task:
                task["Task"] = new_task
                print(f"Task {old_task} updated to {new_task}")
                return
        print("Task not found!")

    def delete_tasks(self, del_task):
        for task in self.all_task:
            if task["Task"] == del_task:
                self.all_task.remove(task)
                print(f"Task: {del_task} has been removed.")
                return
        print("Task not available!")


    def completed_tasks(self, completed_task):
        for task in self.all_task:
            if task["Task"] == completed_task:
                task["Completed"] = True
                print(f"Task: {completed_task} has been completed. ✅")
                return
        print("Task not available!")

    def filter_pending_task(self):
        pending = [task["Task"] for task in self.all_task if not task["Completed"]]
        if pending:
            print(f"Pending Tasks: {pending}")
        else:
            print("No pending tasks!")

    def filter_completed_task(self):
        completed = [task["Task"] for task in self.all_task if task["Completed"]]
        if completed:
            print(f"Completed Tasks: {completed}")
        else:
            print("No Completed Task")
