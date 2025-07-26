# pattern_drawing.py

# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer while loop for rows
while row < size:
    # Inner for loop for columns
    for col in range(size):
        print("*", end="")  # Print stars in one row
    print()  # Move to next line after each row
    row += 1  # Move to the next row
