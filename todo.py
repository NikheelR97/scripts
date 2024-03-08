import os

def display_menu():
    print("Todo List Menu")
    print("1. View Todo List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Quit")

def load_todo_list():
    if os.path.exists("todo.txt"):
        with open("todo.txt", "r") as file:
            todo_list = [line.strip() for line in file.readlines()]
        return todo_list
    else:
        return []

def save_todo_list(todo_list):
    with open("todo.txt", "w") as file:
        for task in todo_list:
            file.write(task + "\n")

def view_todo_list(todo_list):
    if not todo_list:
        print("Todo list is empty.")
    else:
        print("Todo List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append(task)
    print("Task added successfully.")

def mark_completed(todo_list):
    view_todo_list(todo_list)
    try:
        index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= index < len(todo_list):
            completed_task = todo_list.pop(index)
            print(f"Marked '{completed_task}' as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def main():
    todo_list = load_todo_list()

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_todo_list(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            mark_completed(todo_list)
        elif choice == "4":
            save_todo_list(todo_list)
            print("Todo list saved. Exiting.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
