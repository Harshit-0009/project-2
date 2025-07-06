import os
import json

TASK_FILE = "tasks.txt"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    if not tasks:
        print("📭 No tasks available.")
        return
    print("\n📋 Your Tasks:")
    for idx, task in enumerate(tasks, 1):
        status = "✅" if task['completed'] else "❌"
        print(f"{idx}. {task['title']} [{status}]")

def add_task(tasks):
    title = input("Enter task description: ").strip()
    if title:
        tasks.append({'title': title, 'completed': False})
        print("✅ Task added successfully!")
    else:
        print("⚠️ Task description cannot be empty.")

def mark_task_complete(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter the task number to mark as complete: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]['completed'] = True
            print("✅ Task marked as complete.")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter the task number to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"🗑️ Deleted task: {removed['title']}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n📌 To-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("👋 Goodbye! Tasks saved successfully.")
            break
        else:
            print("⚠️ Invalid choice. Please select between 1-5.")

if __name__ == "__main__":
    main()
