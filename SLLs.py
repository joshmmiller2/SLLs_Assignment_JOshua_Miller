class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    
    def print_values(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    
    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self
        new_node = SLNode(val)
        current = self.head
        while (current.next != None):
            current = current.next
        current.next = new_node
        return self
    def remove_from_front(self):
        self.head = self.head.next
        return self
    def remove_from_back (self):
        if self.head != None:
            current = self.head
            while current.next.next != None:
                current = current.next
            current.next = None
        return self
class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

sll = SList()
sll.add_to_front("B").add_to_front ("A").add_to_back("C").remove_from_front().remove_from_back().add_to_back("Z").print_values()
sll2 = SList()
sll2.add_to_back("Z")