a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter a third number: "))

# Logical operators: and, or, not
# and operator: returns True if both conditions are true
if a < b and b < c:
    print("Both conditions are true.")
# or operator: returns True if at least one condition is true
if a < b or b > c:
    print("At least one condition is true.")
# not operator: returns the opposite of the condition
if not a > b:
    print("a is not greater than b.")
