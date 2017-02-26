# manu_bitstrings
Find all bit strings with no consecutive 0s
-------------------------------------------------------------------
The solution to above problem is __Nth term of the fibonacci sequence__.

## Explanation:
---
Suppose A represents all even bit strings (i.e ending with 0)
Suppose B represents all odd bit strings (i.e ending with 1)

If we don't know the answer and start writing down all possibilities (for say n = 3)
& represent the three positions of our length-3 bit string as __ __ __ :

We will see that if a position is filled with 0, the next position can be filled
with only 1 and if it is filled with 1, the next position can be filled by either
0 or 1.

Following above statement:

We get out recurrence relation as:

A(n) = A(n -1) + B(n -1)<br>
B(n) = A(n - 1)

Which is nothing but the very familiar __fibonacci sequence!__

## Testing the solution:
---

Just run the file with command <code>python manu.py</code> and see the results.
