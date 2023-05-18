class LinkedList:
    def __init__(self,  nodes=None):
        self.head = None

        if nodes is not None:
            node = Node(data=nodes.pop(0).get_data())
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem.get_data())
                node = node.next


    def set_head(self, Node):
        self.head = Node

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def remove_duplicates(self):
        if self.head is None:
            return
        node = self.head
        seen_data = set()
        while node is not None:
            if node.data not in seen_data:
                seen_data.add(node.data)
                prev = node
                node = node.next
            else:
                prev.next = node.next
                node = node.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def repr(self):
        return "{}({!r})".format(self.__class__.__name__, self.data)

    def get_data(self):
        return self.data

    def __repr__(self):
        return self.data


llist = LinkedList()
first_node = Node("primo")
llist.head = first_node
print(llist)


second_node = Node("secondo")
third_node = Node("terzo")
quarto = Node("quarto")
quinto = Node("quarto")

first_node.next = second_node
second_node.next = third_node
print(llist)

# Giving the list of nodes
nodes = [first_node, second_node, third_node, quarto, quinto]
llist2 = LinkedList(nodes)
print(llist2)

llist2.remove_duplicates()