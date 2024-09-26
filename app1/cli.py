# from functions import get_todos,write_todos
from modules import functions #module folder contains the functions file..

import time

now = time.strftime("%b %d, %Y ,%H : %M : %S")

print("It is ", now)

while True :
    user_action = input("Type add  or show or edit or complete or exit : ")
    user_action = user_action.strip()

    # if 'add'  in user_action or 'new'  in user_action :   we are not usin this because if user enters as input edit add a new no than it will run add function and string 'edit add a new no' from 4th index will get printed that is add a new no


    if user_action.startswith("add"):


        todo = user_action[4:]

        todos = functions.get_todos()  #function call

        todos.append(todo + '\n')

        functions.write_todos(todos)



    # elif  'show' in user_action  :
    elif user_action.startswith("show"):

        todos = functions.get_todos()

        print(todos)

        for index,item in enumerate(todos):

            item = item.strip('\n')

            print(f"{index+1}->  {item}")

    # elif 'edit' in user_action:
    elif user_action.startswith("edit"):
        try:

            n = int(user_action[5:])
            num = n - 1

            todos = functions.get_todos()

            newTodo = input("Enter a new to-do to be added : ")
            todos[num] = newTodo +'\n'
            print(todos)

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid...")
            continue


    # elif 'complete' in user_action:
    elif user_action.startswith("complete"):
        try:
            n = int(user_action[9:])  #7 for word complete and 8th for space so list slicing done and from 9th index will get our o/p

            todos = functions.get_todos("todo.txt")
            index = n - 1
            todo_removed = todos[index].strip('\n')
            todos.pop(n-1)

            functions.write_todos(todos)

            message = f'Todo list item removed is as follows guys : {todo_removed}'
            print(message)
        except IndexError:
            print("There is no item with this no..")
        continue



    elif user_action.startswith("exit"):
        break
    else :
        print("Command is not Valid...")



print('Bye!!')


# note : syntax error can't be caught from the try catch block because only catches the logical error/exceptions



