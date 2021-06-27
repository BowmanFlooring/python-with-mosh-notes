#11111111 111111111 111111111 111111111 111111111 111111111 111111111 111111111#

# Stacks

# In Python, Stacks work kind of like a stack of books in the physical
# world - the last book that you put on the top of the stack, is the
# first book that you can remove. This is called:
#
#                   *LIFO - Last In, First Out*
#
# A good real world example of this is your browser. Your browser
# keeps your browsing session in a stack. You can press the back
# button to recall the last item in the stack (navigate back a page).

# This stack of webpages can be represented with a bracketed list. for
# simplicity, we will use integers. In an actual model, they would be
# represented as strings - the strings being the URL. So here it is:

[]

# We have jsut opened our browser, so we just have an empty list. Let's
# go to our first webpage:

[1]

# How about a couple more...:

[1, 2, 3]

# Our browser has put our webpages in a stack, with the last page at the
# end of the stack - in this case it's represented with the number 3.
# Now let's hit the back button to go back a page:

[1, 2]

# Now, let's hit the back button two more times...:

[]

# At this point, our browser would simply disable the back button. This
# is how a stack works! But, how does the code look? How would we build
# a stack?

# We know a stack is a list. So, let's create a variable, and set it to
# an empty list:

browsing_session = []
# To add to the list, we use the 'append' method to add the current page:
browsing_session.append(1)
# Now let's say the user navigates to a couple more webpage:
browsing_session.append(2)
browsing_session.append(3)
# Let's see what that looks like:
print(browsing_session)
'''
RESULT:
[1, 2, 3]
'''

# As you can see, each 'URL' (here, represented as integers) has been
# structured into a stack. Now, when the user presses the back button,
# how do we remove the last item in the list? Well, we learned in a
# previous lecture about the 'pop' method. Let's try that here, and then
# set it to a conveniently-named variable:

last_page = browsing_session.pop()
# Then, of course, print the result:
print(last_page)
'''
RESULT:
3
'''
# Now, let's print our stack one more time, juuuuuust to be sure.. :) :
print(browsing_session)
'''
RESULT:
[1, 2]
'''
# As you can see, our last item was removed from the stack! So, to make
# sure the user navigates to their previous page, we need to display
# the top of the stack. We can get that very easily - we know that the
# 'index' of the last item in a list can be called with [-1]. So, no
# natter how big the stack, we don't need to know the actual index of
# that item - we only need to know it's position RELATIVE to the entire
# stack. That's why [-1] is always appropriate, and most effecient, in
# retreiving that last list/stack item.

print(browsing_session[-1])
# A label can also be added, simply for clarity:
print("redirect", browsing_session[-1])
'''
RESULT:
redirect 2
'''

# We also need to check if the stack is empty, that way we can disable
# the back button when there are no more pages to navigate back to.
# ---------------------------------------------------------------------------
# Early on in the course, we learned about what Python calls 'Falsy' values.
#
#    *remember!* There are only THREE 'Falsy' values:
#           1. 0  <-- the integer 'zero'
#           2. "" <-- empty strings
#           3. [] <-- empty lists

# Using that knowledge, we can make the task at hand quite simple. If we just
# apply the 'not' operator to an empty list, the 'not' statement will REVERSE
# it's value - thus, making the expression TRUE. Here's how that looks:

if not browsing_session:
    print("disable")

# So, let's recap everything quickly, and in the correct order:

# We use the 'append' method to add an item on TOP of the stack.
# We use the 'pop' method to REMOVE the top item from the stack.
# We use 'index -1' to RETRIEVE the item on the top of the stack.
# And, of course, before doing that, we check to see if stack is empty.
# The stack CANNOT be empty when running this step in the code.
# You'll get an error!! Here it is now, all together:

browsing_session = []
browsing_session.append()
browsing_session.pop()
if not browsing_session:
    browsing_session[-1]
