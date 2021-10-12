class Node:
    def __init__(self) -> None:
        self.data = None
        self.next = None
    
class Stack:
    def __init__(self) -> None:
        self.head = None
    
    def push(self,data):
        temp = Node()
        temp.data = data
        temp.next = self.head
        self.head = temp

    def pop(self):
        data = self.head.data
        self.head = self.head.next
        return data

    def show(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next
            

if __name__ == "__main__":
    
    st = Stack()
    st.push(1)
    st.push(2)
    st.push(3)
    
    st.show()
    print("SHOW")

    print("Pop",st.pop())
    print("Pop",st.pop())
    print("Pop",st.pop())
    
            

        