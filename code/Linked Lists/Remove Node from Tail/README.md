# Problem Statement
Given the head of a singly-linked list & an integer 'n', we need to remove the n<sup>th</sup> node from the end of the list.

# Solution
Firstly, how do we reach that n<sup>th</sup> node from the end because we know that we cannot iterate through linked lists using indices. What we do is get the size of the linked list at the very beginning using a while loop and then subtract n from the attained size. Then we can reach the (size - n)<sup>th</sup> node from the start easily. But keep in mind of constrainsts such as the node to be removed is the head of the linked list because in that case we can just return head's next pointer and exit the method. Finally, change the pointers of the (size - n)<sup>th</sup> node & its next node, which is the node to be removed. There are other methods such as a fast pointer moving n steps ahead at every loop iteration. The time & space efficiency is O(N) & O(1) respectively in any way. 
