class Node:                                                       #create node
    def __init__(self, data):                                     #constructor 
        self.data = data                                          # node value store yagom
        self.next = None


# Step 1: Nodes create pannrom
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)


# Step 2: Nodes connect pannrom
node1.next = node2
node2.next = node3


# Step 3: First node-la irundhu print pannrom
current = node1   #first node point painnum

while current:
    print(current.data, end=" → ")
    current = current.next                                       # ippa 20 ku move yagom

print("None")