class LinkedList(object):
    def __init__(self, own_key, value):
        self.own_key = own_key
        self.value = value
        self.head = None
        self.tail = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.storage = {}
        self.capacity = capacity
        self.size = 0
        self.front_node = None
        self.back_node = None

    """
    def print_self(self):
        x = "HEAD -> "
        tmp = self.front_node
        while tmp:
            x += str(((tmp.own_key, tmp.value, tmp.head, tmp.tail))) + " -> "
            tmp = tmp.tail
        print(x + "TAIL")
    """
    
    def get(self, key, fetchNode=False):
        """
        :type key: int
        :rtype: int
        """
        rv = self.storage.get(key, None)
        # Update cache
        if rv:
            # No cache update required
            if self.size == 1 or self.front_node == rv:
                if fetchNode:
                    return rv
                else:
                    return rv.value
            if rv.head:
                rv.head.tail = rv.tail
            if rv.tail:
                rv.tail.head = rv.head
            else:
                self.back_node = rv.head
            rv.tail = self.front_node
            rv.head = None
            self.front_node = rv
            rv.tail.head = self.front_node
            if fetchNode:
                return rv
            else:
                return rv.value
        else:
            if fetchNode:
                return None
            else:
                return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        rv = self.get(key, True)
        # Set if exists
        if rv != None:
            rv.value = value
            return
        
        # Add new node if not exists
        if self.capacity == 1 and self.size == 1:
            # Remove existing
            to_delete = self.front_node
            del self.storage[to_delete.own_key]
            self.front_node = None
            self.back_node = None
        elif self.size == self.capacity:
            # Remove existing
            to_delete = self.back_node
            self.back_node.head.tail = None
            self.back_node = to_delete.head
            del self.storage[to_delete.own_key]
        else:
            self.size += 1

        # Update cache
        rv = LinkedList(key, value)
        rv.head = None
        rv.tail = self.front_node
        if rv.tail:
            rv.tail.head = rv
        self.front_node = rv
        if self.size == 1:
            self.back_node = rv
        
        self.storage[key] = rv
        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)