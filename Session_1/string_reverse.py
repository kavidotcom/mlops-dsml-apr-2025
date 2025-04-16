def reverse_string_v1(input_string):
    """
    Reverses the given string and returns the result.
    
    Args:
        input_string (str): The string to reverse.
    
    Returns:
        str: The reversed string.
    """
    return input_string[::-1]

# Example usage
if __name__ == "__main__":
    sample_string = "Hello, World!"
    print("Original String:", sample_string)
    print("Reversed String:", reverse_string(sample_string))