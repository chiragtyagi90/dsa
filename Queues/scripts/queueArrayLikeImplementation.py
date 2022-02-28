class Queue:
    def __init__(self):
        print("Implementing Queues using Python Built In List Class...")
        print(f"""Here we are tring to mimic the array based implementation.
So for this example we will restrict of queue to the maximum size which the user selects:
""")
        self.data=[]
        self.MaxQueueLength = 0

    def enque(self):
        if(self.MaxQueueLength==0 or len(self.data)<self.MaxQueueLength):
            self.MaxQueueLength = int(input("Enter the maximum length of the array!"))
            for i in range(0,self.MaxQueueLength):
                self.data.append(input(f"""Enter {i+1} element of the queue!"""))
            print(f"""{self.MaxQueueLength} Elements inserted into the Queue!""")
        elif(self.MaxQueueLength>=0):
                print("Can not insert more Elements as Queue is Full! Delete some elements!!!")

    def deque(self):
        self.data.pop(0)
        self.MaxQueueLength=self.MaxQueueLength-1
    def getQueueElements(self):
        print(self.data)
    def getQueueLength(self):
        pass
    def top(self):
        pass


q=Queue()
mydict = {"1":q.enque,"2":q.getQueueElements,"3":q.deque,"4":q.getQueueLength,"5":q.top}
while True:
    print(f"""

1.Enter 1 to Add elements into the queue!
2.Enter 2 to view the elements of the queue!
3.Enter 3 to delete an element from the queue!
4.Enter 4 to get the length of the queue!
5.Enter 5 to see the top element of the queue!
6.Enter 6 to exit the program!
""")
    operation=input("Enter your choice:")
    print(f"""Operation Selected is {operation}""")
    if(operation=="6"):
        break
    else:
        mydict[operation]()

print("Queue Demo Finished")