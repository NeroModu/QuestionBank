# Mystery Letter
In this task, you're given a series of words composing a letter. However, every word is encoded in a palindrome. You must figure out how many one-letter changes need to be made to every word in order to make them palindromes.

Input Format:
* A list of words, most of which are not palindromes.

Output Format:
* A list of integers, with the i<sup>th</sup> int representing how many changes must be made to the i<sup>th</sup> word in the input list.

Constraints:
* Letters can only be changed up, not down. So `b` can be changed to `a`, but not `c`.
* `0 < len(word) < 10^8`

Sample Input:
```
3 //number of words. You can ignore, only given for handler function
abc
abcd
acca
```
Sample Output:
```
2
4
0
```
Explanation: To change `abc` to `aba`, `c` must be changed to `b` then to `a` totaling 2 changes. `abcd` requires changing `c` to `b` and `d` to `c` then `b` then `a`, totaling 4. `acca` is already a palindrome so it requires 0 changes.

# Solution
So we need to make a list to hold our ints. Then we should loop through our words in the input letter. We should also keep a counter of needed conversions. At the end of this loop we'll append this counter to our list.
```python
conversions = []
for word in letter:
  total = 0
```

Now we check if the length of our word is one. Because if it is, by default it's already a palindrome and no changes need to be made.
```python
if len(word) == 1:
  conversions.append(0)
  continue
```

Now comes our actual algorithm. The simplest way to do any palindrome anaysis is to compare the first and last chars, then the second and second to last, then the third and third to last, etc... We check if they are the same, or rather how far apart they are, and record that difference, then move on to the next two. We stop when the chars we're comparing overlap.

So lets start by making start and end pointers. (Not really pointers, but we use them to reference the n<sup>th</sup> char.)
```python
start = 0
end = len(word) - 1
```

Now we define a while loop that ends when our start pointer grows bigger than our end one.
```python
while start < end:
```

Inside this loop we now need to grab the numeric value of our chars in question. We can do this with the ASCII function `ord()`. These two numeric representations can now tell us the ammount of changes needed to palindromize this part of the word. And all we need is the difference between the two. It doesn't even matter which one we need to change, since the question isn't asking us to return any solved strings. (Otherwise we would have to ensure the larger char is the one being changed.) So lets do that.
```python
startChar = ord(word[start])
endChar = ord(word[end])
difference = abs(startChar - endChar)
```

Then all we need to do is add that difference to our running total for that word. We should also increment our starting spot, and decrement our ending spot.
```python
total += difference
start += 1
end -= 1
```

Now, outside the while loop we have a completed `total` that tells us the conversions needed for this word. Lets append it to our list.
```python
conversions.append(total)
```

And finally, outside our for loop we can return our list.
```python
return conversions
```
