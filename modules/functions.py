def get_todos(filepath = "todo.txt"):
    ''' Read a file and returns the list of
    to-do items.. this a doc-string which can be displayed using help on the named function like help(get_todos) '''
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local

def write_todos(todos,filepath = "todo.txt"):
    ''' Write the to-do items list in the text file '''
    with open(filepath, 'w') as file:
        file.writelines(todos)

print(__name__)
if __name__ ==  "__main__":

    print("Hey this is main that's why executable")