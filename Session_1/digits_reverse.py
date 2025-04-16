def reverse_number_main(number):
    """
    Reverses the digits of the given number.

    Args:
        number (int): The number to reverse.

    Returns:
        int: The reversed number.
    """
    is_negative = number < 0
    number = abs(number)
    reversed_number = int(str(number)[::-1])
    return -reversed_number if is_negative else reversed_number


def reverse_number(number):
    """
    Reverses the digits of the given number.

    Args:
        number (int): The number to reverse.

    Returns:
        int: The reversed number.
    """
    is_negative = number < 0
    number = abs(number)
    reversed_number = int(str(number)[::-1])
    return -reversed_number if is_negative else reversed_number

# Example usage
if __name__ == "__main__":
    num = 12345
    print(f"Original: {num}, Reversed: {reverse_number(num)}")
    num = -6789
    print(f"Original: {num}, Reversed: {reverse_number(num)}")