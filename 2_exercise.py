
# Function
def count_substring(string, sub_string):
    count = 0

    for i in range(len(string)):
        sub = string[i:i+len(sub_string)]
        if sub == sub_string:
            count += 1
    # total
    return count

# ABCDCDC
# CDC


if __name__ == '__main__':
    string = input("Enter String: ")
    subString = input("Enter SubString: ")
    print(f"Number of appearances: {count_substring(string, subString)}")



