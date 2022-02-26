class Stack:
    def __init__(self):
        self._data=[]
        msg=f"""Program to reverse the string using Stack \n
Enter the String to be reversed!  
            """
        print(msg)

    def push(self,e):
        self._data.append(e)

    def checkData(self):
        print(self._data)
    def pop(self):
        if(len(self._data)>0):
            return self._data.pop()
        else:
            print("Nothing to Pop")

s=Stack()
str=input()
for c in str:
    s.push(c)
print("Check Data")
s.checkData()
rev=[]
for i in range(0,len(str)):
    rev.append(s.pop())


print("Reversed name is:")
print("".join(rev))