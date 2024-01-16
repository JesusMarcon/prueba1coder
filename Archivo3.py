import collections as cl 

# empty counter 
counter = cl.Counter()
print(counter) #counter()

#counter with initial values
counter = cl.Counter(["a","c","a","b","c","b","b","b","c"])
print(dict(counter))

counter = cl.Counter (a=2, b=3, c=1)
print(counter) #counter ({"b":3, "a":2, "c";1})