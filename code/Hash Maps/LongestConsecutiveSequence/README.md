# Problem Statement
Given integer array, return length of longest consecutive sequence

# Solution
How do we identify a sequence?
A sequence, in mathematics, is a list of numbers spaced with a common difference. In this problem, the common difference is 1.
<pre>
Example) Input: nums = [2,20,4,10,3,4,5]
         Output: 4 because 2,3,4,5 is a sequence with CD(common difference) = 1
</pre>
Let's traverse nums and identify the START of a sequence. In this problem, the start of a sequence would be an integer, which when decremented by CD, does not exist in input array. We need to create a hash set, and append the sequence heads into the set.For example,
<pre>
index = 0, element is 2. Does 1 exist in nums? No. 2 is one sequence head.
We must check if (sequence head + common difference) exists in set whilst incrementing cd at each iteration. 
We store this sequence length and compare it to any other sequences in nums.
</pre>
