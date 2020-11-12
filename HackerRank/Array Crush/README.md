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
```
arr = [0] * (n + 1)
```

Now we loop through all the queries.
```
for q in queries:
```

Next we loop through the range given by `a` and `b`. (`q[0]` and `q[1]`).
```
for i in range(q[0], q[1]+1):
```

Then we simply increment that spot in our array by `k` (`q[2]`).
```
arr[i] += q[2]
```

Once outside the loop, we need to get the largest element in our array. One easy way to do this is to sort it, then return the first element.
```
arr.sort(reverse=True)
return arr[0]
```

And thats it! We've completed the probl-

#### Error!
##### Terminated due to timeout.

What? How long are these test cases?

Well maybe that's what makes this problem hard. Potential solution: Don't use nested for loops.

We should probably optimize this code somehow to not run in `O(n^2)` time.


