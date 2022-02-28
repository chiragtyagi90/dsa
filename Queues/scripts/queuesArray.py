class Queues:
    def __init__(self):
        print("Implementing Queues using Python Built In List Class...")
        self.data=[]
    def enque(self,element):
        print(f"""Inserting element {element} into the queue""")
        self.data.append(element)
        print(self.data)

    def isNotEmpty(self):
        print("Inside isNotEmpty...")
        return len(self.data)>0

    def deque(self):
        print("Inside deque...")
        if(self.isNotEmpty()):
            print(f"""Deleting element {self.data.pop(0)} from the queue""")
        else:
            print("Queue is empty")



q=Queues()
q.enque(10)
q.enque(20)
q.deque()
q.enque(99)
q.deque()
q.deque()
q.deque()