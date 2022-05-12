"""
This is a simple python program to generate a fibonacci sequence from a 
number that the user selects, and makes the sequence as long as the user
wants
"""

# welcome the user
print("Welcome to Ugo's Fibonacci Sequence App\n\n")

# create a small loop that ensures the user enters a whole number or decimal
#  as the starting point
start = 0
while start == 0:
    try:
        start = float(input("What number do you want to start from?: "))
    except:
        start = 0
    else:
        break

# create a small loop that ensures the user enters a whole number or decimal
#  as the number of steps of the sequence
steps = 0
while steps == 0:
    try:
        steps = int(input("How many numbers do you want in this sequence?: "))
    except:
        steps = 0
    else:
        break

# create the list that will continue the sequence
sequence = []

# create a counter
i = 0
while i <= steps:
    if len(sequence) <= 1:
        sequence.append(start)
    else:
        # add the last number on the list to the one before it
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    i+=1
    
# print out the sequence
for s in sequence:
    print(s)
    
