
from modules import functions


import FreeSimpleGUI as sg  #This is third party library/moduless

label = sg.Text("Type in a To-do")
input_box =  sg.InputText(tooltip="Enter the to-do",key= "todo") #key here is like indexes earlier window.read() function returns { 0 : hi } but giving key it returns like { todo : hi / any input given by user
add_button = sg.Button("Add")
list_box = sg.Listbox(functions.get_todos(), key = "todos" , enable_events= True, size= [45,10])
edit_button = sg.Button("Edit")


window = sg.Window("My To- Do App ", layout= [[label],[input_box,add_button],[list_box,edit_button]], font=("Helvetica",20))

while True :
    event, values = window.read()
    print(event)
    print(values)
    match event :
        case "Add":
            todos  = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values = todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos= functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values = todos)
        case "todos":
            window['todo'].update(value = values['todos'][0])



        case sg.WINDOW_CLOSED:  #this is for closing X button will not throw error and break the loop once user click on cross in gui
            break









window.close()
