# Function
def camelcase(string):
    count = 1
    for i in string:
        if i.isupper():
            count += 1
    return count

# Execution
if __name__ == '__main__':
    string = input("Enter String: ")
    print(f"Number of words: {camelcase(string)}")
