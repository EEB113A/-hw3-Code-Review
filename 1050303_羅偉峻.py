def sort_by_occurrence(nums):
    #create dict
    nums_dict = {}
    for num in nums:
        #distinguish whether the number exist or not
        if num in nums_dict.keys():
            nums_dict[num] += 1
        else:
            nums_dict[num] = 1

    #arrange in order of the number of occurrence
    a1_sorted_keys = sorted(nums_dict, key=nums_dict.get, reverse=False)
    return a1_sorted_keys

if __name__ == '__main__':
    input_list = [1,1,1,2,2,3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)




#留言板