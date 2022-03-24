def sort_by_occurrence(nums):
    dict1 = {}
    dict2 = {}
    key = list(set(input_list))
    
    for item in key:
        val = list(str(input_list.count(item)))
        dict1[item] = val    

    dict2.update(sorted(dict1.items(), key=lambda x:x[1]))
    nums = list(dict2.keys())
    return nums

        

if __name__ == '__main__':
    

    input_list = [7,7,8,8,8,9]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板