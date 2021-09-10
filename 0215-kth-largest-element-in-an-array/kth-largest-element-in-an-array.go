// Given an integer array nums and an integer k, return the kth largest element in the array.
//
// Note that it is the kth largest element in the sorted order, not the kth distinct element.
//
//  
// Example 1:
// Input: nums = [3,2,1,5,6,4], k = 2
// Output: 5
// Example 2:
// Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
// Output: 4
//
//  
// Constraints:
//
//
// 	1 <= k <= nums.length <= 104
// 	-104 <= nums[i] <= 104
//
//


func findKthLargest(nums []int, k int) int {
    return doFindKthLargest(nums, k, 0, len(nums) -1)
}

func doFindKthLargest(nums []int, k int, start, end int) int {
    nlen := len(nums)
    targetPos := nlen -k
    
    for {
        pivotIndex := partition(nums, start, end)
        if pivotIndex == targetPos {
            return nums[pivotIndex]
        } else if pivotIndex < targetPos {
            start = pivotIndex + 1
        } else {
            end = pivotIndex - 1
        }
    }
}

func partition(nums []int, start, end int) int {
    pivot := nums[start]
    left, right := start + 1, end
    
    for left <= right {
        for left <= right && nums[left] <= pivot {
            left++
        }
        for left <= right && nums[right] > pivot {
            right--
        }
        if left <= right {
            nums[left], nums[right] = nums[right], nums[left]
        }
    }
    nums[right], nums[start] = nums[start], nums[right]
    return right
}
