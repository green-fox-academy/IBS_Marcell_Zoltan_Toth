# TODO application

This is a simple to do application where you can keep track of all the tasks and their status.


## Developement environtment

The application was developed in python 3.9 with the following modules used:
    
    - sys
    - glob
    - os
    
## Necessary dependencies

No external libraries used. The application is only dependent on the python version (has to be 3.0 or greater.)


## Description of usage and features

The application is to be run from the command line. 
To execute the program navigate to the containing folder in your computer and type *python todo_application.py* 
Then you can choose between the following arguments to achieve the desired behaviour:

    1. No argument ("python todo_application.py")
       In case of no argument the program lists all the possible long- and shorthand commands.
    
    2. -la or --ListAll ("python todo_application.py -la" or "python todo_application.py --ListAll")
       This command lists all the tasks added to the list (both checked and unchecked). If the list is empty nothing is listed.
       
    3. -l or --List ("python todo_application.py -l" or "python todo_application.py --List")
       This command lists only the unchected elements. If the list is empty nothing is listed.
       
    4. -a or --Add ("python todo_application.py -a" or "python todo_application.py --Add")
       This command adds one or multiple elements to the list. The specidfic element has to be provided after the "-a" command 
       separated with a space. If multiple elements are to be added, type them continuously with space separation after "-a"
       
    5. -r or --Remove ("python todo_application.py -r" or "python todo_application.py --Remove")
       This command removes one or more elements with the specified index in the list. The index of each element is visible by the 
       "-la" command. To remove elements type the index space separated after the "-r" command. Attention: The list is re-indexed after elements are removed.
       
    6. -c or --Check ("python todo_application.py -c" or "python todo_application.py --Check")
       This command marks one or more elements (check) as done in the list. To check elements proide the indices after the "-c" command.
       The index of each element is visible by the "-la" command. 
       
    7. -m or --Modify ("python todo_application.py -m" or "python todo_application.py --Modify")
       This command modifies one or more elements in the list. To modify elements in the list, first provide the index, then the value you want to modify to
       after the command "-m". The index of each element is visible by the "-la" command.
       
       
The program supports multiple users. Therefore after each command, it has to be specified which user do we want to apply the changes for.
If the user is new (no *.txt file with such prefix) a new .txt file is created to store the individual list. 
## Edge cases and error handling

The following edge cases were considered, tested and handled in the code: 

    1. Provided index for the command 0 --> Error message: "0 index does not exist. Please use -la or --ListAll to see the valid indices!"
    2. Provided index for the command out of range --> Error message: "Unable to " + case + ": index is out of bound"
    3. Provided index for the command not a number --> "Unable to " + case + ": index is not a number"
    4. In case of multiple arguments all the valid arguments are processed, and the invalid arguments are listed with the appropriate error message.
    5. In case of wrong argument order (-m) the unprocessed indices are listed with an error message. Up until the error in order the indices are processed.
    6. In case there is no .txt file with the specified username, the user is asked wheteher a new txt file should be created.

