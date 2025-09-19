# BinarySearchTree

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self, data):
        if data == self.data:
            return

        if data < self.data:
            #add data in left sub-tree
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data in right sub-tree
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def inOrderTraversal(self):
        elements = []

        if self.left:
           elements+=self.left.inOrderTraversal()

        if self.data:
           elements.append(self.data)

        if self.right:
            elements+=self.right.inOrderTraversal()

        return elements

    def preOrderTraversal(self):
        elements = []

        if self.data:
            elements.append(self.data)

        if self.left:
            elements+=self.left.preOrderTraversal()

        if self.right:
            elements+=self.right.preOrderTraversal()

        return elements

    def search(self,val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def findMinLoop(self):
        curr = self
        while curr.left is not None:
            curr = curr.left
        return curr.data

    def findMin(self):
        if self.left is None:
            return self.data
        return self.left.findMin()

    def findMaxLoop(self):
        curr = self
        while curr.right is not None:
            print(curr.data)
            curr = curr.right
        return curr.data

    def findMax(self):
        if self.right is None:
            return self.data
        return self.right.findMax()

    def delete(self, val):

        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.right is None and self.left is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            # minVal = self.right.findMin()
            # self.data = minVal
            # self.right = self.right.delete(minVal)

            #WITH MAX VALUE
            maxVal = self.left.findMax()
            self.data = maxVal
            self.left = self.left.dalete(maxVal)

        return self

    def depth(self):

        l = r = self
        rd = ld = 1

        while l.left is not None:
            l = l.left
            ld += 1

        while r.right is not None:
            r = r.right
            rd += 1

        print(rd,ld)
        return max(ld, rd)



def buildBST(elements):

    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.addChild(elements[i])
    return root

if __name__ == "__main__":

    elements = [22, 10 , 1 , 17, 5, 72, 26, 1, 68, 12, 8, 98]

    btree = buildBST(elements)

    print("In Order Traversed: ",btree.inOrderTraversal()) #[1, 5, 8, 10, 12, 17, 22, 26, 68, 72, 98]
    print("Pre Order Traversed: ", btree.preOrderTraversal()) #[22, 10, 1, 5, 8, 17, 12, 72, 26, 68, 98]
    e = 68
    print("Position of ", str(e), " : ", btree.search(e))

    btree.delete(e)
    print("After removing " + str(e) + " : ", btree.inOrderTraversal())


    print("Minimum : ", btree.findMin(), " = ", btree.findMinLoop())
    print("Maximum : ", btree.findMax(), " = ", btree.findMaxLoop())
    print("Depth = ", btree.depth())

    states = ["Tamil Nadu", "Kerala", "Andhra", "Telangana","Karnataka","Maharashtra","Odissa","Bihar","Dehli"]
    statesTree = buildBST(states)
    print("States - InOrder: ", statesTree.inOrderTraversal())
    print("Tamil Nadu ? ", statesTree.search("Tamil Nadu"), "UP ? ", statesTree.search("UP"))
