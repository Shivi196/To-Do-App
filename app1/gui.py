
from modules import functions


import FreeSimpleGUI as sg  #This is third party library/moduless

label = sg.Text("Type in a To-do")
input_box =  sg.InputText(tooltip="Enter the to-do",key= "todo")
add_button = sg.Button("Add")

window = sg.Window("My To- Do App ", layout= [[label],[input_box],[add_button]], font=("Helvetica",20))

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
        case sg.WINDOW_CLOSED:  #this is for closing X button will not throw error and break the loop once user click on cross in gui
            break








window.close()
