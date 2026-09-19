def characteristic(num_string):
    """
    Extracts the characteristic (integer part) from a number string.

    Returns:
        tuple: (bool, int) - (True, characteristic) if valid, (False, 0) if invalid
    """
    int_part = num_string.split(".")[0]
    return (True, int(int_part))


def mantissa(num_string):
    """
    Extracts the mantissa (fractional part) from a number string.

    Returns:
        tuple: (bool, int, int) - (True, numerator, denominator) if valid, (False, 0, 0) if invalid
    """

    parts = num_string.split(".")

    if len(parts) == 1:
        return (True, 0, 1)

    frac_part = parts[1]
    numerator = int(frac_part)
    denominator = 10 ** len(frac_part)
    return (True, numerator, denominator)
