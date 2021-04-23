"""Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
The function should return true if the string is valid, and false if it's invalid."""


def valid_parentheses(string):
    amount = 0
    for char in string:
        if amount != -1:
            if char == "(":
                amount += 1
            elif char == ")":
                amount -= 1
        else:
            return False
    return amount == 0


print(valid_parentheses(")test"))        #False
print(valid_parentheses("hi(hi)()"))     #True
print(valid_parentheses("    ("))        #False