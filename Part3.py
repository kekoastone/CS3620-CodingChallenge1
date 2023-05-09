# Using a for-loop and a range function, print "I am a programmer" 5 times.
# Create a function that displays out the square values of numbers from 1 to 9.
a = range(0, 5)
for i in a:
    print("I am a programmer")
    i += 1


def square_value():
    value = range(1, 10)
    for j in value:
        print(j**2)
        j += 1


square_value()
