class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        printingvalue = self.head
        while printingvalue is not None:
            print(printingvalue.data)
            printingvalue = printingvalue.next

    def beg(self, data4):
        new = Node(data4)
        new.next = self.head
        self.head= new

    def end(self, data5):
        newest = Node(data5)
        if self.head is None:
            self.head = newest
            return
        lastnode = self.head
        while (lastnode.next):
            lastnode = lastnode.next
        lastnode.next=newest

    def inbetween(self, node, data6):
        bet = Node(data6)
        bet.next = node.next
        node.next = bet


    def delNode(self,deldata):
        new=self.head
        if new is not None:
            if new.data==deldata:
                self.head=new.next
                new=None
                return
        while(new is not None):
            if new.data==deldata:
                break
            prev=new
            new=new.next

        if new==None:
            return
        prev.next=new.next
        new=None


x = LinkedList()
x.head = Node('sinchana')
data2 = Node('teja')
data3 = Node('seema')
x.head.next = data2
data2.next = data3
x.beg('karthik')
x.inbetween(x.head.next,'spandu')
x.end('amma')
x.delNode('seema')
x.delNode('karthik')
x.print()
