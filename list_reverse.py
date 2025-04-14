def list_reverse(input_list):
    """
    Reverses the given list.

    Args:
        input_list (list): The list to be reversed.

    Returns:
        list: A new list that is the reverse of the input list.
    """
    return input_list[::-1]

# Example usage
if __name__ == "__main__":
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = list_reverse(sample_list)
    print("Original List:", sample_list)
    print("Reversed List:", reversed_list)