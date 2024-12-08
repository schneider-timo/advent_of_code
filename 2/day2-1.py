def check(array):
    inc = all(array[i] < array[i+1] for i in range (len(array)-1))
    dec = all(array[i] > array[i+1] for i in range (len(array)-1))
    
    if not (inc or dec):
        return 0
    
    for i in range(len(array)-1):
        diff = abs(array[i] - array[i+1])
        if diff > 3 or diff < 1:
            return 0
    
    return int(1)

def read_input():
    safe = 0
    with open("input2.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("\n", "")
            line = line.split(" ")
            line = list(map(int,line))
            safe += check(line)
            print(safe)
if __name__ == "__main__":
    read_input()
