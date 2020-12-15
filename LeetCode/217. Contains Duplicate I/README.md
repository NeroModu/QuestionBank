# 217. Contains Duplicate I
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

### Example 1:
```
Input: [1,2,3,1]
Output: true
```

### Example 2:
```
Input: [1,2,3,4]
Output: false
```

### Example 3:
```
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
```

## Solution
Theres a few ways of doing this, with some being more efficient than others. Lets look at four different approaches.

### 1. Make a new list
This is the most trivial solution. It involves looping through each element in the given list and adding it to a new list. At each iteration, you then check if that int is already in the new list. If it is, return true.
```python
def containsDuplicate(self, nums: List[int]) -> bool:
    newList = []
    for i in nums:
        if i in newList:
            return True
        else:
            newList.append(i)

    return False
```
You could also use a set instead, since no duplicates should appear. But in any case this is a relatively inefficient solution clocking in at `O(n log(n))`

### 2. Use list.count()
This solution does not use a new list. Instead it just checks how many times each element appears, and if it's ever over one, returns true.
```python
def containsDuplicate(self, nums: List[int]) -> bool:
    for i in nums:
        if nums.count(i) > 1:
            return True
    return False
```
While this method uses less space, since there is no new list created, it turns out the count() method loops through the entire list each time, making this even more inefficient than the previous solution at `O(n^2)`

### 3. Use set() & len()
For this solution we leverage the power of Python, using a built in conversion tool `set()`. Since sets cannot have duplicates, when a list is converted to a set, all duplicates are removed. So if we make a set out of our list, then compare that set's length to the length of our list, we can see if any duplicates were found.
```python
def containsDuplicate(self, nums: List[int]) -> bool:
    return len(nums) != len(set(nums))
```
It only returns true if the length of the set is different, meaning a duplicate was found and removed. This also has a runtime of `O(n log(n))` but it avoids using extra memory to make a copy of the entire list.

### 4. 
