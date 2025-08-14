# Problem Statement
Given an originally sorted array that has been rotated 1 through n times, where n is the length of input array, find input integer Target. in o(logn).

# Solution
As always in Binary Search problems, we create 3 pointers low, mid and high pointing to the first, middle, and last indices respectively.
Let us graph the array [1,2,3,4,5,6] before and after rotation an arbitary number of times.
Before Rotation:
                  .
               .
.           . 
.        .
.     .               
.  .                   
. . . . . . .          
After Rotation:
       
.    .
.  .          .
.           .
.         .
.       .
. . . . . . . 

The graphs show that about the middle index, at least one of the halves remain sorted. So lets say we rotate [1,2,3,4,5,6] 2 times to get [5,6,1,2,3,4]
Mid will point to index 2 and notice the right half remains sorted. How about we rotate 4 times? [3,4,5,6,1,2]. Now, the left half is sorted.
But how do we know which half is sorted? right or left? If we notice a pattern: when integer at mid index is greater than 1st index, left half is sorted. Else, right half is sorted.
Then, to get to target, we need to check wether it is smaller or greater than array[mid]. Additionally, check if target is smaller than nums[mid] and eliminate halves accordingly.
