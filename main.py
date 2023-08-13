def load_tasks():
    tasks = {}
    try:
        with open('tasks.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                task_name = parts[1]
                completed = parts[0] == '1'
                tasks[task_name] = completed
    except FileNotFoundError:
        pass
    return tasks

def save_tasks(tasks):
    with open('tasks.txt', 'w') as file:
        for task_name, completed in tasks.items():
            file.write(f"{int(completed)},{task_name}\n")

def add_task(tasks, task_name):
    tasks[task_name] = False
    save_tasks(tasks)
    print(f"Task '{task_name}' added.")

def view_tasks(tasks):
    print("Tasks:")
    for index, (task, completed) in enumerate(tasks.items(), start=1):
        status = "Completed" if completed else "Not Completed"
        print(f"{index}. {task} - {status}")

def mark_completed(tasks, task_number):
    if 1 <= task_number <= len(tasks):
        task_name = list(tasks.keys())[task_number - 1]
        tasks[task_name] = True
        save_tasks(tasks)
        print(f"Task '{task_name}' marked as completed.")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n------Task Manager------")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Quit")
        print("--------by ABHI--------")
        
        choice = input("Select an option: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            add_task(tasks, task_name)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            view_tasks(tasks)
            task_number = int(input("Enter task number to mark as completed: "))
            mark_completed(tasks, task_number)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
