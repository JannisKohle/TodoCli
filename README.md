# TodoCli:

TodoCli is a Todo App for the terminal which supports nested lists and tasks. Lists can
contain tasks and more lists.

## Installation:

1. Make sure you have Python 3 installed on your system.
2. Clone this Repo (temporarily)
3. Run the install shell script for your OS, which will create a ```~/bin``` directory and put
an executable version of the program there. 
4. Add the lines ```PATH="~/bin:${PATH}"``` and ```export PATH``` to your ```.bashrc``` or ```.bash_profile``` ...
5. Now you can delete this cloned Repository, and after restarting your terminal,
you should be able to use the command ```todocli```

## Usage / Examples:

### Lists:

- Create new list (works just like mkdir): ```todocli list create School/Maths```
- Delete a list and its tasks: ```todocli list delete School/Maths```
- Rename a list: ```todocli list rename School/Maths School/Mathematics```
- List all lists in e.g. ```School```: ```todocli list list School```

### Tasks:

- Create new task: ```todocli task create School/Maths``` (Now enter title and description)
- Delete a task: ```todocli task delete School/Maths``` (Now enter title)
- Edit a task: ```todocli task edit School/Maths {-t / --title / -d / --description / -td}``` (Now enter old & new title/description)
- List all tasks in e.g. ```School/Maths```: ```todocli task list School/Maths```
