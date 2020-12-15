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

### 2. Use list.count

### 3. Use len()

### 4. 
