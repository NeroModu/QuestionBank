# Trapping Rain Water
Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

Example:

![](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)
```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
```

# Solution
Basically, at every iteration of our main loop, we need to iterate backwards to the beginning then forwards to the end. We do this to find the biggest numbers before and after the current number to see if they can hold water between them.

We start by setting two new vars, `size` to hold our solution and `length` to hold the length of `height`. We do the 2nd to avoid calling `len(height)` multiple times and slowing down the problem. Because for this one, speed really matters.
```
size = 0
length = len(height)
```

Then we loop thru every index of height.
```
for i in range(length):
```

Now we initialize vars to hold the maximum values on both the right and left sides.
```
leftMax = 0
rightMax = 0
```

Next we loop thru the indexes between the current iteration and the beginning of the array, backwards. So between `i` and our start minus one, with step `-1`.
```
for j in range(i, -1, -1):
```

Inside this loop we make `height[j]` the new `leftMax` only if it's bigger than it was previously. This collects all the "pockets" between two towers of the same height or bigger.
```
if height[j] > leftMax:
  leftMax = height[j]
```

But python gives us a nice `max()` function we can use.
```
leftMax = max(leftMax, height[j])
```

Then we do the same thing to the right, only this time looping forward.
```
for j in range(i, length):
  rightMax = max(rightMax, height[j])
```

Once outside both inner loops, we add either `leftMax` or `rightMax`, whichever is smaller (because the bigger one will have it's own set of left and right accounted for later), to our answer, `size`. And we also subtract `height[i]` since our current iteration will be accounted for in another loop.
```
size += min(leftMax, rightMax) - height[i]
```

Lastly, outside our outer loop, we `return size`
