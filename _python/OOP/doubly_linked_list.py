class DLNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DLList:
    def __init__ (self):
        self.head = None
        self.length = 0
            
    def add_to_front(self, val):
        new_node = DLNode(val)
        if self.head == None:
            self.head = new_node
        else:
            current_head = self.head
            new_node.next = current_head
            new_node.prev = None
            current_head.prev = new_node
            self.head = new_node
        return self
    
    def add_to_end(self, val):
        if self.validator() == False:
            self.add_to_front(val)
            return self
        else:
            new_node = DLNode(val)
            runner = self.head
            while (runner.next != None):
                runner = runner.next
            runner.next = new_node
            new_node.prev = runner
        return self
    
    def add_to_middle (self, val):
        if self.validator():
            self.list_length()
            half_way = int(self.length/2)
            if self.head.next == None:
                self.add_to_end(val) 
            else:
                new_node = DLNode(val)
                runner = self.head
                count = 0
                while (count != half_way and runner.next != None):
                    previous = runner
                    runner = runner.next
                    count +=1
                previous.next = new_node
                new_node.prev = previous
                new_node.next = runner
                runner.prev  = new_node
        else:
            return self
        return self
        
    def delete_node (self, node):
        if node == self.head:
            node.next = self.head
            node.prev = None
        else:
            previous = node.prev
            after = node.next
            previous.next = after
            after.prev = previous
        return self
    
    def loop_detector(self):
        if self.head.prev != None:
            previous = self.head.prev
            self.head.prev = None
            previous.next = None
        print("No loops found!")
        return self
    
    def delete_duplicate (self):
        runner = self.head
        while (runner.next != None):
            comparison = runner.val
            runnerB = runner.next
            while (runnerB.next != None):
                if runnerB.val == comparison:
                    self.delete_node(runnerB)
                    duplicate = True
                    break
                runnerB = runnerB.next
            runner = runner.next
            
        if duplicate != True:
            print("No duplicates found")
        return self
    
    
    # Does not work at this time
    # def reverse_list(self):
    #     # fix so runs while loops based on counters, not None. Maybe if loops instead?
    #     if self.validator():
    #         self.list_length()
    #         runner_A = self.head
    #         counter_A = 1
    #         while (runner_A.next != None):
    #             start = runner_A
    #             counter_B = counter_A+1
    #             runner_B = runner_A.next
    #             while (runner_B.next != None):
    #                 if (counter_B == self.length):
    #                     break
    #                 else:
    #                     runner_B = runner_B.next
    #                 counter_B +=1
    #             end = runner_B
    #             print("runner_b value:", runner_B.val)
    #             print("runner_a value:",runner_A.val)
    #             runner_B = start
    #             runner_A = end
    #             print("runner_b value after:", runner_B.val)
    #             print("runner_a value after:", runner_A.val)
    #             self.length-=1
    #             counter_A += 1
    #             runner_A = runner_A.next
    #     return self
    
    def print_values (self):
        runner = self.head
        while (runner != None):
            print(runner.val)
            runner = runner.next
        print("*"*20)
        return self
            
    def list_length (self):
        runner = self.head
        self.length = 0
        while (runner != None):
            runner = runner.next
            self.length += 1
        return self
    
    def validator (self):
        if self.head == None:
            return False
        else:
            return True
                
dll = DLList()
dll.add_to_front(1).print_values().add_to_end(4).print_values().add_to_front(3).print_values().add_to_middle(1).print_values().delete_duplicate().print_values().add_to_middle(5).add_to_end(3).add_to_front(8).print_values()