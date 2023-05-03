# Complete the solve function below.
def solve(s):
    string_split = s.split(' ')
    final = list()

    for word in string_split:
        if word:
            final.append(word[0].upper() + word[1:])
        else:
            final.append("")
    # output
    return ' '.join(final)


if __name__ == '__main__':
    s = input("Enter a string: ")
    print(solve(s))
