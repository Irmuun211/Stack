# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside Push() and Pop() - move TopOfStack yourself.

# Exercise 1
Stack = []
TopOfStack = -1
for x in range(10):
    Stack.append(-1)


def IsEmpty():
    global TopOfStack
    return TopOfStack == -1


def IsFull():
    global TopOfStack
    return TopOfStack == 9


# Exercise 2
def Push(Item):
    global Stack, TopOfStack
    if IsFull():
        return False
    TopOfStack +=  1
    Stack[TopOfStack] =Item
    return True


# Exercise 3
def Pop():
    global Stack, TopOfStack
    if IsEmpty():
        return -1
    x = Stack[TopOfStack]
    TopOfStack -= 1
    return x


# Exercise 4
def Peek():
    global Stack, TopOfStack
    if IsEmpty():
        return -1
    return Stack[TopOfStack]


def Size():
    return TopOfStack + 1


# Exercise 5

def ReverseWord(Word):
    Stack = []
    TopOfStack = -1
    for x in range(10):
        Stack.append(-1)
    for i in Word:
        TopOfStack += 1
        Stack[TopOfStack] = i
    s = ""
    while TopOfStack != -1:
        s = s + str(Stack[TopOfStack])
        TopOfStack -= 1
    return s

