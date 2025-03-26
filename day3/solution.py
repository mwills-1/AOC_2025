import re

def get_data(file):
    res = []
    for line in file:
        res.append(line)
    return res

def multiplications(input):
    mults = []
    sum = 0
    for line in input:
        mults.append(re.findall(r"mul\(\d+,\d+\)", line))
        
    for mult in mults:
        for command in mult:
            nums = re.findall(r"\d+", command)
            sum += int(nums[0]) * int(nums[1])
    return sum

def do_dont_mult(input):
    mults = []
    sum = 0

    for line in input:
    # mults.append(re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)","xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"))
         mults.append(re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line))
   
    for commands in mults:
        do = True
        for command in commands:
            if command == "do()":
                do = True
            elif command == "don't()":
                do = False
            else:
                if do:
                    nums = re.findall(r"\d+", command)
                    sum += int(nums[0]) * int(nums[1])
            
    return sum
    

if __name__ == "__main__":
    with open("p3_input.txt") as file:
        data = get_data(file)
    
    result1 = multiplications(data)
    print(result1)

    result2 = do_dont_mult(data)
    print(result2)
    