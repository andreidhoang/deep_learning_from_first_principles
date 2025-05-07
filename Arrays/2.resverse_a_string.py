def reverse(str):
    """
    This function takes a string as input and returns the string in reverse order.
    """
    return str[::-1]

def reverse2(str):
    """
    This function takes a string as input and returns the string in reverse order.
    """
    reversed_str = []
    for i in range(0, len(str)):
        char = str[len(str) - i - 1]
        reversed_str.append(char)
    reversed_str = ''.join(reversed_str)
        
    return reversed_str



string = "Hello, World!"
reversed_string = reverse2(string)
print(reversed_string)  # Output: !dlroW ,olleH