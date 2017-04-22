# WWCode Kuala Lumpur Python 102 - Simple Todo List

from todoitem import *

def add(todoList):
    # Adds an item to the list
    print("\nEnter your to-do:")
    text = input()

    if not todoList:
        lastId = 0
    else:
        try:
            lastId = todoList[-1].id
        except IndexError:
            # No items in list
            lastId = 0

    newItem = TodoItem(lastId + 1, text)
    todoList.append(newItem)

    print("\n%s is added" % newItem.text)

def remove(todoList):
    print("\nEnter a todo item Id:")
    itemId = int(input())

    # removes a todo item by id
    item = todoList[itemId - 1]
    del todoList[itemId - 1]
    print("\n%s is deleted" % item.text)

def markDone(todoList):
    print("\nEnter a todo item Id:")
    itemId = int(input())

    # mark a todo item as done
    item = todoList[itemId - 1]
    item.done = True
    print("\n%s is done" % item.text)

def create(name):
    # creates a new todo object
    myTodo = {'Owner' : name, 'List': []}
    return myTodo

def display(myTodo):
    # prints the todo list
    print("\n%s's To-Do" % myTodo['Owner'])
    todoList = myTodo['List']

    # check if todo list is empty
    if not todoList:
        print("Your to-do list is empty.")
        return

    # print todo list
    for todo in todoList:
        print (todo)

def menu(name):
    # prints the main menu
    print("\nHello %s!" % name)
    options = ("Options:\n"
               "1 - View your to-do lists\n"
               "2 - Create a to-do\n"
               "3 - Complete a to-do\n"
               "4 - Delete a to-do\n"
               "0 - Quit\n")
    choice = input(options)
    return int(choice)

def run():
    # The beginning...
    print("What is your name?")
    name = input()

    # The list
    myTodo = create(name)
    myTodoList = myTodo['List']

    while True:
        choice = menu(myTodo['Owner'])

        if choice == 1:
            display(myTodo)
        elif choice == 2:
            add(myTodoList)
        elif choice == 3:
            markDone(myTodoList)
        elif choice == 4:
            remove(myTodoList)
        elif choice == 0:
            break

# Run the app
run()
