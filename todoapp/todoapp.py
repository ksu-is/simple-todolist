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