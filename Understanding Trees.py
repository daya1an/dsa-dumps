from sys import prefix


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def print_trees(self ):
        spaces = "\t" * self.get_level()
        prefix = spaces + "|---" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_trees()

    def print_IT_Tree(self):
        spaces = "\t" * self.get_level()
        prefix = spaces + "|---" if self.parent else ""
        print(prefix + self.data + self.data)
        if self.children:
            for child in self.children:
                child.print_IT_Tree()

    def get_level(self):
        lvl = 0
        p = self.parent
        while p:
            lvl+=1
            p = p.parent
        return lvl

# def build5Tree():
#     root = TreeNode("Five")
#
#     for i in range(25):
#         if i % 5 != 0:
#             child = TreeNode(i)
#             root.addChild(child)
#         else:
#             node = TreeNode(i)
#             root.addChild(node)
#
#     return root

def build_SWs_Tree():

    root = TreeNode("Software")

    jetbrains = TreeNode("JetBrains")
    jetbrains.addChild(TreeNode("PyCharm"))
    jetbrains.addChild(TreeNode("WebStorm"))
    jetbrains.addChild(TreeNode("DataGrip"))
    jetbrains.addChild(TreeNode("IntelliJ"))

    microsoft = TreeNode("Mirosoft")
    microsoft.addChild(TreeNode("VSCode"))
    microsoft.addChild(TreeNode("Visual Studio"))
    microsoft.addChild(TreeNode("SQL Server Studio"))

    apache = TreeNode("Apache")
    apache.addChild(TreeNode("Eclipse"))
    apache.addChild(TreeNode("NetBeans"))
    apache.addChild(TreeNode("Kafka"))

    root.addChild(jetbrains)
    root.addChild(microsoft)
    root.addChild(apache)

    print(root.get_level(), jetbrains.get_level())
    return root

class ItTreeNode:
    def __init__(self, name, designation):
        self.children = []
        self.name = name
        self.designation = designation
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def printItTree(self, option):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|--" if self.parent else ""
        if option == "both":
            print(prefix + self.name + " ( " + self.designation + " ) ")
        elif option == "designation":
            print(prefix + self.designation)
        elif option == "name":
            print(prefix + self.name)
        if self.children:
            for child in self.children:
                child.printItTree(option)

    def get_level(self):
        lvl = 0
        p = self.parent
        while p:
            lvl+=1
            p = p.parent
        return lvl

def build_management_tree():

    ceo = ItTreeNode("Nilpul","CEO")

    cto = ItTreeNode("Chinmay", "CTO")

    ih = ItTreeNode("Vishwa","Infrastructure Head")
    ih.addChild(ItTreeNode("Dhaval", "Cloud Manger"))
    ih.addChild(ItTreeNode("Abijith", "App Manager"))

    cto.addChild(ih)
    cto.addChild(ItTreeNode("Amir","Application Head"))

    hr = ItTreeNode("Gels","HR LEAD")
    hr.addChild(ItTreeNode("Peter","Recruitment Manager"))
    hr.addChild(ItTreeNode("Waqas","Policy Manager"))

    ceo.addChild(cto)
    ceo.addChild(hr)

    return ceo

class GlobalTreeNode:

    def __init__(self, place):
        self.place = place
        self.children = []
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def getLevel(self):
        lvl = 0
        p = self.parent
        while p:
            lvl+=1
            p = p.parent

        return lvl

    def print_GlobalTreeNode(self, lvl):
        if lvl >= self.getLevel():
            spaces = ' ' * self.getLevel() * 3
            prefix = spaces + "|--" if self.parent else ""
            print(prefix + self.place)
            if self.children:
                for child in self.children:
                    child.print_GlobalTreeNode(lvl)

def buidl_GlobalTreeNode():

    root = GlobalTreeNode("Global")

    india = GlobalTreeNode("India")

    gujarat =  GlobalTreeNode("Gujarat")
    karnataka = GlobalTreeNode("Karnataka")

    gujarat.addChild(GlobalTreeNode("Ahmedabad"))
    gujarat.addChild(GlobalTreeNode("Baroda"))

    karnataka.addChild(GlobalTreeNode("Bangalore"))
    karnataka.addChild(GlobalTreeNode("Mysore"))

    india.addChild(gujarat)
    india.addChild(karnataka)

    newJersey = GlobalTreeNode("New Jersey")
    newJersey.addChild(GlobalTreeNode("Princetone"))
    newJersey.addChild(GlobalTreeNode("Trenton"))

    california = GlobalTreeNode("California")
    california.addChild(GlobalTreeNode("San Fransico"))
    california.addChild(GlobalTreeNode("Mountain View"))
    california.addChild(GlobalTreeNode("Palo Alto"))

    usa = GlobalTreeNode("USA")
    usa.addChild(newJersey)
    usa.addChild(california)

    root.addChild(india)
    root.addChild(usa)

    return root


if __name__ == '__main__':
    # softwares = build_SWs_Tree()
    # softwares.print_trees()

    # fiveTree = build5Tree()
    # fiveTree.print_trees()

    # root = build_management_tree()
    #
    # root.printItTree("name")
    # print("\n")
    # root.printItTree("designation")
    # print("\n")
    # root.printItTree("both")

    globalRoot = buidl_GlobalTreeNode()
    print("    LEVEL 0")
    globalRoot.print_GlobalTreeNode(0)

    print(" \n LEVEL 1")
    globalRoot.print_GlobalTreeNode(1)

    print(" \n LEVEL 2")
    globalRoot.print_GlobalTreeNode(2)

    print(" \n LEVEL 3")
    globalRoot.print_GlobalTreeNode(3)

    pass