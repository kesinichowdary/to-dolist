class Task:
    def __init__(self, description, priority="Medium"):
        self.description = description
        self.status = "Incomplete"
        self.priority = priority

    def mark_complete(self):
        self.status = "Complete"

    def __str__(self):
        return f"[{self.status}] {self.description} (Priority: {self.priority})"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority="Medium"):
        task = Task(description, priority)
        self.tasks.append(task)
        print(f"Task '{description}' added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty!")
        else:
            print("\nYour To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def update_task_status(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1].mark_complete()
            print(f"Task {task_number} marked as complete!")
        else:
            print("Invalid task number!")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task.description}' deleted successfully!")
        else:
            print("Invalid task number!")


def main():
    to_do_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            description = input("Enter the task description: ")
            priority = input("Enter the task priority (Low, Medium, High): ")
            to_do_list.add_task(description, priority)

        elif choice == "2":
            to_do_list.view_tasks()

        elif choice == "3":
            task_number = int(input("Enter the task number to mark as complete: "))
            to_do_list.update_task_status(task_number)

        elif choice == "4":
            task_number = int(input("Enter the task number to delete: "))
            to_do_list.delete_task(task_number)

        elif choice == "5":
            print("Exiting To-Do List application. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option.")


if __name__ == "__main__":
    main()
