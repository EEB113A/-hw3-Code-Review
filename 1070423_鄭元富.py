from operator import index

def sort_by_occurrence(nums):
    output_nums = []
    for i in nums:
        if i not in output_nums:
            output_nums.append(i)
            for j in output_nums:
                if nums.count(i) < nums.count(j):
                    output_nums.remove(i)
                    output_nums.insert(output_nums.index(j), i)
                    break
    return output_nums

if __name__ == '__main__':
    input_list = [1, 1, 1, 2, 2, 3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)

#留言板