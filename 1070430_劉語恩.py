def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    # Sort the input list nums by key which counts the occurrence of each item
    sort_by_occurrence_list = sorted(nums, key=lambda num: nums.count(num))
    # 去除列表內重複物件
    # noReapt_list = []
    # for i in range(len(sort_by_occurrence_list)):
    #     if sort_by_occurrence_list[i] not in noReapt_list:
    #             noReapt_list.append(sort_by_occurrence_list[i])
    # return noReapt_list
    # 等同上面(使用comprehension執行效率較高，重複使用命名列表sort_by_occurrence_list減少記憶體使用空間並增加可讀性)
    return [i for n, i in enumerate(sort_by_occurrence_list) if i not in  sort_by_occurrence_list[:n]]


if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    # test input
    input_list = [1, 1, 1, 2, 2, 3]
    # input_list = [5,5,6,6,6,6,0,1,1,1]
    # input_list = [2,0,9,8,9,2,8,2,0,9,7,9,8,2,9]
    # Call own function sort_by_occurrence
    output_list = sort_by_occurrence(input_list)
    # Output the result
    print(output_list)


#留言板