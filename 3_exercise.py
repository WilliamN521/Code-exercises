
if __name__ == '__main__':
    s = input("enter string: ")
    alphaNumeric = alpha = digit = lower = upper = False

    for i in s:
        alphaNumeric = alphaNumeric or i.isalnum()
        alpha = alpha or i.isalpha()
        digit = digit or i.isdigit()
        lower = lower or i.islower()
        upper = upper or i.isupper()

    print(alphaNumeric)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)