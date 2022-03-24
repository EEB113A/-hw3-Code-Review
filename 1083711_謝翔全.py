def sort_by_occurrence(nums):
    sortedlist = sorted(set(nums), key = lambda elements: nums.count(elements)) #sorted()可以依序排列list，set()可以去除重複的元素，count()可用來計算元素出現次數，key為sorted()決定的排列方式
    return sortedlist
    
if __name__ == '__main__':
    input_list = [1, 1, 1, 2, 2, 3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板