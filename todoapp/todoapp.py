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