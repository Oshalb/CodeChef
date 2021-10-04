# Find a substring in a string of binary numbers

def find_substring(s):
    if "101" in s:
        return "Good"
    elif "010" in s:
        return "Good"
    else:
        return "Bad"


if __name__ == "__main__":
    number_of_testcases = int(input())
    result = []
    for _ in range(number_of_testcases):
        string_to_check = str(input())
        result.append(find_substring(string_to_check))
    print(*result, sep='\n')
