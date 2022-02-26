class Stacks:
    def __init__(self):
        self._data=[]

    def push(self,e):
        self._data.append(e)
    def pop(self):
        if(len(self._data)>0):
            self._data.pop()
        else:
            print("No elements to Pop from stack")
    def peek(self):
        print("In Peek " + str(self._data[-1]))
    def __len__(self):
        return len(self._data)
    def top(self):
        pass
    def getStackData(self):
        return (self._data)

stack=Stacks()
print(len(stack))
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.peek()
print(stack.getStackData())
print(len(stack))
stack.pop()
print(len(stack))
print(stack.getStackData())
stack.peek()
stack.pop()
print(stack.getStackData())
stack.pop()
print(stack.getStackData())
stack.pop()
print(stack.getStackData())
stack.pop()

