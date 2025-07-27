def main(n):
    """
    Return numbers from zero to n in a list view.
    Args:
        n: int
    Returns:
        list: return  answer
    """
    result = []
    for i in range(n + 1):
        result = result + [i]
    return result
print(main(5))
