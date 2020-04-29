class LinkedListNode(object):
    
    def __init__(self, value):
        self.head = None
        self.tail = None
        self.value = value


class FirstUnique(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.isUniqueDict = {}
        self.first_node = None
        self.last_node = None
        
        for num in nums:
            self.add(num)

    def showFirstUnique(self):
        """
        :rtype: int
        """
        if self.first_node == None:
            return -1
        return self.first_node.value

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        # Not unique
        needsProcessing, node = self.isUniqueDict.get(value, (False, None))
        if needsProcessing:
            # Remove from queue
            if node.head:
                node.head.tail = node.tail
            else:
                if node.tail:
                    self.first_node = node.tail
                    self.first_node.head = None
                else:
                    self.first_node = None
                
            if node.tail:
                node.tail.head = node.head
            else:
                if node.head:
                    self.last_node = node.head
                    self.last_node.tail = None
                else:
                    self.last_node = None
            
            self.isUniqueDict[value] = (not needsProcessing, node)
        # Unique
        elif not node:
            new_node = LinkedListNode(value)
            
            if self.last_node == None:
                self.first_node = new_node
                self.last_node = new_node
            else:
                new_node.head = self.last_node
                self.last_node.tail = new_node
                self.last_node = new_node
            
            self.isUniqueDict[value] = (True, new_node)

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)