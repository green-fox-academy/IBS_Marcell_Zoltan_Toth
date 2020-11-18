import sys
from os import path

#tasks_global = []


def load_data():
    buffer2 = []
    buffer = []
    try:
        with open("database.txt", "r") as file:
            buffer = file.readlines()
    finally:
        for i in range(len(buffer)):
            buffer2.append(buffer[i].replace("\n", ""))
        return buffer2


def save_data(tasks):
    with open("database.txt", "w") as file:
        for i in tasks:
            file.write(i + "\n")


def print_data(tasks):
    for i in range(len(tasks)):
        print(str(i+1) + " - " + tasks[i])


def print_usage():
    print("Command line arguments:")
    print("\t-l\tLists all the tasks")
    print("\t-a\tAdds a new task")
    print("\t-r\tRemoves a task")
    print("\t-c\tCompletes a task")


def add_new_task(new_task):
    global tasks_global
    tasks_global.append("[ ] " + new_task)


def remove_task(index):
    global tasks_global
    tasks_global.pop(index - 1)

def check_task(index):
    global tasks_global
    tasks_global[index - 1] = "[x" + tasks_global[index - 1][2:]






if len(sys.argv) == 1:
    print_usage()

elif sys.argv[1] == "-l":
    print("list all the tasks")

elif sys.argv[1] == "-a":
    if len(sys.argv) == 3:
        tasks_global = load_data()
        add_new_task(sys.argv[2])
        save_data(tasks_global)
    else:
        print("Unable to add: no task provided")

elif sys.argv[1] == "-r":

    tasks_global = load_data()

    if len(sys.argv) == 2:
        print("Unable to remove: no index provided")
    else:
        if sys.argv[2].isnumeric():
            if len(tasks_global) <= int(sys.argv[2]):
                print("Unable to remove: index is out of bound")
            else:
                remove_task(int(sys.argv[2]))
                save_data(tasks_global)
        else:
            print("Unable to remove: index is not a number")


elif sys.argv[1] == "-c":
    tasks_global = load_data()

    if len(sys.argv) == 2:
        print("Unable to check: no index provided")
    else:
        if sys.argv[2].isnumeric():
            if len(tasks_global) <= int(sys.argv[2]):
                print("Unable to check: index is out of bound")
            else:
                check_task(int(sys.argv[2]))
                save_data(tasks_global)
        else:
            print("Unable to check: index is not a number")

else:
    print("Unsupported argument")


