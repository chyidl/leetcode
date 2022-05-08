// Design and implement a data structure for a Least Frequently Used (LFU) cache.
//
// Implement the LFUCache class:
//
//
// 	LFUCache(int capacity) Initializes the object with the capacity of the data structure.
// 	int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
// 	void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
//
//
// To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.
//
// When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.
//
// The functions get and put must each run in O(1) average time complexity.
//
//  
// Example 1:
//
//
// Input
// ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
// [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
// Output
// [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
//
// Explanation
// // cnt(x) = the use counter for key x
// // cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
// LFUCache lfu = new LFUCache(2);
// lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
// lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
// lfu.get(1);      // return 1
//                  // cache=[1,2], cnt(2)=1, cnt(1)=2
// lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
//                  // cache=[3,1], cnt(3)=1, cnt(1)=2
// lfu.get(2);      // return -1 (not found)
// lfu.get(3);      // return 3
//                  // cache=[3,1], cnt(3)=2, cnt(1)=2
// lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
//                  // cache=[4,3], cnt(4)=1, cnt(3)=2
// lfu.get(1);      // return -1 (not found)
// lfu.get(3);      // return 3
//                  // cache=[3,4], cnt(4)=1, cnt(3)=3
// lfu.get(4);      // return 4
//                  // cache=[4,3], cnt(4)=2, cnt(3)=3
//
//
//  
// Constraints:
//
//
// 	0 <= capacity <= 104
// 	0 <= key <= 105
// 	0 <= value <= 109
// 	At most 2 * 105 calls will be made to get and put.
//
//
//  
//  


type Cache struct {
    key int
    value int
    lastUsedTime int64
    freq int
}

type LFUCache struct {
    data []*Cache
    capacity int
    m map[int]int
}


func Constructor(capacity int) LFUCache {
    c := LFUCache{}
    c.data = make([]*Cache,0)
    c.capacity = capacity
    c.m = make(map[int]int)
    return c
}


func (this *LFUCache) Get(key int) int {
    value := -1
    if v, ok := this.m[key]; ok && v!=-1 {
        value = this.data[v-1].value
        this.data[v-1].freq = this.data[v-1].freq + 1
        this.data[v-1].lastUsedTime = time.Now().UnixNano()
    }
    return value
}


func (this *LFUCache) Put(key int, value int)  {
    c := Cache{
        key: key,
        value: value,
        freq:1,
        lastUsedTime:time.Now().UnixNano(),
    }
    if this.capacity == 0 {
        this.m[key]=-1
        return
    }
    if v,ok:=this.m[key];ok && v!=-1 {
        this.data[v-1].value = value
        this.data[v-1].freq = this.data[v-1].freq+1
        this.data[v-1].lastUsedTime=time.Now().UnixNano()
    } else if len(this.data) == this.capacity {
        // 啥意思 没看懂
        mini := 2147483647
        minT := time.Now().UnixNano()
        var index int
        for i:= 0; i<len(this.data); i++ {
            if mini > this.data[i].freq {
                mini = this.data[i].freq
                minT = this.data[i].lastUsedTime
                index=i
            } else if mini == this.data[i].freq && minT > this.data[i].lastUsedTime {
                index = i
                minT = this.data[i].lastUsedTime
            }
        }
        // fmt.Println(index)
        this.m[this.data[index].key] = -1
        this.data[index] = &c
        this.m[key] = index + 1
    } else {
        this.data = append(this.data, &c)
        this.m[key] = len(this.data)
    }
}


/**
 * Your LFUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
