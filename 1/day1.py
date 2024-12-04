import re
#init
a1 = []
a2 = []
t  = 0
#####
def read_in():
    regex = r"(\d+)\s+(\d+)"
    with open("/Users/timo/Documents/code/advent_of_code/input.txt", "r") as f:
        lines = f.readlines()
        print(f"[i] filling a1 and a2 from input.txt...")
        for line in lines:
            line = line.replace("\n", "")
            numbers = re.search(regex, line)
            a1.append(int(numbers.group(1)))
            a2.append(int(numbers.group(2)))
        print(f"[i] size of a1: {len(a1)}")
        print(f"[i] size of a2: {len(a2)}")
        a1.sort()
        a2.sort()

def diff(a1,a2):
    if a1>a2:
        return a1-a2
    elif a1<a2:
        return a2-a1
    elif a1==a2:
        return 0

def main():
    global t
    read_in()
    for i in range(len(a1)):
        difference = diff(a1[i],a2[i])
        t         += difference
    return t

if __name__ == "__main__":
    print(main())
