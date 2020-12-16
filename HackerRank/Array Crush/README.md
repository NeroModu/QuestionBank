# Crush / Array Manipulation
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array.

Example:
```
n = 10
queries = [[1,5,3], [4,8,7], [6,9,1]]
```
Queries are interpreted as follows:
```
a b k
1 5 3
4 8 7
6 9 1
```

Add the values of `k` between the indices `a` and `b` inclusive:
```
index->	 1 2 3  4  5 6 7 8 9 10
        [0,0,0, 0, 0,0,0,0,0, 0]
        [3,3,3, 3, 3,0,0,0,0, 0]
        [3,3,3,10,10,7,7,7,0, 0]
        [3,3,3,10,10,8,8,8,1, 0]
```

The largest value is `10` after all operations are performed.

Function Description:
Complete the function arrayManipulation in the editor below.
`arrayManipulation()` has the following parameters:
* int n - the number of elements in the array
* int queries[q][3] - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.

Returns:
* int - the maximum value in the resultant array

Input Format:

The first line contains two space-separated integers `n` and `m`, the size of the array and the number of operations.
Each of the next `m` lines contains three space-separated integers `a`, `b` and `k`, the left index, right index and summand.

Constraints:
```
3 <= n <= 10^7
1 <= m <= 2 * 10^5
1 <= a <= b <= n
0 <= k <= 10^9
```

https://www.hackerrank.com/challenges/crush/problem

## Solution

This problem is marked as hard, yet it seems pretty straightforward. This scares me.

Okay so we start by defining an array of 0s of size `n+1`. We need the extra one because the problem specifies the array is 1-indexed.
```python
arr = [0] * (n + 1)
```

Now we loop through all the queries.
```python
for q in queries:
```

Next we loop through the range given by `a` and `b`. (`q[0]` and `q[1]`).
```python
for i in range(q[0], q[1]+1):
```

Then we simply increment that spot in our array by `k` (`q[2]`).
```python
arr[i] += q[2]
```

Once outside the loop, we need to get the largest element in our array. One easy way to do this is to sort it, then return the first element.
```python
arr.sort(reverse=True)
return arr[0]
```

And thats it! We've completed the probl-

#### Error!
##### Terminated due to timeout.

What? How long are these test cases?

We should probably optimize this code somehow to not run in `O(n*m)` time.

Well maybe that's what makes this problem hard. Potential solution: Don't try to access every element in the array.

## New Solution

Initialize our array.
```python
arr = [0] * (n + 1)
```

Loop thru queries.
```python
for q in queries:
```

Now it gets interesting. Before we were looping through the *entire* range from `a` to `b` for every one of our queries. Since this was too slow, what we can do instead is only increment `arr[a - 1]` by `k`, then *decrement* `arr[b]` by `k`. Essentially, this changes what our array represents. Now, every non-zero value represents how the 0s between them differ from what comes before and after.

So lets do it. To clarify what each element of `q` means, lets name them.
```python
a = q[0] - 1
b = q[1]
k = q[2]
```
`a` gets one subtracted to account for the indexing starting at 1.

Now we just add `k` to `arr[a]` and subtract `k` from `arr[b]`.
```python
arr[a] += k
arr[b] -= k
```

Now we leave the loop. Next, we need to iterate down the array adding or subtracting each element to a counter. We also need to keep track of when this counter is at its highest, and return that.
```python
biggest = 0
    running_total = 0
    for i in arr:
        running_total += i
        if running_total > biggest:
            biggest = running_total
    return biggest
```

## Explanation

Lets look at this example:
```
5 3
1 2 100
2 5 100
3 4 100
```

Previously, we were doing this:
```
1) [0   0   0   0   0]
2) [100 100 0   0   0]
3) [100 200 100 100 100]
4) [100 200 200 200 100]
```
However, it turns out you do not need to update each element between the first and last. You only need to record the *change* at each start and end location. Like in the 3rd update, the only reason element 2 changes to 200 is because earlier the ending location for the update landed on that spot.

Imagine the final array instead representing something like this.
```python
300 
200    --------- 
100 ---         ---
000
     |  |  |  |  |
     1  2  3  4  5
```
What we did was modify each start and end *change* rather than cumulative total. Pretty wild stuff.
