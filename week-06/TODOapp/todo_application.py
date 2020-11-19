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

def print_data_unchecked(tasks):
    for i in range(len(tasks)):
        if tasks[i][1] == " ":
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


def remove_task(indexes):
    global tasks_global
    indexes.sort(reverse=True)
    for i in indexes:
        tasks_global.pop(i - 1)


def check_task(indexes):
    global tasks_global
    indexes.sort()
    for i in indexes:
        tasks_global[i - 1] = "[x" + tasks_global[i - 1][2:]


def argument_ok(arg, case):
    if not sys.argv[2].isnumeric():
        print("Unable to " + case + ": index is not a number")
        return False
    elif len(tasks_global) < int(arg):
        print("Unable to " + case + ": index is out of bound")
        return False
    else:
        return True


def sort_arguments(case):
    ret = []
    good_args = []
    bad_args = []

    for i in sys.argv[2:]:
        if argument_ok(int(i), case):
            good_args.append(int(i))
        else:
            bad_args.append(i)

    ret.append(good_args)
    ret.append(bad_args)
    return ret



if len(sys.argv) == 1:
    print_usage()

elif sys.argv[1] == "-la" or sys.argv[1] == "-ListAll":
    tasks_global = load_data()
    print_data(tasks_global)

elif sys.argv[1] == "-l" or sys.argv[1] == "-List":
    tasks_global = load_data()
    print_data_unchecked(tasks_global)

elif sys.argv[1] == "-a" or sys.argv[1] == "-Add":
    if len(sys.argv) > 2:
        tasks_global = load_data()
        for i in range(2,len(sys.argv)):
            add_new_task(sys.argv[i])
        save_data(tasks_global)
    else:
        print("Unable to add: no task provided")

elif sys.argv[1] == "-r" or sys.argv[1] == "-Remove":

    tasks_global = load_data()
    args_in_order = sort_arguments("remove")

    if len(args_in_order[0]) != 0:
        remove_task(args_in_order[0])
        save_data(tasks_global)

    if len(args_in_order[1]) != 0:
        print("The following argument(s) are invalid: " + str(args_in_order[1]))

elif sys.argv[1] == "-c" or sys.argv[1] == "-Check":

    tasks_global = load_data()
    args_in_order = sort_arguments("check")

    if len(args_in_order[0]) != 0:
        check_task(args_in_order[0])
        save_data(tasks_global)

    if len(args_in_order[1]) != 0:
        print("The following argument(s) are invalid: " + str(args_in_order[1]))

else:
    print("Unsupported argument")


