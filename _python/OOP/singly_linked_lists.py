# starts new node
class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None


# creates list and adds to / takes away from
class SList:
    def __init__ (self):
        self.head = None
    
    # sets location of curret node and next node location
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    
    def print_values(self):
        runner = self.head  # points to the first node in the list
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self
    
    def add_to_back (self, val):
        # if item is first added, run add_to_front
        if self.validator() == False:
                self.add_to_front(val)
                return self
        else:
            # if list has multiple nodes, iterate through list to end, and make last node
            new_node = SLNode(val)
            runner = self.head
            while (runner.next != None):
                runner = runner.next
            runner.next = new_node
            return self
    
    def remove_from_front (self):
        if self.validator():
            self.head = self.next
            return self
    
    def remove_from_end (self):
        if self.validator():
            runner = self.head
            while (runner != None):
                temp = runner
                runner = runner.next
            temp.next = None
        return self
    
    def validator (self):
        if self.head == None:
            return False
        else:
            return True
        
    def remove_val (self, val):
        if self.validator():
            if self.head.value == val:
                self.remove_from_front()
            else:
                runner = self.head
                while (runner.value != val & runner.next != None):
                    temp = runner
                    runner = runner.next
                temp.next = runner.next
        return self
    
    def insert_at (self, val, n):
        if self.validator():
            if n == 0:
                self.add_to_front(val)
            else:
                new_node =- SLNode(val)
                runner = self.head
                counter = 0
                while (runner != None & counter != n):
                    counter += 1
                    temp = runner
                    runner = runner.next
                temp.next = new_node
                new_node.next = runner
        
    


my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()