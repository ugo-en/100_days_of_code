"""
The aim is simply to practice the use of the yield statement
"""


# function for generator
def x():
    l = [1,2,3,4,5,6,7,8,9,10]
    for i in l:
        yield i


# new generator
gen = x()

# you can loop through them
for g in gen:
    print(g)

# print blank line
print()
# another generator
gen2 = x()

# using the next keyword to iterate through
print(next(gen2))
print(next(gen2))
print(next(gen2))
