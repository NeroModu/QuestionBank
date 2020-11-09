# 20. Valid Parenthesis
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

* Open brackets must be closed by the same type of brackets.
* Open brackets must be closed in the correct order.

https://leetcode.com/problems/valid-parentheses/

## Solution
This problem asks you to parse parenthesis, checking if, hypothetically, a language interpreter would be able to make sense of them.

As you comb through the chars in the given string, you're checking if the current closing parenthesis matches up with the last opened one. And therefore the best approach for this is to use a stack. As new paranthesis are opened, they are added to the stack. When a closing parenthesis is found, the most recently added parenthesis is popped from the stack, and them compared to the current one. If they match up, great. Continue. If they don't, the parenthesis are not valid.

So to start, first we initialize a stack. Python doesn't natively have a stack object, but the built in list will do just fine.
```
stack = []
```

Then we loop through every character in the string.
```
for c in s:
```

C is now our working char. This is what we will investigate at every iteration. Now we first add a check to see if it's an opening parenthesis. If it is, we add it to the stack and continue.
```
if c == '(' or c == '[' or c == '{':
  stack.append(c)
 ```
 
But if it's a closing parenthesis, we give the stack a pop to remove the top element, and compare it with our current parenthesis's opening counterpart. If they don't match up, we have a problem. So we return False.
```
elif c == ')':
  curr = stack.pop()
  if curr != '(':
    return False
```

Remember to include checks for other types of parenthesis (`[`, `{`).

Now, if we reach the end of our loop, it means that all parenthesis are valid so far, since no `return False` has been tripped. But there could still be an opening parenthesis or two at the end that have no closing parenthesis, which is invalid. This is an easy check however. Just check if the stack is empty.
```
if len(stack) > 0:
  return False
```

We are almost done. The last thing we need to worry about is the case that right from the beginning we hit a closing parenthesis. If there is nothing on the stack, and we try to pop, we'll get an error. To remedy this just put a filler element in the stack. It can be anything, as long as it serves the purpose of keeping at least one element in the stack at all times.
```
stack = ['x']
```

Lastly don't forget to account for that extra element in your length check.
```
if len(stack) > 1:
  return False
```

And so, if we reach this point in the function without triggering a Return False, then we know the parenthesis in the given string are valid. We can exit the function now.
```
return True
```
