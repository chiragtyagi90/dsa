class Queue:
    def __init__(self):
        print("Implementing Queues using Python Built In List Class...")
        print(f"""Menu Driven Queue implementation""")
        self.data=[]
        self.MaxQueueLength = 0
        self.firstRun=True

    def enque(self):

        #print(f""" self.MaxQueueLength = {self.MaxQueueLength} """)
        #print(f""" len(data) = {len(self.data)} """)
        if(self.MaxQueueLength==0 or len(self.data)<self.MaxQueueLength):
            if(self.firstRun):
                self.MaxQueueLength = int(input("Enter the maximum length of the array!"))
                length=self.MaxQueueLength
            else:
                newLength=self.MaxQueueLength-len(self.data)
                print(f"""Only {newLength} can be added to the queue""")
                length=newLength
            for i in range(0,length):
                self.data.append(input(f"""Enter {i+1} element of the queue!"""))
                self.firstRun=False
            print(f"""{self.MaxQueueLength} Elements inserted into the Queue!""")
        elif(self.MaxQueueLength>=0):
                print("Can not insert more Elements as Queue is Full! Delete some elements!!!")

    def deque(self):
        self.data.pop(0)
        self.getQueueLength()
    def getQueueElements(self):
        print(self.data)
    def getQueueLength(self):
        print(f"""Length of queue is {len(self.data)}""")
        print(f"""Empty space remaining in Queue is {self.MaxQueueLength-len(self.data)}""")
    def top(self):
        print(self.data[0])


q=Queue()
mydict = {"1":q.enque,"2":q.getQueueElements,"3":q.deque,"4":q.getQueueLength,"5":q.top}
while True:
    print(f"""

1.Enter 1 to Add elements into the queue!
2.Enter 2 to view the elements of the queue!
3.Enter 3 to delete an element from the queue!
4.Enter 4 to get the length of the queue!
5.Enter 5 to see the top element of the queue!
6.Enter X to exit the program!
""")
    operation=input("Enter your choice:")
    print(f"""Operation Selected is {operation}""")
    if(operation.lower()=="x"):
        break
    else:
        mydict[operation]()

print("***********************Queue Demo Finished***********************")