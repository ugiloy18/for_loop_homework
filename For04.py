def main(A,B):
    """
    Return the numbers from A to B in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    result = []
    for i in range(A + 1):
        result = result + [i]
    return result
print(main('B'))