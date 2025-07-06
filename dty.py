# To-Do List Application using Functions and Data Structures

todo_list = []  # Global list to store tasks

def add_task(task_description):
    task = {"task": task_description, "completed": False}
    todo_list.append(task)
    print(f"✅ Task added: {task_description}")

def delete_task(index):
    if 0 <= index < len(todo_list):
        removed_task = todo_list.pop(index)
        print(f"❌ Task deleted: {removed_task['task']}")
    else:
        print("⚠️ Invalid task number.")

def display_tasks():
    if not todo_list:
        print("📭 No tasks to display.")
        return
    print("\n📝 Your To-Do List:")
    for idx, task in enumerate(todo_list):
        status = "✅" if task["completed"] else "❌"
        print(f"{idx}. [{status}] {task['task']}")
    print()

def mark_task_complete(index):
    if 0 <= index < len(todo_list):
        todo_list[index]["completed"] = True
        print(f"🎉 Task marked as complete: {todo_list[index]['task']}")
    else:
        print("⚠️ Invalid task number.")

def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Display Tasks")
        print("4. Mark Task as Complete")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter task description: ")
            add_task(task)

        elif choice == '2':
            display_tasks()
            try:
                index = int(input("Enter the task number to delete: "))
                delete_task(index)
            except ValueError:
                print("⚠️ Please enter a valid number.")

        elif choice == '3':
            display_tasks()

        elif choice == '4':
            display_tasks()
            try:
                index = int(input("Enter the task number to mark as complete: "))
                mark_task_complete(index)
            except ValueError:
                print("⚠️ Please enter a valid number.")

        elif choice == '5':
            print("👋 Exiting To-Do List. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
