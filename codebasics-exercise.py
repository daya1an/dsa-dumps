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

if __name__ == '__main__':
    root = build_management_tree()
    root.printItTree("name")
    print("\n")
    root.printItTree("designation")
    print("\n")
    root.printItTree("both")
    pass