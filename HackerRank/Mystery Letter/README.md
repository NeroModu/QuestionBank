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
