

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __iter__(self):
        self.stop_iter_flag = False
        self.node = self.head
        return self

    def __next__(self):
        if self.stop_iter_flag:
            raise StopIteration
        value = self.node.value
        if self.node.next:
            self.node = self.node.next
        else:
            self.stop_iter_flag = True
        return value

    def print_list(self):
        temp = self.head
        while (temp):
            print(str(temp.value) + " ", end="")
            temp = temp.next

    def __str__(self):
        temp = self.head
        l1 = "["
        while (temp):
            l1 += str(temp.value) + ", "
            temp = temp.next
        return l1[:-2] + "]"

    def __getitem__(self, index):
        temp = self.head
        index_map = {}
        i = 0
        while (temp):
            index_map[i] = temp.value
            temp = temp.next
            i += 1
        return index_map[index]



ll1 = LinkedList()

A = Node(1)
B = Node(2)
C = Node(3)

ll1.head = A
A.next = B
B.next = C

for v in ll1:
    print(v)

ll1.print_list()
print(ll1)
print(ll1[1])