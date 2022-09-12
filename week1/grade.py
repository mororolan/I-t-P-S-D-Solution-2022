import re
def grades():
    with open ("grades.txt", "r") as file:
        grades = file.read()
    # YOUR CODE HERE
        list = re.findall('[A-Z][a-z]* [A-Z][a-z]*.: [B]', grades)
        result = []
        for i in list:
            result.append(i[0:-3])
        return result

if __name__ == '__main__':
    print(grades())
    print(len(grades()))