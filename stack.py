size = 5
stack = [0]* size
top = -1

def push():
    global top
    if top == size - 1:
        print("stack overflow")
    else:
        value = int(input("Enter value: "))
        top = top + 1
        stack[top] = value
        print("element inserted")

def pop():
    global top
    if top == -1:
        print("stack underflow")
    else:
        value = stack[top]
        top = top -1 
        print("element deleted",value)

def peek():
    if top == -1:
        print("stack is empty")
    else:
        print("top element: ",stack[top])

def display():
    if top == -1:
        print("stack is empty")
    else:
        print("stack elements: ")
        i = top
        while i>= 0:
            print(stack[i])
            i = i - 1
while True:
    print("\n1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Display")
    print("5.Exit")

    choice = int(input("enter a choice: "))
    if choice == 1:
        pop()
    elif choice == 2:
        push()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    elif choice == 5:
        break
    else:
        print("invalid choice")