# 3. Drawing Patterns with Nested Loops

size = int(input("Enter the size of the pattern: "))

i = 0
while i < size :
    for row in range(0, size-1):
            print("*", end="")
            
    print("*")
    i += 1