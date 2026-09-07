class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(10)
node2 = Node(20) 
node3 = Node(30) 
node4 = Node(40) 
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node2.next = node3.next        #30-a delete pannanum na:|20 → 30 → 40| 20-oda next-a 30-la irundhu 40-kku maathu.|Previous.next = Current.next|Delete panna node-a skip pannu

current = node1

while current:
    print(current.data, end=" → ")
    current = current.next

print("None")
