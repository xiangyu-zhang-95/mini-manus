def count_char(input_string, char):
    """
    Count how many times a specific character appears in a string.
    
    Args:
        input_string (str): The string to search in
        char (str): The character to count
        
    Returns:
        int: The number of occurrences of the character in the string
    """
    count = 0
    for c in input_string:
        if c == char:
            count += 1
    return count

# Test the function with some examples
print(count_char("hello world", "l"))  # Should return 3
print(count_char("programming", "m"))   # Should return 2
print(count_char("banana", "a"))       # Should return 3
print(count_char("python", "z"))       # Should return 0