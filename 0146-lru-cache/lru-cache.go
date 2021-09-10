// Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
//
// Implement the LRUCache class:
//
//
// 	LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
// 	int get(int key) Return the value of the key if the key exists, otherwise return -1.
// 	void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
//
//
// The functions get and put must each run in O(1) average time complexity.
//
//  
// Example 1:
//
//
// Input
// ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
// [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
// Output
// [null, null, null, 1, null, -1, null, -1, 3, 4]
//
// Explanation
// LRUCache lRUCache = new LRUCache(2);
// lRUCache.put(1, 1); // cache is {1=1}
// lRUCache.put(2, 2); // cache is {1=1, 2=2}
// lRUCache.get(1);    // return 1
// lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
// lRUCache.get(2);    // returns -1 (not found)
// lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
// lRUCache.get(1);    // return -1 (not found)
// lRUCache.get(3);    // return 3
// lRUCache.get(4);    // return 4
//
//
//  
// Constraints:
//
//
// 	1 <= capacity <= 3000
// 	0 <= key <= 104
// 	0 <= value <= 105
// 	At most 2 * 105 calls will be made to get and put.
//
//


type CacheNode struct {
    Next *CacheNode
    Prev*CacheNode
    Key int
    Val int
}

type LRUCache struct {
    Cap int
    Len int
    Head *CacheNode
    Tail *CacheNode
    Map map[int]*CacheNode
}


func Constructor(capacity int) LRUCache {
    m := make(map[int]*CacheNode)
    c := LRUCache{Cap: capacity, Map: m}
    return c
}


func (this *LRUCache) Get(key int) int {
    found, ok := this.Map[key]
    if !ok {
        return -1
    }
    if this.Head == found {
        return found.Val
    }
    if this.Tail == found {
        this.Tail = found.Prev
    }
    // move found to head
    if found.Next != nil {
        found.Next.Prev = found.Prev
    }
    if found.Prev != nil {
        found.Prev.Next = found.Next
    }
    this.Head.Prev, found.Next = found, this.Head
    this.Head = found
    return found.Val
}



func (this *LRUCache) Put(key int, value int)  {
    found, ok := this.Map[key]
    if ok {
        found.Val = value
        _ = this.Get(found.Key) // to move found node to head
        return
    }
    
    // add to head
    n := &CacheNode{Key: key, Val: value}
    
    if len(this.Map) == 0 {
        this.Tail = n
    } else {
        this.Head.Prev, n.Next = n, this.Head
    }
    this.Map[key], this.Head = n,n
    if this.Cap == this.Len {
        delete(this.Map, this.Tail.Key)
        this.Len, this.Tail = this.Len-1, this.Tail.Prev
    }
    this.Len++
}


/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
