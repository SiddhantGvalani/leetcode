# Problem Statement
Given an originally sorted array, now rotated 1 to n times, find minimum in array in O(logn) time

# Solution
What does it mean for the array to be rotated?
Shifting indices to the right n times where n belongs to set (0,length(array))

Finding the solution in o(n) time is too trivial. So the next best is o(logn) where we eliminate half the size of the input array at each every iteration.
We create 3 pointers: low, mid and high pointing to the first, middle and final index of input array respectively. At each iteration we must eliminate HALF THE REMAINING SIZE OF ARRAY. 
That is what "log to the base 2" means. So update low and high depending on which half besides mid we wish to eliminate.

Notice there is at least one half that is always sorted after as many rotations. So if an element is smaller than mid, we keep the half it is enclosed in. If an element is larger than mid, we discard the half it is enclosed in. To reitirate, our goal is to find minimum of array.

