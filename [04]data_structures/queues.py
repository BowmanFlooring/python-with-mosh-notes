#       10#       20#       30#       40#       50#       60#       70#       80
# Queues

# Another data structure in Python is 'queues'. When compared to the 'stacks'
# data structure we just learned about in the last lecture, it's behavior is
# quite similar. Instead of 'last in - first out', queues model more of a 
# real-world model: FIFO (first in - first out). For example, think of a line
# at the BMV, or a wait at a restaurant. The first customers in line are the
# first ones that get seated, or waited, or helped - call it however necessary.

# Again, this is more of a 'real-world' model. And, just like stacks, we can use
# a list to represent a queue in Python. So, let's say we have a queue of items,
# we'll go with 3. If we want to remove an item from this list, we need to
# remove it from the beginning. With only a few items in the list, no problem.
# But pretent we have 10,000 items in the list - from the perspective of your
# computer's memory, all 9,999 of the remaining list items now need shifted over
# by one position. That's a lot of items to move! So that's not efficient.

# For the sake of efficiecy, we need to use a 'deque' object. Let's import deque
# (deque is a 'class') from the 'collections' module (we will go over modules in
# a future lecture, so don't worry if this part doesn't make sense yet).
from collections import deque

# Instead of setting a variable to an empty list, we should wrap the list with
# a 'deque' object and pass our list an an argument, like:
queue = deque([])

# This 'deque' object has similar methods to the 'list' object. So, let's begin
# by adding a few items to the list. We do that with the 'append' method:
queue.append(1)
queue.append(2)
queue.append(3)

# Let's check out our new queue:
print(queue)
"""
RESULT:
deque([1, 2, 3])
"""
# Nice! Now, if we want to remove an item from the beginning of the list, we use
# the deque's 'popleft' method. This 'popleft' method is NOT a method of the 
# 'list' object - hence the use of 'deque' in this situation:
queue.popleft()

# Let's see what our list looks like now:
print(queue)
"""
RESULT:
deque([2, 3])
"""
# Also similar to 'lists', we can easily check to see if our queue is empty by
# using the 'not' operator:
if not queue:
    print("empty")
