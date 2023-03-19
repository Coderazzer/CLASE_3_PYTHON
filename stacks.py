stack1 = [1, 2, 3]
stack2 = [5, 4]
stack3 = []

def display(stack1, stack2, stack3):
    print (stack1)
    print (stack2)
    print (stack3)

display(stack1, stack2, stack3)

stack3.append(stack1.pop())
stack3.append(stack2.pop())
stack3.append(stack2.pop())
stack2.append(stack1.pop())
stack2.append(stack1.pop())
stack1.append(stack3.pop())
stack1.append(stack3.pop())
stack1.append(stack3.pop())
stack3.append(stack2.pop())
stack3.append(stack1.pop())
stack2.append(stack1.pop())
stack1.append(stack3.pop())

display(stack1, stack2, stack3)