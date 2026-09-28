# # # # class node:
# # # #     def __init__(self, value):
# # # #         self.value = value
# # # #         self.left = None
# # # #         self.right = None

# # # # def insert(root, value):

# # # #     if root is None:
# # # #         return Node(value)
    
# # # #     if value < root.value:
# # # #         root.left = insert(root.left, value)

# # # #     else:
# # # #         root.right = insert(root.right, value)

# # # #     return root    

# # # class Node:
# # #     def __init__(self, Value):
# # #         self.value = Value
# # #         self.left = None
# # #         self.right = None

# # # root = Node(50)

# # # root.left = Node(30)
# # # root.right = Node(70)

# # # print(root.value)
# # # print(root.left.value)
# # # print(root.right.value)

# # class Node:
# #     def __init__(self, student_id):
# #         self.student_id = student_id
# #         self.left = None
# #         self.right = None

# # root = Node(50)

# # root.left = Node(30)
# # root.right = Node(70)

# # root.left.left = Node(20)
# # root.left.right = Node(40)

# # print("Root Student ID:", root.student_id)
# # print("Left Student ID:", root.left.student_id)
# # print("Right Student ID:", root.right.student_id)
# # print("20 Student ID:", root.left.left.student_id)
# # print("40 Student ID:", root.left.right.student_id)
# class Node:
#     def __init__(self, order_id):
#         self.order_id = order_id
#         self.left = None
#         self.right = None


# root = Node(50)

# root.left = Node(30)
# root.right = Node(70)

# root.left.left = Node(20)
# root.left.right = Node(40)

# print("Main Order:", root.order_id)
# print("Left Order:", root.left.order_id)
# print("Right Order:", root.right.order_id)


class Node:
    def __init__(self, patient_number):
        self.patient_number = patient_number
        self.left = None
        self.right = None


root = Node(50)

root.left = Node(10)
root.right = Node(10)

root.left.left = Node(20)
root.left.right = Node(40)


print("Root Patient:", root.patient_number)
print("Left Patient:", root.left.patient_number)
print("Right Patient:", root.right.patient_number)