# Can Place Flowers
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

https://leetcode.com/problems/can-place-flowers/

## Solution
So we have an array `flowerbed` with 1s and 0s that can look like `[1,0,0,0,1]` or `[1,0,0]` or `[0,0]` or something, and an int `n` for number of flowers to place. Flowers can only go in spots in the array that are 0, and have 0s on both sides. So it seems like just a matter of looping through the array seeing where this condition is met.

We do need the index of the array, so we loop `range(len(flowerbed))`
```
for i in range(len(flowerbed)):
  if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
```

If this condition is met, we plant a flower (set spot to 1) and decrease number of flowers left.
```
flowerbed[i] = 1
n -= 1
```

However the first and last iterations wont have any spots on one side of them. So we need special checks for those too.

If `i` is 0, only check on the right side.
```
if i == 0 and flowerbed[i+1] == 0:
  flowerbed[i] = 1
  n -= 1
```

If `i` is at the end, only check on the left side
```
if i == len(flowerbed) - 1 and flowerbed[i-1] == 0:
  flowerbed[i] = 1
  n -= 1
```

So the full loop should look like this:
```
for i in range(len(flowerbed)):
  if flowerbed[i] == 0:
    if i == 0 and flowerbed[i+1] == 0:
      flowerbed[i] = 1
      n -= 1
    elif i == len(flowerbed) - 1 and flowerbed[i-1] == 0:
      flowerbed[i] = 1
      n -= 1
    elif flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
      flowerbed[i] = 1
      n -= 1
```
