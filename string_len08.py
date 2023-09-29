def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    a=len(s)
    if a%2==1:
        return s[(a)//2]
    else :
        return s[a//2-1:a//2+1]
print(main("abcdfg"))
print(main("abcdf"))
print(main("cool"))