tasks = []

def show_menu():
    """Display the menu options"""
    print("\n===== TO-DO LIST =====")
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Mark task as complete")
    print("4. Delete a task")
    print("5. Exit")
    print("=====================")
      
def view_tasks():
    """Display all tasks from the list"""
    if not tasks:
        print("No tasks found!")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        status = task["status"]
        title = task["title"]
        if status == "complete":
            print(f"{i}. [x] {title}")
        else:
            print(f"{i}. [  ] {title}")


def add_task():
    """Add a new task to the list"""
    title = input("Enter new task: ")

    if title:
        task = {
            "title": title,
            "status": "incomplete"
        }
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty!")

def mark_complete():
    """Mark a task as complete"""
    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("\nEnter task number to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            task = tasks[task_number - 1]
            if task["status"] == "complete":
                print("Task is already marked as complete!")
            else:
                task["status"] = "complete"
                print("Task marked as complete!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task():
    """Delete a task from the list"""
    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("\nEnter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"Task deleted: {deleted_task['title']}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    """Main program function"""
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Thank you for using the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
