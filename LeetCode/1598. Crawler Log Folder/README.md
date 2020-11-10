# Crawler Log Folder
The Leetcode file system keeps a log each time some user performs a change folder operation.

The operations are described below:

* "../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
* "./" : Remain in the same folder.
* "x/" : Move to the child folder named x (This folder is guaranteed to always exist).
You are given a list of strings logs where logs[i] is the operation performed by the user at the i<sup>th</sup> step.

The file system starts in the main folder, then the operations in logs are performed.

Return the minimum number of operations needed to go back to the main folder after the change folder operations.

## Solution
This might seem like a stack problem, but since the folder names don't matter, you only need a counter. Start it at 0.
```
count = 0
```

Then loop thru the strings in the given list.
```
for op in logs:
```

If the operation is `'../'`, and if the counter is not at 0, decrement the counter.
```
if op == '../':
  if count != 0:
    count -= 1
```

If the operation is `'./'` then we do nothing.

If the operation is anything else ending with `/` (but not `./`) then we increment the counter. To check for this we see if the string contains a `/` but not a `.`.
```
elif '/' in op and '.' not in op:
  count += 1
```

Then just `return count`
