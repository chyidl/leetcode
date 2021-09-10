# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
#
# Implement the LRUCache class:
#
#
# 	LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# 	int get(int key) Return the value of the key if the key exists, otherwise return -1.
# 	void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
#
#
# The functions get and put must each run in O(1) average time complexity.
#
#  
# Example 1:
#
#
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
#
#
#  
# Constraints:
#
#
# 	1 <= capacity <= 3000
# 	0 <= key <= 104
# 	0 <= value <= 105
# 	At most 2 * 105 calls will be made to get and put.
#
#


"""
Using linked list and hashmap together

Time complexity: O(N)
Space complexity: O(N)
"""


class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    """
    Least Recently Used (LRU) cache
    """

    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with positive size capacity
        """
        self.cache = {}
        self.count = 0
        self.capacity = capacity

        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        """
        Return the value of the key if the key exists, otherwise return -1
        """
        node = self.cache.get(key, None)
        if not node:
            return -1

        self.insert_to_head(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        """
        Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache.
        If the number of keys exceeds the capacity from this operation, evict the least recently used key.
        """
        node = self.cache.get(key, None)

        if not node:
            new_node = ListNode(key, value)

            self.cache[key] = new_node
            self.add_node(new_node)

            self.count += 1

            if self.count > self.capacity:
                tail = self.remove_tail()
                del self.cache[tail.key]
                self.count -= 1
        else:
            node.value = value
            self.insert_to_head(node)

    def add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def insert_to_head(self, node):
        self.remove_node(node)
        self.add_node(node)

    def remove_tail(self):
        res = self.tail.prev
        self.remove_node(res)
        return res


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
