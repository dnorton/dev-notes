"""a collection of interesting python snippets"""

# just to satisfy my curiousity, I tried to figure out how to print 1 to 10 in python
# This is a fairly convoluted way to do it. Note, in 2.x print is a statement
# so I had to import the 3.x print() function
map(lambda x: print(x+1), range(10))
