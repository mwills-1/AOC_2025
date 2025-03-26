def get_lists(file):
    left_lst = []
    right_lst = []
    sum = 0

    for line in file:
        numbers = line.strip().split('   ')
        left_lst.append(numbers[0])
        right_lst.append(numbers[1])
    left_lst.sort()
    right_lst.sort()

    return left_lst, right_lst

def list_distances(lst1, lst2):
    sum = 0
    for left, right in zip(lst1, lst2):
        sum += abs(int(left) - int(right))

    return sum

def similarity_score(left, right):
    num_count = {}
    sum = 0

    for val in right:
        num_count[val] = num_count.get(val, 0) + 1
    
    for val in left:
        sum += int(val) * num_count.get(val, 0)
    
    return sum

if __name__ == "__main__":
    with open("p1_input.txt") as file:
        left, right = get_lists(file)

    result = list_distances(left, right)
    print(result)

    result = similarity_score(left, right)
    print(result)
