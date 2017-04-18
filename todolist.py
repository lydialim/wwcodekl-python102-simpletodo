# WWCode Kuala Lumpur Python 102 - Simple Todo List

from todoitem import *

def add(todoList, text):
    # Adds an item to the list
    try:
        lastId = todoList[-1].id
    except IndexError:
        # No items in list
        lastId = 0

    newItem = TodoItem(lastId + 1, text)
    todoList.append(newItem)

def remove(todoList, itemId):
    # removes a todo item by id
    del todoList[itemId - 1]

def markDone(todoList, itemId):
    # mark a todo item as done
    todoList[itemId - 1].done = True

def create(name):
    # creates a new todo object
    myTodo = {'Owner' : name, 'List': []}
    return myTodo

def display(myTodo):
    # prints the todo list
    print("Hello %s!" % myTodo['Owner'])

    todoList = myTodo['List']

    # check if todo list is empty
    if not todoList:
        print("There is nothing for you to do!")
        return

    # print todo list
    for todo in todoList:
        print (todo)


def run():
    # The beginning...
    print('Who are you?')
    name = input()

    myTodo = create(name)

    add(myTodo['List'], "Buy milk")
    add(myTodo['List'], "Buy Cookies I")
    add(myTodo['List'], "Buy Cookies II")
    display(myTodo)

    remove(myTodo['List'], 3)
    markDone(myTodo['List'], 2)
    display(myTodo)

# Run the app
run()
