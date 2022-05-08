// Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
//
// Implement the MinStack class:
//
//
// 	MinStack() initializes the stack object.
// 	void push(int val) pushes the element val onto the stack.
// 	void pop() removes the element on the top of the stack.
// 	int top() gets the top element of the stack.
// 	int getMin() retrieves the minimum element in the stack.
//
//
//  
// Example 1:
//
//
// Input
// ["MinStack","push","push","push","getMin","pop","top","getMin"]
// [[],[-2],[0],[-3],[],[],[],[]]
//
// Output
// [null,null,null,null,-3,null,0,-2]
//
// Explanation
// MinStack minStack = new MinStack();
// minStack.push(-2);
// minStack.push(0);
// minStack.push(-3);
// minStack.getMin(); // return -3
// minStack.pop();
// minStack.top();    // return 0
// minStack.getMin(); // return -2
//
//
//  
// Constraints:
//
//
// 	-231 <= val <= 231 - 1
// 	Methods pop, top and getMin operations will always be called on non-empty stacks.
// 	At most 3 * 104 calls will be made to push, pop, top, and getMin.
//
//


type intStack struct {
    s []int
}

func (s *intStack) empty() bool {
    return len(s.s) == 0
}

func (s *intStack) push(n int) {
    s.s = append(s.s, n)
}

func (s *intStack) peek() int {
    if s.empty() {
        panic("stack is empty")
    }
    return s.s[len(s.s) - 1]
}

func (s *intStack) pop() int {
    if s.empty() {
        panic("stack is empty")
    }
    
    val := s.s[len(s.s) - 1]
    s.s = s.s[:len(s.s) - 1]
    return val
}


type MinStack struct {
    mins intStack
    nums intStack
}


/** initialize your data structure here. */
func Constructor() MinStack {
    return MinStack{}
}


func (this *MinStack) Push(val int)  {
    this.nums.push(val)
    
    // we need to check if the mins stack is empty
    // the element has to be the smallest so far
    if this.mins.empty() || val <= this.mins.peek() {
        this.mins.push(val)
    }
}


func (this *MinStack) Pop()  {
    val := this.nums.pop()
    
    if val == this.mins.peek() {
        this.mins.pop()
    }
}


func (this *MinStack) Top() int {
    return this.nums.peek()
}


func (this *MinStack) GetMin() int {
    return this.mins.peek()
}


/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
