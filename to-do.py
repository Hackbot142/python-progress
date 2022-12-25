tasks = []

def add_task(task):
  tasks.append(task)

def complete_task(task_index):
  tasks.pop(task_index)

def list_tasks():
  for i, task in enumerate(tasks):
    print(f"{i+1}: {task}")

def main():
  while True:
    action = input("What do you want to do? [A]dd a task, [C]omplete a task, [L]ist tasks, [Q]uit: ")
    if action.lower() == "a":
      task = input("Enter a task: ")
      add_task(task)
    elif action.lower() == "c":
      task_index = int(input("Enter the task number to complete: ")) - 1
      complete_task(task_index)
    elif action.lower() == "l":
      list_tasks()
    elif action.lower() == "q":
      break

if __name__ == "__main__":
  main()