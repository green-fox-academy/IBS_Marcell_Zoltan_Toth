import sys
from os import path

tasks_global = []


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
    print("remove a task")

elif sys.argv[1] == "-c":
    print("completed a task")

else:
    print("case not handled so far")


