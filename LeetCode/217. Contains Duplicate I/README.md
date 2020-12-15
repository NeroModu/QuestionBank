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
### 3. Use len()


### 4. 
