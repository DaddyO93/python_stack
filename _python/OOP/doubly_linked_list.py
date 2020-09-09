class DLNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DLList:
    def __init__ (self):
        self.head = None
    
    def add_to_front(self, val):
        new_node = DLNode(val)
        current_head = self.head
        prev = self.head.prev
        self.head = new_node
        new_node.next = current_head
        prev = current_head.prev
        return self
    
    def add_to_end(self, val):
        if self.validator() == False:
            self.add_to_front()
            return self
        new_node = DLNode(val)
        runner = self.head
        while (runner != None):
            runner = runner.next
        runner.next = new_node
        new_node.prev = runner
        return self
    
    def add_to_middle (self, val):
        new_node = DLNode(val)
        count = self.list_length()
        half_way = count/2
        runner = self.head
        count = 0
        while (count != half_way):
            runner = runner.next
            count +=1
        nxt = runner.next
        prev = runner.prev
        runner = new_node
        new_node.prev = prev
        new_node.next = nxt
        return self
        
    def delete_node (self, val):
        runner = self.head
        while (runner != None):
            if runner == val:
                prev = runner.prev
                current = runner.next
                runner = current
                current.prev = prev
        return self
    
    def delete_duplicate (self):
        runner = self.head
        while (runner != None):
            comparison = runner
            runner = runner.next
            while (runner != None):
                if runner == comparison:
                    self.delete_node(runner)
                    break
                runner = runner.next
        return self
    
    def print_values (self):
        runner = self.head
        while (runner != None):
            print(runner.val)
            runner = runner.next
            
    def list_length (self):
        runner = self.head
        count = 0
        while (runner != None):
            runner = runner.next
            count += 1
        return self
    
    def validator (self):
        if self.head == None:
            return False
        else:
            return True
                