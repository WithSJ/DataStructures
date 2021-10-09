
class Node:
    def __init__(self):
        self.data = None
        self.next = None


class Array:
    def __init__(self,size):
        self.arr = Node()
        self.size = size
        temp = self.arr
        
        for i in range(size):
            temp.next = Node()
            temp.data = i
            temp = temp.next
    
    def show(self,size):
        temp = self.arr
        for i in range(size):
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    arr = Array(10)
    arr.show(10)
            

