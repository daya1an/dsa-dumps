from numpy.distutils.conv_template import header


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

    def reverseIt(self):
        prev = None
        curr = self.head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head = prev

    def sortIt(self):
        if self.head == None or self.head.next == None:
            return self.head

        i = None
        while i!=self.head:
            j = self.head
            while j.next != i:
                if j.data > j.next.data:
                    j.data, j.next.data = j.next.data, j.data
                j = j.next
            i = j


ll = LinkedList()

for i in range(0,50,10):
    ll.addLast(i+10)

for i in range(0,60,5):
    if i%5 == 0:
        ll.addLast(i)
    else:
        ll.addFirst(i)

ll.printLL()

print(ll.findNodePos(40))
print(ll.deleteNode(170))

ll.reverseIt()

print("New Unsorted List: ")

ll.printLL()

ll.sortIt()

print("Sorted List: ")

ll.printLL()
