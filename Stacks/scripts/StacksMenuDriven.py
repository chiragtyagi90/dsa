class Stack:
    def __init__(self):
        print("Implementing Stack!!!")
        self.data=[]
        self.maxLength=0
        self.top=-1
    def getStackSize(self):
        print(f"""Stack Length is {len(self.data)}""")
        return (len(self.data)>0)

    def isStackEmpty(self):
        if(not self.getStackSize()):
            return True

    def push(self):

            self.data.append(int(input(f"""Enter element to perform push operation!!!""")))
            self.top=self.top=1

    def pop(self):
        if(self.isStackEmpty()):
            print("Stack Underflow!")
        else:
            self.data.pop()
            self.top = self.top - 1

    def peek(self):
        print(self.data[-1])
    def getStackData(self):
        print(self.data)

s=Stack()
myStackDict={"1":s.getStackSize,"2":s.push,"3":s.pop,"4":s.peek,"5":s.getStackData}
while(True):
    print(f"""Menu Driven Stack Implementaion
Enter 1 to Check the size of the Stack
Enter 2 for Push Operation
Enter 3 for Pop Operation
Enter 4 for Peek Operation
Enter 5 to  print Stack Elements
Enter X to terminate the program
""")
    operation=input("Enter your choice!")
    if(operation.lower()=='x'):
        break
    else:
        myStackDict[operation]()
