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
Python has a built in datetime library built for literally this. But thats no fun. Lets do it ourselves.

So we're asked to find the difference between two times, in seconds. Now, we could individually compare each date's year, month, day, hours, minutes and seconds, then convert them all to seconds. But if you're gonna convert to seconds eventually, wouldn't it make more sense to just do that from the start, then take the difference?

Yeah so lets do that. First lets parse the input. It's given as `Day dd Mon yyyy hh:mm:ss +xxxx`, so its convenient to `split()` the parts into an array. Also we don't need the day of the week, so we splice that first element out.
```
t1 = t1.split()[1:]
t2 = t2.split()[1:]
```

Now we'll need to convert the one string element, the month. Lets make a dictionary with the ammount of days in each month.
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

But wait... If a date is, lets say, in the middle of August, why would we want *all* the days in Aug? What we need is the total number of days up until Aug. Then we can add that to our days, and hours, and etc. We *could* then take the days in July and loop backwards adding the days in June, and May, and April, etc. But wouldn't it be much more convenient if we simply stored that information in the dict?

Behold, a dictionary with all the days leading up to each month:
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

Okay now lets deal with the time portion. ("hh:mm:ss")
```
t1_Time = t1[3].split(':')
t2_Time = t2[3].split(':')
```
But we want the hours, minutes and seconds to be ints, not strings.
```
t1_Time = [int(i) for i in t1[3].split(':')]
t2_Time = [int(i) for i in t2[3].split(':')]
```
Thats better.

Now we begin our count. Vars `t1_Seconds` and `t2_Seconds` will hold the running totals.
```
# [hh, mm ss]
#  0   1   2
#                secs   |   mins (60 secs)  |  hours (3600 secs)
t1_Seconds = t1_Time[2] + (t1_Time[1] * 60) + (t1_Time[0] * 3600)
t2_Seconds = t2_Time[2] + (t2_Time[1] * 60) + (t2_Time[0] * 3600)
```

Lets add up the seconds in the days. (index 0 in `t1` & `t2`)
```
# 1 day = 86400 seconds
t1_Seconds += int(t1[0]) * 86400
t2_Seconds += int(t2[0]) * 86400
```

Next the months. (index 1 in `t1` & `t2`) We can get the days up till our current month from our dictionary.
```
t1_Seconds += months[t1[1]] * 86400
t2_Seconds += months[t1[1]] * 86400
```

Now the year. (index 2)
```
t1_Seconds += int(t1[2]) * 86400 * 365
t2_Seconds += int(t2[2]) * 86400 * 365
```

We also need to keep in mind leap years. Lets write a function for that.
```
def is_leap(year):
    leap = False
    if (year % 100 == 0) and (year % 400 != 0):
        leap = False
    else:
        if year % 4 == 0:
            leap = True
        else:
            leap = False

    return leap
```
So we now need to add another day (86400 seconds) to our counts if both the year is a leap year and the month is after February. We first check if Feb has passed.
```
t1_isAfterFeb = t1[1] != 'Jan' and t1[1] != 'Feb'
t2_isAfterFeb = t2[1] != 'Jan' and t2[1] != 'Feb'
```
Then we add 86400 if it's a leap year and after Feb. Otherwise don't add anything.
```
t1_Seconds += 86400 if (is_leap(int(t1[2])) and t1_isAfterFeb) else 0
t2_Seconds += 86400 if (is_leap(int(t2[2])) and t2_isAfterFeb) else 0
```

Lastly we need to add or subtract the timezone difference. Lets write a function to parse it.
```
def parse_timezone(sxxxx):
    hours = sxxxx[1:3]
    minutes = sxxxx[3:]
    sign = -1 if sxxxx[0] == '+' else 1
    
    seconds = (int(minutes) * 60) + (int(hours) * 3600)
    return seconds * sign
```
And then we just add/subtract the corresponding ammont of seconds.
```
t1_Seconds += parse_timezone(t1[4])
t2_Seconds += parse_timezone(t2[4])
```

Lets get the difference now.
```
difference = abs(t1_Seconds - t2_Seconds)
```

aaaand send it.
```
return difference
```
