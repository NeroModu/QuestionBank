# Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2<sup>31</sup>,  2<sup>31</sup> − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

https://leetcode.com/problems/reverse-integer/

## Solution

Here we're simulating computer logic. Internally, integers are stored in a series of bits, Since a 32 signed integer has 32 bits, and each bit can be a 1 or a 0, each one can hold values of up to 2<sup>31</sup>. (minus one to hold the +/- symbol).

However since python is as far from internal computer logic as you can get, this won't look very technical. We still should avoid doing something too high level like ordering each digit in a list and then reversing it though.

So first we make a new int to hold our reversed value.
```
rev = 0
```

Then we enter a loop to incrementally remove each digit from our input (`x`) and add it to `rev`.
```
while x > 0:
```

Inside each iteration, we first divide `x` by 10, get the remainder, and store it in a temp int.
```
a = x % 10
```

Then we multiply `rev` by 10, and add the remainder.
```
rev = rev * 10 + a
```

When we took the remainder, we actually wanted the division by 10 to happen, since we are done with that digit. (And to decrement `x` so we can eventually leave the loop).
```
x = x // 10
```
The `//` just means it keeps `x` as an integer and doesn't convert it to a float.

Eventually we will exit the loop. Now we have a reversed number. However, if this were to be happening at an internal, lower level process, then `rev` might become too large to store in 32 bits. (987654321 is much bigger than 123456789, for example).

We remedy this by simply checking if `rev` is greater than 2<sup>31</sup> − 1.
```
if abs(rev) > 2 ** 31 - 1:
  return 0
```

We are almost done. The last thing we need to account for is negative numbers. Normally, signed ints use the first bit to hold a positive or negative sign to indicate a number's +/-, so we would only compare and reverse bits 2 thru 32. But unfortunantly in python we need to compare digits rather than bits.

So we just check if `x` is negative at the start. If it is, we make note of that, then turn it positive.
```
neg = False
if x < 0:
  neg = True
  x *= -1
```

And then if `x` was not negative, we return `rev`. If it was negative, we return negative `rev`.
```
return rev if not neg else rev * -1
```
