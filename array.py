
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
            temp = temp.next
    
    def insertAt(self,index,data):
        self.checkIndex(index)
        temp = self.arr
        for i in range(index):
            temp = temp.next
        
        temp.data = data
        

    def show(self,size):
        self.checkIndex(size)
        temp = self.arr
        for i in range(size):
            print(i," : ",temp.data)
            temp = temp.next

    def checkIndex(self,index):
        if index > self.size or index < 0:
            raise IndexError("Out of index")
    
    def __repr__(self) -> str:
        stng = "["
        temp = self.arr
        for i in range(self.size):
            stng += str(temp.data) + ","
            temp = temp.next
        return stng[:-1] + "]"
    
    def __getitem__(self,index):
        self.checkIndex(index)
        temp = self.arr
        for i in range(index):
            temp = temp.next
        
        return temp.data

if __name__ == "__main__":
    arr = Array(10)
    arr.insertAt(1,"Data")
    arr.show(10)
    print(arr[1])
    print( arr)
            

