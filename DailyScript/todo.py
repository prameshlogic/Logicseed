import json
import os

# File to store tasks
TASKS_FILE = 'tasks.txt'

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

# Add a new task
def add_task(tasks):
    task_id = str(len(tasks) + 1)
    description = input("Enter task description: ")
    priority = input("Enter task priority (high, medium, low): ")
    tasks[task_id] = {'description': description, 'completed': False, 'priority': priority}
    print(f"Task {task_id} added.")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTasks:")
        for task_id, task in tasks.items():
            status = 'Completed' if task['completed'] else 'Pending'
            print(f"ID: {task_id}, Description: {task['description']}, Status: {status}, Priority: {task['priority']}")
    print("")

# Mark a task as completed
def mark_task_completed(tasks):
    task_id = input("Enter task ID to mark as completed: ")
    if task_id in tasks:
        tasks[task_id]['completed'] = True
        print(f"Task {task_id} marked as completed.")
    else:
        print("Invalid task ID.")

# Delete a task
def delete_task(tasks):
    task_id = input("Enter task ID to delete: ")
    if task_id in tasks:
        del tasks[task_id]
        print(f"Task {task_id} deleted.")
    else:
        print("Invalid task ID.")

# Edit a task
def edit_task(tasks):
    task_id = input("Enter task ID to edit: ")
    if task_id in tasks:
        new_description = input("Enter new task description: ")
        tasks[task_id]['description'] = new_description
        print(f"Task {task_id} updated.")
    else:
        print("Invalid task ID.")

# Main function to run the to-do list application
def main():
    tasks = load_tasks()
    
    while True:
        print("\nMenu:")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Edit a task")
        print("6. Save and Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            edit_task(tasks)
        elif choice == '6':
            save_tasks(tasks)
            print("Tasks saved. Exiting.")
            break
        else:
            print("Invalid option. Please choose a valid option.")
            
if __name__ == "__main__":
    main()
