# Time Delta
When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

`Day dd Mon yyyy hh:mm:ss +xxxx`

Here `+xxxx` represents the time zone. Your task is to print the absolute difference (in seconds) between them.

Input Format:
* The first line contains `T`, the number of testcases.
* Each testcase contains 2 lines, representing time `t1` and time `t2`

Constraints:
* input contains only valid timestamps
* year <= 3000

Output Format:
* Print the absolute difference (`t1 - t2`) in seconds.

Sample Input:
```
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
```

Sample Output:
```
25200
88200
```

https://www.hackerrank.com/challenges/python-time-delta/problem

## Solution

```
t1 = t1.split()[1:]
t2 = t2.split()[1:]
```

```
months = {
  'Jan': 31,
  'Feb': 28,
  'Mar': 31,
  'Apr': 30,
  'May': 31,
  'Jun': 30,
  'Jul': 31,
  'Aug': 31,
  'Sep': 30,
  'Oct': 31,
  'Nov': 30,
  'Dec': 31
}
```

```
months = {
  'Jan': 0,
  'Feb': 31,
  'Mar': 59,
  'Apr': 90,
  'May': 120,
  'Jun': 151,
  'Jul': 181,
  'Aug': 212,
  'Sep': 243,
  'Oct': 273,
  'Nov': 304,
  'Dec': 334
}
```
