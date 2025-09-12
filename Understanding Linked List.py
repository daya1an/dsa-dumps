class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def addFirst(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        
    def addLast(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode
    
    def printLL(self):
        curNode = self.head
        
        while curNode:
            print(curNode.data, end= " => ")
            curNode = curNode.next
        print("None")
    
    def findNodePos(self, target):
        
        curNode = self.head
        pos = 0
        while curNode.next:
            if curNode.data == target:
                return "Position: " + str(pos)
            else:
                pos+=1
                curNode = curNode.next
        return str(-1)
    
    def deleteNode(self, target):
        
        if self.head == None:
            return "Empty"
        
        if self.head.data == target:
            self.head = None
            return "First Node"
        
        curNode = self.head
        pos = 0 
        while curNode:
            if curNode.data == target:
                curNode.next = curNode.next.next
                return "Deleted Node " + str(curNode.data) + " from Position " + str(pos)
            else:
                curNode = curNode.next
                pos+=1
        
        if curNode == None:
            return str(target) + " Node not Found!!!"

ll = LinkedList()

for i in range(0,100,10):
    ll.addLast(i+10)

ll.printLL()
print(ll.findNodePos(40))
print(ll.deleteNode(170))