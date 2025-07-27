def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    result = [A]
    for i in range(B + 1):
        result = result + ['B']
    return result
print(main('A'))