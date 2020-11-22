import sys
from os import path
import glob

tasks_global = []

# The function load_data loads the specified user's tasks into the global variable tasks_global.
def load_data(user):
    buffer2 = []
    buffer = []
    filename = user + "_database.txt"
    try:
        with open(filename, "r") as file:
            buffer = file.readlines()
    finally:
        for i in range(len(buffer)):
            buffer2.append(buffer[i].replace("\n", ""))
        return buffer2

#The function save_data saves the specified user's data into the corresponding txt file from tasks_global.
def save_data(tasks, user):
    filename = user + "_database.txt"
    with open(filename, "w") as file:
        for i in tasks:
            file.write(i + "\n")

#The function print_data prints all data from the global variable.
def print_data(tasks):
    for i in range(len(tasks)):
        print(str(i + 1) + " - " + tasks[i])

#The function print_data_unchecked prints all unchecked tasks from the global variable.
def print_data_unchecked(tasks):
    for i in range(len(tasks)):
        if tasks[i][1] == " ":
            print(str(i + 1) + " - " + tasks[i])

#The function print_usage prints the short and longhand commands.
def print_usage():
    print("Command line arguments:")
    print("\t-l  or  --List\t\tLists the unchecked tasks")
    print("\t-la or  --ListAll\tLists all the tasks")
    print("\t-a  or  --Add\t\tAdds a new task(s)")
    print("\t-r  or  --Remove\tRemoves a task(s)")
    print("\t-c  or  --Check\t\tCompletes a task(s)")
    print("\t-m  or  --Modify\tModifies a task(s)")

#The function add_new_tasks updates the global vaiable tasks_global with the new task.
def add_new_task(new_task):
    global tasks_global
    tasks_global.append("[ ] " + new_task)

#The function remove_task removes the specified index from the global variable tasks_global.
def remove_task(indexes):
    global tasks_global
    indexes.sort(reverse=True)
    for i in indexes:
        tasks_global.pop(i - 1)

#The function check_task checks the specified index in the global variable tasks_global.
def check_task(indexes):
    global tasks_global
    indexes.sort()
    for i in indexes:
        tasks_global[i - 1] = "[x" + tasks_global[i - 1][2:]

#The function modifies the specified index in the global variable tasks_global.
def modify_task(indexes):
    global tasks_global

    if len(indexes[1]) != 0:
        for i, v in indexes[1].items():
            if tasks_global[i - 1][1] == " ":
                tasks_global[i - 1] = "[ ] " + v
            else:
                tasks_global[i - 1] = "[x] " + v

    if len(indexes[0]) != 0:
        print("Error occured, unprocessed indices: ")
        print(indexes[0])

#The function argument_ok check whether the argument is in a valid range and provides case-by-case error messages.
def argument_ok(arg, case):
    if not sys.argv[2].isnumeric():
        print("Unable to " + case + ": index is not a number")
        return False
    elif len(tasks_global) < int(arg):
        print("Unable to " + case + ": index is out of bound")
        return False
    elif int(arg) == 0:
        print("0 index does not exist. Please use -la or --ListAll to see the valid indices!")
        return False
    else:
        return True

#The function sort arguments sorts the system arguments into lists.
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

#The function sort_arguments_dict sorts the arguments into a dictionary. (used only for modifying)
def sort_arguments_dict():
    temp = sys.argv[:]
    ret = {}
    grouped_arguments = {}
    good_args = {}
    bad_args = []
    last = ""
    order_ok = True

    if len(temp) % 2 == 1:
        last += sys.argv[-1]
        del temp[-1]

    for i in range(2, len(temp) - 1, 2):
        if order_ok:
            if temp[i].isnumeric():
                if int(temp[i]) == 0:
                    print("0 index does not exist. Please use -la or --ListAll to see the valid indices!")
                    bad_args.append(temp[i])
                    bad_args.append(temp[i + 1])
                else:
                    if len(tasks_global) < int(temp[i]):
                        print("Unable to replace " + temp[i] + " and " + temp[i + 1] + ": index is out of bound")
                        bad_args.append(temp[i])
                        bad_args.append(temp[i + 1])
                    else:
                        good_args[int(sys.argv[i])] = sys.argv[i + 1]
            else:
                print("Arguments are provided in wrong order! " + " OR " + temp[i] + " is not a number!")
                order_ok = False
                bad_args.append(temp[i])
                bad_args.append(temp[i + 1])
        else:
            bad_args.append(temp[i])
            bad_args.append(temp[i + 1])

    if last != "":
        bad_args.append(last)

    ret[0] = bad_args
    ret[1] = good_args
    return ret

#The function user_exists checks whether a user has a txt file created already for storing tasks.
def user_exists(name):
    databases = glob.glob("*.txt")
    users = []

    for i in databases:
        users.append(i[:(len(i) - 13)])

    for i in users:
        if name == i:
            return True

    return False


#The if-else branches below decide which functions are called based on different system arguments.
if len(sys.argv) > 1:
    user = input("Specify the user! ")

    if not user_exists(user):
        ans = input("User does not exist! Do you want to create a new user ? (y/n)")
        if ans == "n":
            sys.exit()
        elif ans == "y":
            save_data(tasks_global, user)
            print(user + " user has been created!")

if len(sys.argv) == 1:
    print_usage()

elif sys.argv[1] == "-la" or sys.argv[1] == "--ListAll":
    tasks_global = load_data(user)
    print_data(tasks_global)

elif sys.argv[1] == "-l" or sys.argv[1] == "--List":
    tasks_global = load_data(user)
    print_data_unchecked(tasks_global)

elif sys.argv[1] == "-a" or sys.argv[1] == "--Add":
    if len(sys.argv) > 2:
        tasks_global = load_data(user)
        for i in range(2, len(sys.argv)):
            add_new_task(sys.argv[i])
        save_data(tasks_global, user)
    else:
        print("Unable to add: no task provided")

elif sys.argv[1] == "-r" or sys.argv[1] == "--Remove":

    tasks_global = load_data(user)
    args_in_order = sort_arguments("remove")

    if len(args_in_order[0]) != 0:
        remove_task(args_in_order[0])
        save_data(tasks_global, user)

    if len(args_in_order[1]) != 0:
        print("The following argument(s) are invalid: " + str(args_in_order[1]))

elif sys.argv[1] == "-c" or sys.argv[1] == "--Check":

    tasks_global = load_data(user)
    args_in_order = sort_arguments("check")

    if len(args_in_order[0]) != 0:
        check_task(args_in_order[0])
        save_data(tasks_global, user)

    if len(args_in_order[1]) != 0:
        print("The following argument(s) are invalid: " + str(args_in_order[1]))

elif sys.argv[1] == "-m" or sys.argv[1] == "--Modify":

    tasks_global = load_data(user)
    if len(sys.argv) < 4:
        print("Unable to modify: no replacement value is provided")
    else:
        args_in_order = sort_arguments_dict()
        modify_task(args_in_order)
        save_data(tasks_global, user)

else:
    print("Unsupported argument")
