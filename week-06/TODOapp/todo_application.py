import sys


if len(sys.argv) == 1:
    print("print usage")
elif sys.argv[1] == "-l":
    print("list all the tasks")
elif sys.argv[1] == "-a":
    print("add a new task")
elif sys.argv[1] == "-r":
    print("remove a task")
elif sys.argv[1] == "-c":
    print("completed a task")
else:
    print("case not handled so far")

