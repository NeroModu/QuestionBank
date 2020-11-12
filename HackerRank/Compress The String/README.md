# Compress The String!
In this task, we would like for you to appreciate the usefulness of the `groupby()` function of `itertools`. To read more about this function, [Check this out](https://docs.python.org/2/library/itertools.html#itertools.groupby).

You are given a string `S`. Suppose a character `c` occurs consecutively `X` times in the string. Replace these consecutive occurrences of the character `c` with `(X, c)` in the string.

For a better understanding of the problem, check the explanation.

Input Format:
* A single line of input consisting of the string `S`.

Output Format:
* A single line of output consisting of the modified string.

Constraints:
* All the characters of `S` denote integers between 0 and 9.

Sample Input:
```
1222311
```

Sample Output:
```
(1, 1) (3, 2) (1, 3) (2, 1)
```

Explanation:
First, the character `1` occurs only once. It is replaced by `(1, 1)`. Then the character `2` occurs three times, and it is replaced by `(3, 2)` and so on.

Also, note the single space within each compression and between the compressions.

https://www.hackerrank.com/challenges/compress-the-string/problem

## Solution
Okay they want us to use `groupby()`. What does that even do? I've never used this method before, but id assume it groups duplicate elements together if it's supposed to help us at all.

I came across [this article](https://www.quora.com/How-can-we-use-itertools-groupby-in-Python-3) that explains it pretty clearly. Who knew quora would ever come in handy?

Anyway so it seems like we need to build tuples for every series of repeating ints. Lets start by making an empty list to hold all our tuples.
```
encodings = []
```

Now we use `groupby()`. (BTW `line` refers to the input)
```
for group, items in itertools.groupby(line):
```

The function seems to give us a common element (`group`) and a list of its repeated contents (`items`). We don't need this list, since we're only being asked for the ammount of times they repeat.

So lets get the length.
```
length = len(items)
```
#### Error!
##### TypeError: object of type 'itertools._grouper' has no len()

Oops! What the hell is an `itertools._grouper`?

Okay so this works.
```
length = len(list(items))
```

Now we can build our tuple and add it to our list of them.
```
compression = (length, group)
encodings.append(compression)
```
Now we exit the loop and start a new one. This time we loop thru our list of tuples, printing each one like they want us to.
```
for tup in encodings:
  print(tup, end=' ')
```
The `end=' '` specifies not to put a newline after each one.

#### Wrong Answer!
##### Your output: `(1, '1') (3, '2') (1, '3') (2, '1')`
##### Expected: `(1, 1) (3, 2) (1, 3) (2, 1)`

Well damn.

Since our input line was a string, the grouping keys are all strings. We'll just have to format it manually.
```
tup_formatted = "({0})".format(', '.join(map(str, tup)))
print(tup_formatted, end=' ')
```
...y'know, as one does.

And that seems to work!

#### Congratulations!
##### Your output: `(1, 1) (3, 2) (1, 3) (2, 1)`
##### Expected: `(1, 1) (3, 2) (1, 3) (2, 1)`
