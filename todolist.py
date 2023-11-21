import os

def display_menu():
    print("\nSimple To-Do List Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_tasks():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        if tasks:
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
        else:
            print("\nNo tasks found.")

def add_task():
    task = input("\nEnter task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")

def delete_task():
    view_tasks()
    try:
        task_index = int(input("\nEnter the task number to delete: ")) - 1
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print(f"Task '{deleted_task.strip()}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid task number.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    # Check if the tasks.txt file exists, if not, create it
    if not os.path.exists("tasks.txt"):
        with open("tasks.txt", "w"):
            pass
    main()
