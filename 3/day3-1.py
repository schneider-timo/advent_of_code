import re

def scan(data,mul):
    matches = re.findall(mul, data)
    solution = 0
    for match in matches:
        numbers = re.findall(r"(\d+)", match) 
        multiplication = int(numbers[0]) * int(numbers[1])
        solution += multiplication
    return solution

def read_in():
    with open("input3.txt", "r") as f:
        data = f.read()
    return data

if __name__ == "__main__":
    mul = r"mul\(\d+,\d+\)"
    data = read_in()
    solution = scan(data,mul)
    print(solution)
