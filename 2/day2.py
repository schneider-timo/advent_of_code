import re

#init
a1 = []
a2 = []
sim_score  = 0
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

def main():
    global sim_score
    read_in()
    for e1 in a1:
        c = 0
        for e2 in a2:
            if e1 == e2:
                c += 1
        sim_score += e1*c
    return sim_score23655822

if __name__ == "__main__":
    print(main())
