def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    a = len(s1)
    b = len(s2)
    c = len(s3)
    if  a%2 == 0 and b%2==1 and c%2==1:
        return f"[{s3},{s2}]"
    elif a%2 != 0 and b%2==0 and c%2==0:
        return f"[{s1}]"
    if  b%2 == 0 and a%2==1 and c%2==1:
        return f"[{s1},{s3}]"
    elif b%2 == 1 and b%2==0 and c%2==0 :
        return f"[{s2}]"
    if  c%2 == 0 and b%2==1 and a%2==1:
        return f"[{s1},{s2}]"
    elif  c%2 == 1 and b%2==0 and a%2==0:
        return f"[{s3}]"
    
        
print(main( s1="code", s2="python", s3="coder"))
print(main(s1="codeschool.uz" ,s2="example" ,s3="python"))