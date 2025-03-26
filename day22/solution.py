def get_data (file):
    nums = []
    for line in file:
        nums.append (int (line))

    return nums


def mix (a, b):
    return a ^ b


def prune (a):
    return a % 16777216


def calc_next_num (num):
    step1 = prune (mix (num, num * 64))
    step2 = prune (mix (step1, step1 // 32))
    step3 = prune (mix (step2, step2 * 2048))

    return step3

def problem_1 (nums):
    sum = 0

    for num in nums:
 
        for _ in range (2000):
            #print (num)
            num = calc_next_num (num)
        #print (num)
        sum += num

    return sum
if __name__ == "__main__":
    with open ("p22_input.txt", "r", encoding = "utf-8") as f:
        nums = get_data (f)

    print (problem_1 (nums))
    