import sys
from os import path

tasks_global = ["take a nap", "brush teeth"]

def load_data():
    buffer2 = []
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


tasks = load_data()
print_data(tasks)

tasks = ["read", "netflix", "chill"]
save_data(tasks)


'''


def print_usage():
    print("Command line arguments:")
    print("\t-l\tLists all the tasks")
    print("\t-a\tAdds a new task")
    print("\t-r\tRemoves a task")
    print("\t-c\tCompletes a task")

def add_new_task():
    if path.exists("database.txt"):
        print("we have a database")
    else:
        with open("database.txt", "a") as file:



if len(sys.argv) == 1:
    print_usage()
elif sys.argv[1] == "-l":
    print("list all the tasks")
elif sys.argv[1] == "-a":
    print("add a new task")
    add_new_task()
elif sys.argv[1] == "-r":
    print("remove a task")
elif sys.argv[1] == "-c":
    print("completed a task")
else:
    print("case not handled so far")


'''