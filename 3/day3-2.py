import re

def scan(data,mul,control):
    allow_matching = True
    solution = 0
    for match in re.finditer(control, data):
        token = match.group(0)

        if token == "do()":
            allow_matching = True

        elif token == "don't()":
            allow_matching = False

        elif allow_matching and re.match(mul, token):
            numbers = re.findall(r"(\d+)", token) 
            multiplication = int(numbers[0]) * int(numbers[1])
            solution += multiplication
    return solution

def read_in():
    with open("input3.txt", "r") as f:
        data = f.read()
    return data

if __name__ == "__main__":
    mul = r"mul\(\d+,\d+\)"
    control = r"(do\(\)|don't\(\)|mul\(\d+,\d+\))"
    data = read_in()
    solution = scan(data,mul,control)
    print(solution)
