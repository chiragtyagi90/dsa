class Queues:
    def __init__(self):
        print("Implementing Queues using Python Built In List Class...")
        self.data=[]
    def enque(self):
        element=input("Enter the element to add to the queue!!!")
        print(f"""Inserting element {element} into the queue""")
        self.data.append(element)
    def isNotEmpty(self):
        print("Inside isNotEmpty...")
        return len(self.data)>0
    def deque(self):
        print("Inside deque...")
        if(self.isNotEmpty()):
            print(f"""Deleting element {self.data.pop(0)} from the queue""")
        else:
            print("Queue is empty")
    def getQueueElements(self):
        print(self.data)
    def getQueueLength(self):
        print(len(self.data))
    def top(self):
        print(self.data[0])


q=Queues()
mydict = {"1":q.enque,"2":q.getQueueElements,"3":q.deque,"4":q.getQueueLength,"5":q.top}
while True:
    print(f"""
1.Enter 1 to Add elements into the queue!
2.Enter 2 to view the elements of the queue!
3.Enter 3 to delete an element from the queue!
4.Enter 4 to get the length of the queue!
5.Enter 5 to see the top element of the queue!
6.Enter 6 to exit the program!1
""")
    operation=input("Enter your choice:")
    print(f"""Operation Selected is {operation}""")
    if(operation=="6"):
        break
    else:
        mydict[operation]()

print("Queue Demo Finished")





