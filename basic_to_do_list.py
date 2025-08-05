# basic to do list app in Python

# import the necessary modules
# Step 1: Empty list to store tasks
tasks = []

# Step 2: Function to show menu options
def show_menu():
    print("\n📋 To-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

# Step 3: Function to add task
def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print(f"✅ '{task}' added to the list.")

# Step 4: Function to show all tasks
def show_tasks():
    if len(tasks) == 0:
        print("📭 No tasks found.")
    else:
        print("\n📄 Your Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Step 5: Function to delete task
def delete_task():
    show_tasks()
    if len(tasks) > 0:
        try:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"❌ '{removed_task}' removed from the list.")
            else:
                print("⚠️ Invalid task number.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

# Step 6: Main Loop - Keeps running until user exits
while True:
    show_menu()
    choice = input("Choose option (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("👋 Exiting To-Do List App. Goodbye!")
        break
    else:
        print("⚠️ Invalid choice. Please enter 1-4.")
